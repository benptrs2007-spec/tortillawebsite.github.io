import glob

html_files = glob.glob("*.html")

common_mobile_css = """
            .glass-nav-wrapper { padding: 10px 15px !important; border-radius: 20px !important; }
            .nav-inner { gap: 8px !important; padding-top: 5px !important; }
            .nav-links { gap: 8px !important; padding-top: 5px !important; }
            .nav-links a { font-size: 0.6rem !important; letter-spacing: 0 !important; }
            .logo-container img { height: 50px !important; margin-bottom: 5px !important; }
            .promo-banner { padding: 8px 10px !important; font-size: 0.75rem !important; }
            
            /* Global pushdown to prevent title overlapping the menu wrapper */
            header { top: 40px !important; }
            .hero { padding-top: 240px !important; }
            .page-container { padding-top: 240px !important; }
            .product-detail-container { padding-top: 240px !important; }
            .shop-container { padding-top: 240px !important; }
"""

for f in html_files:
    try:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            
        # 1. Update the photo crop on the main page
        if f == "index.html":
            content = content.replace('aspect-ratio: 1 / 1;', 'aspect-ratio: 4 / 3;') # Make it landscape
            # Clean up the previous mobile gap specifically since we overwrite
            content = content.replace('padding-top: 150px !important;', '') 
            
        # 2. Append overriding mobile CSS right before </style>
        if '/* Global pushdown' not in content:
            mobile_override = "\n        @media (max-width: 900px) {" + common_mobile_css + "\n        }\n"
            content = content.replace("</style>", mobile_override + "</style>")
            
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
            
    except Exception as e:
        print(f"Error on {f}: {e}")

print("Mobile optimizations applied seamlessly.")
