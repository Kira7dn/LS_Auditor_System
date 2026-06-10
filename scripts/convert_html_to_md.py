import argparse
import html
import json
import logging
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("html_converter")


BLOCK_TAGS = {
    "address",
    "article",
    "aside",
    "blockquote",
    "div",
    "dl",
    "fieldset",
    "figcaption",
    "figure",
    "footer",
    "form",
    "header",
    "hr",
    "main",
    "nav",
    "ol",
    "p",
    "pre",
    "section",
    "table",
    "ul",
}


class MarkdownHTMLParser(HTMLParser):
    def __init__(self, content_id: str | None = None, drop_notices: bool = True):
        super().__init__(convert_charrefs=False)
        self.content_id = content_id
        self.drop_notices = drop_notices
        self.capture = content_id is None
        self.capture_depth = 0
        self.skip_stack: list[str] = []
        self.blocks: list[str] = []
        self.current: list[str] = []
        self.heading_level: int | None = None
        self.in_li = False
        self.in_cell = False
        self.row_cells: list[str] = []
        self.cell_text: list[str] = []
        self.title: str | None = None
        self.in_title = False
        self.title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs_dict = {k.lower(): (v or "") for k, v in attrs}

        if tag == "title":
            self.in_title = True

        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_stack.append(tag)
            return

        if self.content_id and not self.capture and attrs_dict.get("id") == self.content_id:
            self.capture = True
            self.capture_depth = 1
            return

        if not self.capture:
            return

        if self.content_id:
            self.capture_depth += 1

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._flush_current()
            self.heading_level = int(tag[1])
        elif tag == "p":
            self._flush_current()
        elif tag == "br":
            self._append_text("\n")
        elif tag == "li":
            self._flush_current()
            self.in_li = True
        elif tag == "tr":
            self._flush_current()
            self.row_cells = []
        elif tag in {"td", "th"}:
            self.in_cell = True
            self.cell_text = []
        elif tag in BLOCK_TAGS:
            self._flush_current()

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()

        if tag == "title":
            self.in_title = False
            title = self._clean_text(" ".join(self.title_parts))
            if title:
                self.title = title

        if self.skip_stack:
            if self.skip_stack[-1] == tag:
                self.skip_stack.pop()
            return

        if not self.capture:
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._flush_current()
            self.heading_level = None
        elif tag == "li":
            self._flush_current()
            self.in_li = False
        elif tag in {"td", "th"}:
            self.in_cell = False
            cell = self._clean_text(" ".join(self.cell_text))
            self.row_cells.append(cell)
            self.cell_text = []
        elif tag == "tr":
            if self.row_cells:
                self.blocks.append("| " + " | ".join(self._escape_table(c) for c in self.row_cells) + " |")
            self.row_cells = []
        elif tag in BLOCK_TAGS:
            self._flush_current()

        if self.content_id:
            self.capture_depth -= 1
            if self.capture_depth <= 0:
                self.capture = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

        if self.skip_stack or not self.capture:
            return

        text = html.unescape(data)
        if self.in_cell:
            self.cell_text.append(text)
        else:
            self._append_text(text)

    def handle_entityref(self, name: str) -> None:
        self.handle_data(f"&{name};")

    def handle_charref(self, name: str) -> None:
        self.handle_data(f"&#{name};")

    def finish(self) -> str:
        self._flush_current()
        title = self.title or "Converted HTML"
        body = "\n\n".join(block for block in self.blocks if block.strip())
        return f"# {title}\n\n{body}\n"

    def _append_text(self, text: str) -> None:
        if not text:
            return
        self.current.append(text)

    def _flush_current(self) -> None:
        if not self.current:
            return

        raw = " ".join(self.current)
        text = self._clean_text(raw)
        self.current = []

        if not text or self._should_drop(text):
            return

        if self.heading_level:
            self.blocks.append(f"{'#' * self.heading_level} {text}")
        elif self.in_li:
            self.blocks.append(f"- {text}")
        else:
            self.blocks.append(text)

    def _should_drop(self, text: str) -> bool:
        if not self.drop_notices:
            return False
        lowered = text.lower()
        if "tvpl" in lowered and "pro" in lowered and ("dang nhap" in self._ascii_fold(lowered) or "thanh vien" in self._ascii_fold(lowered)):
            return True
        if "mọi chi tiết xin liên hệ" in lowered or "moi chi tiet xin lien he" in self._ascii_fold(lowered):
            return True
        return False

    @staticmethod
    def _clean_text(text: str) -> str:
        text = text.replace("\xa0", " ")
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        text = re.sub(r"\n\s*\n+", "\n", text)
        text = re.sub(r"\s*\n\s*", "\n", text)
        return text.strip()

    @staticmethod
    def _escape_table(text: str) -> str:
        return text.replace("|", "\\|").replace("\n", " ")

    @staticmethod
    def _ascii_fold(text: str) -> str:
        table = str.maketrans(
            "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ",
            "aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuyyyyyd",
        )
        return text.translate(table)


def convert_html_to_md(input_path: Path, output_path: Path, content_id: str | None, overwrite: bool) -> dict:
    if output_path.exists() and not overwrite:
        logger.info("Skipping already converted file: %s", output_path)
        return {"file": str(input_path), "status": "skipped"}

    try:
        html_text = input_path.read_text(encoding="utf-8", errors="replace")
        parser = MarkdownHTMLParser(content_id=content_id)
        parser.feed(html_text)
        md = parser.finish()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(md, encoding="utf-8")
        return {"file": str(input_path), "status": "success", "output": str(output_path)}
    except Exception as exc:
        logger.error("Error converting %s: %s", input_path, exc, exc_info=True)
        return {"file": str(input_path), "status": "error", "error_message": str(exc)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert an HTML file to Markdown.")
    parser.add_argument("--input", required=True, help="Input HTML file")
    parser.add_argument("--output", default=None, help="Output Markdown file. Defaults to input path with .md suffix.")
    parser.add_argument("--content-id", default="divContentDoc", help="Only extract content from an element with this id. Use an empty string to parse the whole file.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite output file if it exists")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".md")
    content_id = args.content_id or None

    if not input_path.exists() or not input_path.is_file():
        result = {
            "status": "error",
            "error_code": "INVALID_INPUT",
            "message": f"Input file {input_path} does not exist or is not a file.",
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(1)

    result = convert_html_to_md(input_path, output_path, content_id, args.overwrite)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if result["status"] == "error":
        sys.exit(1)


if __name__ == "__main__":
    main()
