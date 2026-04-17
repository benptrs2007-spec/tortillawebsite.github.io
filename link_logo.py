import glob
import os
import re

def link_header_logo():
    for fpath in glob.glob("*.html"):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Wrap the header logo img with an anchor tag to index.html
        # We target the img inside the logo-container
        # Pattern: <img src="logotransparent-2.webp" alt="J&D Peters Logo">
        pattern = r'(<div class="logo-container">.*?)(<img src="logotransparent-2.webp" alt="J&D Peters Logo">)'
        replacement = r'\1<a href="index.html">\2</a>'
        
        # Check if already linked to avoid double-wrapping
        if '<a href="index.html"><img src="logotransparent-2.webp"' not in content:
            new_content = re.sub(pattern, replacement, content, flags=re.S)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)

if __name__ == "__main__":
    link_header_logo()
    print("Header logos linked to homepage.")
