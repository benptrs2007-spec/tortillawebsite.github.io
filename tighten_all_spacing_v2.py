import glob
import os
import re

for fpath in glob.glob("*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Restore desktop spacing (first occurrence of the block) to 220px
    # Using a non-greedy search or count=1
    content = re.sub(r'(\.container, \.hero, \.map-hero, \.contact-container)\s*\{\s*padding-top:\s*125px\s*!important;\s*\}', r'\1 { padding-top: 220px !important; }', content, count=1)
    
    # 2. Tighten mobile spacing (any remaining 125px or high values) to 120px
    content = re.sub(r'padding-top:\s*(?:125|190|240)\s*px\s*!important;', r'padding-top: 120px !important;', content)
    
    # Specifically target any remaining product detail or page container mobile styles
    content = re.sub(r'(\.page-container|\.shop-container|\.product-detail-container)\s*\{\s*padding-top:\s*\d+px\s*!important;\s*\}', r'\1 { padding-top: 120px !important; }', content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Tightened mobile spacing to 120px and restored desktop spacing.")
