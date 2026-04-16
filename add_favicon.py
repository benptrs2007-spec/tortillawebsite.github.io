import glob
import os

favicon_link = '<link rel="icon" type="image/x-icon" href="favicon.ico">'

for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if favicon_link not in content:
        content = content.replace('</head>', f'    {favicon_link}\n</head>')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
print('Added favicon to all HTML files.')
