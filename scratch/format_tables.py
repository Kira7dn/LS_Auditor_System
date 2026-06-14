# -*- coding: utf-8 -*-
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

input_path = "Projects/ESG/kb/qd226_btnmt/01_phu_luc_I_nang_luong.md"
with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_content = []
in_frontmatter = False
frontmatter_lines = []

for line in lines:
    if line.strip() == "---":
        if not in_frontmatter and len(frontmatter_lines) == 0:
            in_frontmatter = True
            frontmatter_lines.append(line)
            continue
        elif in_frontmatter:
            in_frontmatter = False
            frontmatter_lines.append(line)
            continue
    if in_frontmatter:
        frontmatter_lines.append(line)

new_content.extend(frontmatter_lines)
new_content.append("\n")

# Let's inspect the sections
# We want to format everything below the frontmatter.
# Let's build a parser that finds ## Page X headings and parses the text into tables.

text_content = "".join(lines[len(frontmatter_lines):])

# We can split by ## Page X or similar.
pages = re.split(r'(## Page \d+)', text_content)

header = "| STT | Tên hệ số phát thải | Loại khí | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp |\n|---|---|---|---|---|---|---|\n"

# Let's process each page segment.
# If a page contains row patterns like:
# "1.1  Hệ số phát thải CO2 của than antraxit  CO2 Công nghiệp năng lượng 98.300 Kg CO2/TJ Bậc 1"
# we convert them to a table row.

# Let's write a regex for row extraction.
# Group 1: STT (e.g., 1.1 or 2.1)
# Group 2: Name (e.g., "Hệ số phát thải CO2 của than antraxit")
# Group 3: Gas (e.g., "CO2", "CH4", "N2O")
# Group 4: Source (e.g., "Công nghiệp năng lượng")
# Group 5: Value (e.g., "98.300", "1", "1,5", "0,00000064")
# Group 6: Unit (e.g., "Kg CO2/TJ", "Kg CH4/TJ", "m3CH4/tấn", "Nghìn tấn CO2/103m3 tổng sản phẩm dầu")
# Group 7: Method (e.g., "Bậc 1", "Bậc 2")

for i in range(1, len(pages), 2):
    page_header = pages[i]
    page_text = pages[i+1]
    
    # We should preserve page anchors like <a id="qd226_btnmt_page_X"></a>
    anchor = ""
    anchor_match = re.search(r'(<a id="qd226_btnmt_page_\d+"></a>)', page_text)
    if anchor_match:
        anchor = anchor_match.group(1) + "\n"
        page_text = page_text.replace(anchor_match.group(1), "")
        
    # Clean page_text lines
    sub_lines = [l.strip() for l in page_text.split("\n") if l.strip()]
    
    table_rows = []
    other_lines = []
    
    for sub_line in sub_lines:
        # Match pattern
        # STT pattern: e.g. "1.10" or "2.12"
        # Since some rows are split across lines, let's look at them.
        # Wait, some lines are:
        # "1 Các hoạt động đốt nhiên liệu"
        # "2 Phát thải do phát tán"
        if sub_line.startswith("1 ") and "đốt nhiên liệu" in sub_line:
            other_lines.append(f"### 1. {sub_line[2:].strip()}")
            continue
        elif sub_line.startswith("2 ") and "Phát thải do phát tán" in sub_line:
            other_lines.append(f"### 2. {sub_line[2:].strip()}")
            continue
        
        # Regex to try parsing a complete line
        # Match STT
        m = re.match(r"^(\d+\.\d+)\s+(.*?)\s+(CO2|CH4|N2O)\s+(.*?)\s+([\d,.]+E?[-+]?\d*)\s+(.*?)\s+(Bậc \d+)", sub_line)
        if m:
            stt, name, gas, source, val, unit, method = m.groups()
            table_rows.append((stt, name, gas, source, val, unit, method))
        else:
            # Let's log unmatched lines to manually inspect or handle them
            other_lines.append(sub_line)
            
    # Print unmatched lines for diagnostics
    print(f"--- {page_header} ---")
    print("Unmatched:")
    for ol in other_lines:
        if not ol.startswith("###"):
            print("  ", ol)
            
    # Let's reconstruct page content
    page_out = []
    if anchor:
        page_out.append(anchor)
    page_out.append(page_header + "\n")
    
    # Render heading categories
    for ol in other_lines:
        if ol.startswith("###"):
            page_out.append(ol + "\n")
            
    if table_rows:
        page_out.append(header)
        for row in table_rows:
            page_out.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} |\n")
        page_out.append("\n")
        
    # Rest of unmatched lines
    remaining_text = []
    for ol in other_lines:
        if not ol.startswith("###"):
            remaining_text.append(ol)
    if remaining_text:
        page_out.append("\n".join(remaining_text) + "\n")
        
    new_content.append("".join(page_out))
    if i < len(pages) - 2:
        new_content.append("---\n\n")

print("Processed all pages.")
