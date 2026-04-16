import os
import glob
import re

html_files = glob.glob("*.html")

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 1. Update dropdown
    # Single-line format (index.html usually)
    old_dropdown_single = r'<li><a href="tallow-chips\.html">Tallow</a></li></ul></li>'
    new_dropdown_single = r'<li><a href="tallow-chips.html">Tallow</a></li><li><a href="variety-box.html">Variety Box</a></li></ul></li>'
    content = re.sub(old_dropdown_single, new_dropdown_single, content)
    
    # Multi-line format
    old_dropdown_multi = r'<li><a href="tallow-chips\.html">Tallow</a></li>\s*</ul>\s*</li>'
    new_dropdown_multi = r'<li><a href="tallow-chips.html">Tallow</a></li>\n                            <li><a href="variety-box.html">Variety Box</a></li>\n                        </ul>\n                    </li>'
    content = re.sub(old_dropdown_multi, new_dropdown_multi, content)

    # 2. Update titles in product pages (dill-pickle-chips.html etc)
    # The title looks like <h1>Something Tortilla Chips</h1>
    # We want <h1>Something <span class="cursive">Tortilla Chips</span></h1>
    # Same for Variety Chip Box -> Variety <span class="cursive">Chip Box</span>
    if fpath.endswith("-chips.html") or fpath == "variety-box.html":
        # First, find if we already added it so we don't double replace
        if '<span class="cursive">' not in content.split('<h1>')[1].split('</h1>')[0] if '<h1>' in content else True:
            # Replace Tortilla Chips or Chip Box
            content = re.sub(r'(<h1>.*?)(Tortilla Chips|Chip Box)(</h1>)', r'\1<span class="cursive">\2</span>\3', content)
            
    # 3. Remove description only on tallow-chips.html
    if fpath == "tallow-chips.html":
        content = re.sub(r'<p class="description">.*?</p>', '', content, flags=re.DOTALL)
        
    with open(fpath, "w", encoding="utf-8") as file:
        file.write(content)

print("Batch updates applied successfully.")
