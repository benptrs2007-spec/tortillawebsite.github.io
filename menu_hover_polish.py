import glob
import os
import re

hover_styles = """
        .nav-links a {
            position: relative;
            text-decoration: none;
            color: var(--accent-dark);
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: color 0.3s ease;
        }
        .nav-links a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 1.5px;
            bottom: -4px;
            left: 50%;
            background-color: #7d6e53; /* Using your brand accent color */
            transition: all 0.3s ease;
            transform: translateX(-50%);
        }
        .nav-links a:hover {
            color: #7d6e53;
        }
        .nav-links a:hover::after {
            width: 100%;
        }
"""

def apply_menu_animations():
    for fpath in glob.glob("*.html"):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace the simple .nav-links a definition with the animated version
        # We look for the block that matches the original pattern
        nav_pattern = r'\.nav-links a \{\s*text-decoration: none;\s*color: var\(--accent-dark\);\s*font-size: 0\.75rem;\s*font-weight: 600;\s*text-transform: uppercase;\s*letter-spacing: 1px;\s*\}'
        
        if re.search(nav_pattern, content):
            content = re.sub(nav_pattern, hover_styles.strip(), content)
        else:
            # If it's already modified or looks different, let's try a broader match or just append
            # But based on my previous view_file, it should match.
            # I'll also check if the animation is already there to avoid duplicates
            if ".nav-links a::after" not in content:
                 content = content.replace("</style>", hover_styles + "\n</style>")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
    print("Menu hover animations applied to all pages.")

if __name__ == "__main__":
    apply_menu_animations()
