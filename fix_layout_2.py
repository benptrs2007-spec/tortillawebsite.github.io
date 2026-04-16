import glob
import re

html_files = glob.glob("*-chips.html")

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
    
    def replacer(match):
        wrapper_css = match.group(0)
        if 'flex-direction: column;' not in wrapper_css:
            wrapper_css = wrapper_css.replace('display: flex;', 'display: flex;\n            flex-direction: column;\n            align-items: center;')
        return wrapper_css
        
    content = re.sub(r'\.product-image-wrapper\s*\{[^}]*\}', replacer, content)

    with open(fpath, "w", encoding="utf-8") as file:
        file.write(content)

print("Layout accurately fixed.")
