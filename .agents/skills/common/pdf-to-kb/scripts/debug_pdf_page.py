"""
debug_pdf_page.py
=================
Debug font sizes, styles, flags, and classification of all text spans on a specific PDF page.
Tuân thủ nghiêm ngặt bộ tiêu chuẩn SCRIPT_STANDARDS.md (AI-First Scripting).

Usage:
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/debug_pdf_page.py --pdf document.pdf --page 12
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/debug_pdf_page.py --pdf document.pdf --page 12 --config resources/font_config.json

Output (stdout):
  JSON array of text spans and classification details.
All logs/progress are routed to stderr.
"""
import sys
import os
import json
import argparse
from typing import Dict, List, Any
import fitz  # PyMuPDF

def load_font_config(config_path: str) -> Dict[str, Any]:
    if not config_path or not os.path.exists(config_path):
        # Default fallback config
        return {
            "h2_min_size": 12.5,
            "h3_min_size": 10.0,
            "h3_max_len": 100,
            "h3_no_trailing_punct": True,
            "callout_max_size": 9.5,
            "callout_min_len": 8
        }
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Failed to load config from {config_path}: {e}. Using defaults.", file=sys.stderr)
        return load_font_config("")

def main():
    try:
        parser = argparse.ArgumentParser(description="Debug text spans on a PDF page.")
        parser.add_argument("--pdf", required=True, help="Path to the PDF file")
        parser.add_argument("--page", type=int, required=True, help="1-based page number to debug")
        parser.add_argument("--config", help="Path to font_config.json")
        args = parser.parse_args()

        if not os.path.exists(args.pdf):
            raise FileNotFoundError(f"PDF file not found: {args.pdf}")

        config = load_font_config(args.config or "")
        
        doc = fitz.open(args.pdf)
        if args.page < 1 or args.page > len(doc):
            raise ValueError(f"Page number must be between 1 and {len(doc)}")
            
        page = doc[args.page - 1]
        blocks = page.get_text("dict")["blocks"]
        
        print(f"=== Debugging PDF: {args.pdf} | Page: {args.page} ===", file=sys.stderr)
        print(f"Loaded Config: {json.dumps(config, indent=2)}", file=sys.stderr)
        print(f"{'Text':<50} | {'Size':<6} | {'Bold':<4} | {'Len':<4} | {'Classification':<15}", file=sys.stderr)
        print("-" * 90, file=sys.stderr)
        
        spans_list = []
        
        for b in blocks:
            if "lines" not in b:
                continue
            for l in b["lines"]:
                for s in l["spans"]:
                    text = s["text"].strip()
                    if not text:
                        continue
                        
                    size = s["size"]
                    flags = s["flags"]
                    bold_flag = config.get("bold_flag", 16)
                    is_bold = bool(flags & bold_flag)
                    
                    # Classify matching the extract_pdf_to_kb logic
                    classification = "body"
                    
                    # Rule 1: Skip very small
                    if size < 7.5:
                        classification = "skip (<7.5pt)"
                    # Rule 2: Box label
                    elif text.upper().startswith(("BOX ", "FIGURE ", "TABLE ", "APPENDIX ")):
                        classification = "box_label"
                    # Rule 3: H2
                    elif size >= config.get("h2_min_size", 12.5) and is_bold:
                        classification = "h2"
                    # Rule 4: H3
                    elif config.get("h3_min_size", 10.0) <= size < config.get("h2_min_size", 12.5) and is_bold:
                        has_trailing_punct = len(text) > 0 and text[-1] in (".", ":", "?", "!")
                        too_long = len(text) >= config.get("h3_max_len", 100)
                        
                        if too_long:
                            classification = "body (h3: too long)"
                        elif config.get("h3_no_trailing_punct", True) and has_trailing_punct:
                            classification = "body (h3: trailing punct)"
                        else:
                            classification = "h3"
                    # Rule 5: Callout
                    elif size <= config.get("callout_max_size", 9.5) and not is_bold:
                        if len(text) > config.get("callout_min_len", 8):
                            classification = "callout"
                        else:
                            classification = "skip (callout too short)"
                    
                    span_item = {
                        "text": text,
                        "size": size,
                        "bold": is_bold,
                        "len": len(text),
                        "classification": classification
                    }
                    spans_list.append(span_item)
                    
                    # Truncate text for display to stderr
                    disp_text = text[:47] + "..." if len(text) > 50 else text
                    print(f"{disp_text:<50} | {size:<6.2f} | {str(is_bold):<4} | {len(text):<4} | {classification:<15}", file=sys.stderr)
        
        # Output pure JSON array to stdout
        print(json.dumps(spans_list, indent=2, ensure_ascii=False))

    except Exception as e:
        error_json = {
            "status": "error",
            "error_code": type(e).__name__,
            "message": str(e),
            "suggestion": "Check input PDF path, page number, or config path."
        }
        print(json.dumps(error_json, indent=2, ensure_ascii=False))
        sys.exit(1)

if __name__ == "__main__":
    main()
