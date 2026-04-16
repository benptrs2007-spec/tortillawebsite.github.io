import glob
import os

mobile_cart_css = """
        @media (max-width: 900px) {
            .glass-nav-wrapper {
                position: relative;
            }
            paypal-cart-button[data-id="pp-view-cart"] {
                position: absolute;
                left: 15px;
                top: 18px;
                z-index: 1002;
            }
            .hamburger {
                right: 15px;
                top: 10px; /* Adjusted slightly to look balanced */
            }
        }
"""

for fpath in glob.glob("*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Add CSS for mobile cart positioning
    if "paypal-cart-button[data-id=\"pp-view-cart\"]" not in content:
        # Insert before the end of the style tag that our previous script may have added or the original
        if "/* Hamburger Menu Styles */" in content:
            content = content.replace("/* Hamburger Menu Styles */", mobile_cart_css + "\n        /* Hamburger Menu Styles */")
        else:
            content = content.replace("</style>", mobile_cart_css + "\n</style>")
            
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Mobile cart positioning added to all pages.")
