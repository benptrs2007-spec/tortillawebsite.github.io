import glob
import os
import re

clean_mobile_header = """
        /* Final Mobile Header Styles */
        @media (max-width: 900px) {
            .glass-nav-wrapper {
                position: relative;
                min-height: 70px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .logo-container {
                margin-bottom: 0 !important;
            }
            .hamburger { 
                display: flex !important;
                position: absolute !important;
                right: 15px !important;
                top: 15px !important;
                margin: 0 !important;
            }
            paypal-cart-button[data-id="pp-view-cart"] {
                display: block !important;
                position: absolute !important;
                left: 15px !important;
                top: 15px !important;
                margin: 0 !important;
                z-index: 1002;
            }
            .nav-links {
                display: none !important;
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
                width: 100%;
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

for fpath in glob.glob("*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Identify the start of where our messy additions began
    # It usually starts after the standard product/hero styles
    
    # We'll search for the first instance of a media query we added
    # Or just use the markers we know
    
    # First, revert to a state without our custom styles if possible
    content = re.sub(r'/\* Hamburger Menu Styles \*/.*?</style>', '</style>', content, flags=re.S)
    content = re.sub(r'/\* Hamburger and Cart Styles \*/.*?</style>', '</style>', content, flags=re.S)
    
    # Also remove any "orphaned" media query blocks that don't have markers but match our addition pattern
    content = re.sub(r'\s*@media \(max-width: 900px\)\s*\{[^{}]*(?:hamburger|paypal-cart-button)[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', '', content)

    # Re-insert the clean version
    content = content.replace("</style>", clean_mobile_header + "\n</style>")
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Master cleanup and finalization complete.")
