import glob
import os
import re

for fpath in glob.glob("*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace any padding-top in the mobile area with 125px
    # We target .hero, .container, .page-container, .shop-container, etc.
    content = re.sub(r'(\.hero|\.container|\.page-container|\.shop-container|\.product-detail-container|\.map-hero|\.contact-container)\s*\{\s*padding-top:\s*\d+px\s*!important;\s*\}', r'\1 { padding-top: 125px !important; }', content)
    
    # Also handle the broader selector if it exists
    content = re.sub(r'(\.container, \.hero, \.map-hero, \.contact-container)\s*\{\s*padding-top:\s*\d+px\s*!important;\s*\}', r'\1 { padding-top: 125px !important; }', content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Tightened spacing to 125px on all pages.")
