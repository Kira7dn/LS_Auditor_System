import argparse
import json
import logging
import os
import sys
from pathlib import Path
from pypdf import PdfReader

# Configure logging to stderr to comply with AI-First Scripting Standards
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr
)
logger = logging.getLogger("pdf_converter")

def convert_pdf_to_md(pdf_path: Path, md_path: Path, overwrite: bool = False) -> dict:
    """Converts a single PDF file to a Markdown file page-by-page.
    
    Args:
        pdf_path: Path to the input PDF file.
        md_path: Path to the output MD file.
        overwrite: If True, overwrites existing MD file.
        
    Returns:
        dict: Summary of the conversion result.
    """
    if md_path.exists() and not overwrite:
        logger.info(f"Skipping already converted file: {md_path}")
        return {"file": str(pdf_path), "status": "skipped", "pages": 0}
        
    try:
        logger.info(f"Converting {pdf_path} to {md_path}...")
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        
        md_content = []
        md_content.append(f"# {pdf_path.stem}\n\n")
        md_content.append(f"- Converted from: `{pdf_path.name}`\n")
        md_content.append(f"- Total Pages: {total_pages}\n\n---\n\n")
        
        for idx, page in enumerate(reader.pages):
            page_num = idx + 1
            text = page.extract_text()
            md_content.append(f"## Page {page_num}\n\n")
            if text:
                md_content.append(text)
            else:
                md_content.append("*[Empty page or image-only page]*")
            md_content.append("\n\n---\n\n")
            
        md_path.parent.mkdir(parents=True, exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as f:
            f.writelines(md_content)
            
        return {"file": str(pdf_path), "status": "success", "pages": total_pages}
        
    except Exception as e:
        logger.error(f"Error converting {pdf_path}: {e}", exc_info=True)
        return {"file": str(pdf_path), "status": "error", "error_message": str(e)}

def main() -> None:
    parser = argparse.ArgumentParser(description="Convert PDF files to Markdown format.")
    parser.add_argument("--src-dir", type=str, required=True, help="Directory containing PDF files")
    parser.add_argument("--out-dir", type=str, default=None, help="Directory to save MD files. Defaults to src-dir.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing MD files")
    
    args = parser.parse_args()
    
    src_dir = Path(args.src_dir)
    out_dir = Path(args.out_dir) if args.out_dir else src_dir
    
    if not src_dir.exists() or not src_dir.is_dir():
        error_res = {
            "status": "error",
            "error_code": "INVALID_SOURCE",
            "message": f"Source directory {src_dir} does not exist or is not a directory.",
            "suggestion": "Check the --src-dir argument."
        }
        print(json.dumps(error_res, indent=2))
        sys.exit(1)
        
    # Find all PDFs
    pdf_files = list(src_dir.rglob("*.pdf"))
    logger.info(f"Found {len(pdf_files)} PDF files in {src_dir}")
    
    results = []
    
    for pdf_path in pdf_files:
        # Determine output path maintaining the hierarchy
        relative_path = pdf_path.relative_to(src_dir)
        md_path = out_dir / relative_path.with_suffix(".md")
        
        res = convert_pdf_to_md(pdf_path, md_path, overwrite=args.overwrite)
        results.append(res)
        
    # Standard JSON Output via stdout
    final_output = {
        "status": "success",
        "converted_files_count": len([r for r in results if r["status"] == "success"]),
        "skipped_files_count": len([r for r in results if r["status"] == "skipped"]),
        "failed_files_count": len([r for r in results if r["status"] == "error"]),
        "details": results
    }
    print(json.dumps(final_output, indent=2))

if __name__ == "__main__":
    main()
