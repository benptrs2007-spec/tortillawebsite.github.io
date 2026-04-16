import glob
import os

hamburger_html = '<button class="hamburger"><span></span><span></span><span></span></button>'
hamburger_css = """
        /* Hamburger Menu Styles */
        .hamburger {
            display: none;
            cursor: pointer;
            background: none;
            border: none;
            padding: 10px;
            z-index: 1001;
            flex-direction: column;
            gap: 5px;
        }
        .hamburger span {
            display: block;
            width: 25px;
            height: 3px;
            background: var(--accent-dark);
            border-radius: 3px;
            transition: 0.3s;
        }

        @media (max-width: 900px) {
            .hamburger { 
                display: flex;
                position: absolute;
                right: 20px;
                top: 20px;
            }
            .nav-links {
                display: none !important; /* Hide by default on mobile */
                flex-direction: column;
                width: 100%;
                text-align: center;
                padding: 20px 0;
                gap: 15px !important;
            }
            .nav-links.active {
                display: flex !important;
            }
            .nav-inner {
                flex-direction: column;
            }
            .dropdown-menu {
                position: static !important;
                transform: none !important;
                opacity: 1 !important;
                visibility: visible !important;
                box-shadow: none !important;
                background: none !important;
                padding: 0 !important;
                display: none;
            }
            .dropdown.active .dropdown-menu {
                display: block;
            }
        }
"""

hamburger_js = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const hamburger = document.querySelector('.hamburger');
            const navLinks = document.querySelector('.nav-links');
            
            if (hamburger && navLinks) {
                hamburger.addEventListener('click', function() {
                    navLinks.classList.toggle('active');
                });
            }
            
            const dropdowns = document.querySelectorAll('.dropdown');
            dropdowns.forEach(dropdown => {
                dropdown.addEventListener('click', function(e) {
                    if (window.innerWidth <= 900) {
                        this.classList.toggle('active');
                        e.stopPropagation();
                    }
                });
            });
        });
    </script>
"""

for fpath in glob.glob("*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Add CSS if not present
    if "/* Hamburger Menu Styles */" not in content:
        content = content.replace("</style>", hamburger_css + "\n</style>")
    
    # Add Hamburger Button if not present
    if 'class="hamburger"' not in content:
        content = content.replace('<div class="logo-container">', '<div class="logo-container">\n            ' + hamburger_html)
        
    # Add JS if not present
    if "const hamburger = document.querySelector" not in content:
        content = content.replace("</body>", hamburger_js + "\n</body>")
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Hamburger menu added to all pages.")
