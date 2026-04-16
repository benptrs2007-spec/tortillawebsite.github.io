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
                justify-content: flex-start;
                padding: 15px 10px !important;
            }
            .logo-container {
                margin-bottom: 0 !important;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                min-height: 55px;
            }
            .logo-container img {
                height: 55px !important;
                max-width: 200px;
                object-fit: contain;
                margin: 0 !important;
            }
            .hamburger { 
                display: flex !important;
                position: absolute !important;
                right: 12px !important;
                top: 23px !important;
                margin: 0 !important;
            }
            paypal-cart-button[data-id="pp-view-cart"] {
                display: block !important;
                position: absolute !important;
                left: 12px !important;
                top: 23px !important;
                margin: 0 !important;
                z-index: 1002;
            }
            .hero, .page-container, .shop-container, .product-detail-container, .map-hero, .contact-container, .container {
                padding-top: 120px !important;
            }
            .nav-links {
                display: none !important;
                flex-direction: column;
                width: 100%;
                text-align: center;
                padding: 15px 0;
                gap: 15px !important;
                border-top: 1px solid rgba(0,0,0,0.06);
                margin-top: 15px;
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
    
    # 1. Strip out all previous additions
    content = re.sub(r'/\* Final Mobile Header Base Styles \*/.*?</style>', '</style>', content, flags=re.S)
    content = re.sub(r'/\* Final Mobile Header Styles \*/.*?</style>', '</style>', content, flags=re.S)
    content = re.sub(r'/\* Hamburger and Cart Styles \*/.*?</style>', '</style>', content, flags=re.S)
    content = re.sub(r'/\* Hamburger Menu Styles \*/.*?</style>', '</style>', content, flags=re.S)
    content = re.sub(r'\s*@media \(max-width: 900px\)\s*\{[^{}]*(?:hamburger|paypal-cart-button|glass-nav-wrapper)[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', '', content)

    # Replace existing desktop padding if it was messed up by previous scripts
    content = re.sub(r'(\.container, \.hero, \.map-hero, \.contact-container)\s*\{\s*padding-top:\s*120px\s*!important;\s*\}', r'\1 { padding-top: 220px !important; }', content)

    # 2. Re-insert the full correct version
    content = content.replace("</style>", final_styles + "\n</style>")
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Fixed mobile gaps on all pages.")
