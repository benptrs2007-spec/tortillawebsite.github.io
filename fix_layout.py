import glob
import re

html_files = glob.glob("*-chips.html")

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 1. Remove ingredients-box from logo-container
    # Match the image tag and the div immediately following it
    pattern_logo = r'(<img src="logotransparent-2\.webp" alt="J&D Peters Logo">)\s*<div class="ingredients-box".*?</div>'
    content = re.sub(pattern_logo, r'\1', content, flags=re.DOTALL)
    
    # 2. Add flex-direction: column; align-items: center; to .product-image-wrapper CSS
    if 'flex-direction: column;' not in content and '.product-image-wrapper {' in content:
        content = content.replace(
            '.product-image-wrapper {',
            '.product-image-wrapper {\n            flex-direction: column;\n            align-items: center;'
        )
        
    with open(fpath, "w", encoding="utf-8") as file:
        file.write(content)

print("Layout fixed.")
