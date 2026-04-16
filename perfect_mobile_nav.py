import glob
import os
import re

final_styles = """
        /* Final Mobile Header Base Styles */
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
            .glass-nav-wrapper {
                position: relative;
                min-height: 70px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 12px 10px !important;
            }
            .logo-container {
                margin-bottom: 0 !important;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
            }
            .logo-container img {
                height: 40px !important; /* Smaller logo to prevent overlap */
                max-width: 160px;
                object-fit: contain;
                margin: 0 !important;
            }
            .hamburger { 
                display: flex !important;
                position: absolute !important;
                right: 12px !important;
                top: 50%;
                transform: translateY(-50%);
                padding: 5px !important;
                margin: 0 !important;
            }
            paypal-cart-button[data-id="pp-view-cart"] {
                display: block !important;
                position: absolute !important;
                left: 12px !important;
                top: 50%;
                transform: translateY(-50%);
                margin: 0 !important;
                z-index: 1002;
            }
            .nav-links {
                display: none !important;
                flex-direction: column;
                width: 100%;
                text-align: center;
                padding: 15px 0;
                gap: 12px !important;
                border-top: 1px solid rgba(0,0,0,0.05);
                margin-top: 10px;
            }
            .nav-links.active {
                display: flex !important;
            }
            .nav-inner {
                flex-direction: column;
                width: 100%;
                border-top: none !important;
                padding-top: 0 !important;
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
    
    # Clean up all previous additions
    content = re.sub(r'/\* Final Mobile Header Base Styles \*/.*?</style>', '</style>', content, flags=re.S)
    content = re.sub(r'/\* Final Mobile Header Styles \*/.*?</style>', '</style>', content, flags=re.S)
    content = re.sub(r'/\* Hamburger and Cart Styles \*/.*?</style>', '</style>', content, flags=re.S)
    content = re.sub(r'/\* Hamburger Menu Styles \*/.*?</style>', '</style>', content, flags=re.S)
    content = re.sub(r'\s*@media \(max-width: 900px\)\s*\{[^{}]*(?:hamburger|paypal-cart-button|glass-nav-wrapper)[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', '', content)

    # Re-insert the perfect Version
    content = content.replace("</style>", final_styles + "\n</style>")
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Perfected mobile navigation spacing.")
