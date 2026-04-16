import glob
import os
import re

clean_mobile_header = """
        /* Hamburger and Cart Styles */
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
    
    # Remove previous blocks more carefully
    # We remove anything between our previous marker comments if we had any, or the generated blocks
    
    # Remove any media query block that mentions hamburger and cart button
    content = re.sub(r'\s*@media \(max-width: 900px\)\s*\{[^{}]*(?:hamburger|paypal-cart-button)[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', '', content)
    
    # Re-insert the clean version
    content = content.replace("</style>", clean_mobile_header + "\n</style>")
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Finalized mobile header on all pages.")
