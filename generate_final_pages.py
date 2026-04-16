import os

banner_header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | J&D Peters</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;600&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <script src="https://www.paypalobjects.com/ncp/cart/cart.js" data-merchant-id="2Z48U82V2P5H2"></script>
    <style>
        :root {{
            --bg-base: #ece6d9; 
            --glass-bg: rgba(255, 255, 255, 0.45);
            --glass-border: rgba(255, 255, 255, 0.3);
            --accent-dark: #2d2a26;
            --text-main: #3d3a35;
            --blur-val: 18px;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }}

        body {{
            background-color: var(--bg-base);
            color: var(--text-main);
            line-height: 1.4;
            overflow-x: hidden;
        }}

        /* --- Tightened Header --- */
        header {{
            position: absolute;
            top: 15px; /* Compressed top margin */
            left: 0;
            width: 100%;
            z-index: 1000;
            padding: 0 5%;
        }}

        .glass-nav-wrapper {{
            background: var(--glass-bg);
            backdrop-filter: blur(var(--blur-val));
            -webkit-backdrop-filter: blur(var(--blur-val));
            border: 1px solid var(--glass-border);
            border-radius: 30px;
            padding: 15px 30px;
            max-width: 1000px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.04);
        }}

        .logo-container img {{
            height: 85px;
            display: block;
            margin-bottom: 10px;
        }}

        .nav-inner {{
            display: flex;
            align-items: center;
            gap: 25px;
            border-top: 1px solid rgba(0,0,0,0.06);
            padding-top: 10px;
            width: 100%;
            justify-content: center;
            flex-wrap: wrap;
        }}

        .nav-links {{
            display: flex;
            list-style: none;
            gap: 25px;
        }}

        .nav-links a {{
            text-decoration: none;
            color: var(--accent-dark);
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        /* Dropdown */
        .dropdown {{ position: relative; }}
        .dropdown-menu {{
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%) translateY(5px);
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 12px;
            list-style: none;
            padding: 8px 0;
            min-width: 140px;
            opacity: 0;
            visibility: hidden;
            transition: 0.2s;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        }}
        .dropdown:hover .dropdown-menu {{ opacity: 1; visibility: visible; transform: translateX(-50%) translateY(0); }}
        .dropdown-menu li a {{ padding: 8px 15px; display: block; text-transform: none; text-align: center; }}
        
        .cursive {{
            font-family: 'Dancing Script', cursive;
            color: #7d6e53;
            font-size: 1.3em;
            display: inline-block;
            transform: rotate(-2deg);
        }}

        /* --- Global Announcement Bar --- */
        .promo-banner {{
            background: #7d6e53;
            color: white;
            text-align: center;
            padding: 12px 20px;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            position: relative;
            z-index: 1100;
            width: 100%;
        }}

        .promo-banner span {{
            color: #ece6d9;
            font-weight: 400;
            margin-left: 10px;
        }}

        header {{
            top: 55px !important;
        }}

        /* Specific Page Styles */
        {custom_css}

        /* Mobile */
        @media (max-width: 900px) {{
            header {{ top: 55px !important; }}
            .nav-links {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; padding-top: 10px; }}
            .nav-links a {{ font-size: 0.65rem; }}
            .logo-container img {{ height: 70px; }}
        }}
    </style>
</head>
<body>
    <div class="promo-banner">
        SALE! 20% OFF ALL LUKE'S CHIPS — <span>FREE SHIPPING CANADA WIDE ONLY</span>
    </div>

    <header>
        <div class="glass-nav-wrapper">
            <div class="logo-container">
                <img src="logotransparent-2.webp" alt="J&D Peters Logo">
            </div>
            <nav class="nav-inner">
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="products.html">Products</a></li>
                    <li><a href="tallow-products.html">Tallow Products</a></li>
                    <li><a href="where-to-buy.html">Where to Buy</a></li>
                    <li class="dropdown"><a href="shop.html">Shop</a>
                        <ul class="dropdown-menu">
                            <li><a href="dill-pickle-chips.html">Dill Pickle</a></li>
                            <li><a href="kale-chips.html">Kale</a></li>
                            <li><a href="mexican-spice-chips.html">Mexican Spice</a></li>
                            <li><a href="multigrain-chips.html">Multigrain</a></li>
                            <li><a href="nacho-cheese-chips.html">Nacho Cheese</a></li>
                            <li><a href="sea-salt-chips.html">Sea Salt</a></li>
                            <li><a href="tallow-chips.html">Tallow</a></li>
                        </ul>
                    </li>
                    <li><a href="contact-us.html">Contact Us</a></li>
                </ul>
                <paypal-cart-button data-id="pp-view-cart"></paypal-cart-button>
                <script>
                    cartPaypal.Cart({{ id: "pp-view-cart" }})
                </script>
            </nav>
        </div>
    </header>

"""

footer = """
</body>
</html>
"""

# 1. products.html
products_css = """
        .page-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 220px 5% 80px;
            text-align: center;
        }

        .page-title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2.5rem, 5vw, 3.5rem);
            color: var(--accent-dark);
            margin-bottom: 20px;
        }
        
        .section-title {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: var(--accent-dark);
            margin: 60px 0 30px;
            text-align: left;
            border-bottom: 2px solid var(--glass-border);
            padding-bottom: 10px;
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 35px;
        }

        .product-card {
            background: var(--glass-bg);
            backdrop-filter: blur(var(--blur-val));
            -webkit-backdrop-filter: blur(var(--blur-val));
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            padding: 35px 25px;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            transition: transform 0.3s, box-shadow 0.3s;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
        }

        .product-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
        }

        .product-image {
            width: 100%;
            height: 220px;
            object-fit: contain;
            margin-bottom: 25px;
            transition: transform 0.4s ease;
            filter: drop-shadow(0 15px 25px rgba(0,0,0,0.15));
        }

        .product-card:hover .product-image {
            transform: scale(1.08) rotate(2deg);
        }

        .product-title {
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            font-size: 1.4rem;
            color: var(--accent-dark);
            margin-bottom: 15px;
            flex-grow: 1;
            display: flex;
            align-items: center;
            text-align: center;
            line-height: 1.3;
        }
        
        .store-notice {
            color: #7d6e53;
            font-size: 0.9rem;
            font-weight: 600;
            margin-top: auto;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .btn-details {
            margin-top: auto;
            background: var(--accent-dark);
            color: white;
            padding: 12px 30px;
            border-radius: 50px;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 600;
            transition: background 0.3s;
            border: none;
            cursor: pointer;
            width: 100%;
            max-width: 200px;
        }

        .btn-details:hover {
            background: #4a453f;
        }
"""

tortillas = [
    {"name": "Mexican Flour Tortillas", "img": "mexican.webp"},
    {"name": "Unbleached Flour Tortillas", "img": "unbleached.webp"},
    {"name": "Kamut Tortillas", "img": "kamut.webp"},
    {"name": "Spelt Tortillas", "img": "spelt.webp"},
    {"name": "Whole Wheat Tortillas", "img": "wholewheat.webp"},
    {"name": "Spinach Tortillas", "img": "spinach.webp"},
    {"name": "Tomato Basil Tortillas", "img": "tomato.webp"},
]

chips = [
    {"name": "Tallow Fried Tortilla Chips", "img": "tallow-chip.webp", "link": "tallow-chips.html"},
    {"name": "Sea Salt Tortilla Chips", "img": "sea-salt-chip.webp", "link": "sea-salt-chips.html"},
    {"name": "Mexican Spice Tortilla Chips", "img": "mexican-spice-chip.webp", "link": "mexican-spice-chips.html"},
    {"name": "Nacho Cheese Tortilla Chips", "img": "nachocheese.webp", "link": "nacho-cheese-chips.html"},
    {"name": "Dill Pickle Tortilla Chips", "img": "dillpickle.webp", "link": "dill-pickle-chips.html"},
    {"name": "Multigrain Tortilla Chips", "img": "multigrain.webp", "link": "multigrain-chips.html"},
    {"name": "Kale Tortilla Chips", "img": "kale.webp", "link": "kale-chips.html"},
]

products_html = banner_header.format(title="Products", custom_css=products_css) + """
    <section class="page-container">
        <h1 class="page-title">Our <span class="cursive">Products</span></h1>
        <p>Explore our complete line of heritage-quality baked goods. Freshly crafted, always authentic.</p>

        <h2 class="section-title">Tortillas</h2>
        <div class="product-grid">
"""

for t in tortillas:
    products_html += f"""
            <div class="product-card">
                <img src="{t['img']}" alt="{t['name']}" class="product-image">
                <h3 class="product-title">{t['name']}</h3>
                <span class="store-notice">Available in Stores Only</span>
            </div>
"""

products_html += """
        </div>
        
        <h2 class="section-title">Tortilla Chips</h2>
        <div class="product-grid">
"""

for c in chips:
    products_html += f"""
            <div class="product-card">
                <img src="{c['img']}" alt="{c['name']}" class="product-image">
                <h3 class="product-title">{c['name']}</h3>
                <a href="{c['link']}" class="btn-details">More Details</a>
            </div>
"""

products_html += """
        </div>
    </section>
""" + footer


# 2. tallow-products.html
tallow_css = products_css
tallow_html = banner_header.format(title="Tallow Products", custom_css=tallow_css) + """
    <section class="page-container">
        <h1 class="page-title">Our <span class="cursive">Tallow</span> Products</h1>
        <p>Delicious tortillas and chips masterfully crafted using premium beef tallow for an unmatched authentic flavor.</p>

        <div class="product-grid" style="margin-top: 50px;">
"""

tallow_html += f"""
            <div class="product-card">
                <img src="tallow-chip.webp" alt="Tallow Fried Tortilla Chips" class="product-image">
                <h3 class="product-title">Tallow Fried Tortilla Chips</h3>
                <a href="tallow-chips.html" class="btn-details">More Details</a>
            </div>
"""

tallow_html += """
        </div>
    </section>
""" + footer

# 3. contact-us.html
contact_css = """
        .contact-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 220px 5% 80px;
            text-align: center;
        }

        .contact-title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2.5rem, 5vw, 3.5rem);
            color: var(--accent-dark);
            margin-bottom: 20px;
        }
        
        .contact-box {
            background: var(--glass-bg);
            backdrop-filter: blur(var(--blur-val));
            -webkit-backdrop-filter: blur(var(--blur-val));
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            padding: 50px;
            margin-top: 40px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
            text-align: left;
        }
        
        .form-group {
            margin-bottom: 25px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: var(--accent-dark);
        }
        
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid rgba(0,0,0,0.1);
            background: rgba(255,255,255,0.7);
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            outline: none;
            transition: background 0.3s;
        }
        
        .form-group input:focus, .form-group textarea:focus {
            background: rgba(255,255,255,1);
            border-color: rgba(0,0,0,0.3);
        }
        
        .btn-submit {
            background: var(--accent-dark);
            color: white;
            padding: 15px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-size: 1rem;
            font-weight: 600;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
            width: 100%;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .btn-submit:hover {
            background: #4a453f;
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(45, 42, 38, 0.3);
        }
        
        .contact-info {
            margin-top: 40px;
            font-size: 1.1rem;
            color: var(--accent-dark);
            line-height: 1.8;
            text-align: center;
        }
"""

contact_html = banner_header.format(title="Contact Us", custom_css=contact_css) + """
    <section class="contact-container">
        <h1 class="contact-title">Get In <span class="cursive">Touch</span></h1>
        <p>We'd love to hear from you. Reach out with any questions, wholesale inquiries, or just to say hello!</p>

        <div class="contact-box">
            <form action="#" method="POST">
                <div class="form-group">
                    <label for="name">Full Name</label>
                    <input type="text" id="name" name="name" required placeholder="Jane Doe">
                </div>
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required placeholder="jane@example.com">
                </div>
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" rows="5" required placeholder="How can we help you?"></textarea>
                </div>
                <button type="submit" class="btn-submit">Send Message</button>
            </form>
        </div>
        
        <div class="contact-info">
            <p><strong>Email:</strong> info@jdpeters.com</p>
            <p>Made with love in Canada.</p>
        </div>
    </section>
""" + footer

with open("products.html", "w", encoding="utf-8") as f:
    f.write(products_html)

with open("tallow-products.html", "w", encoding="utf-8") as f:
    f.write(tallow_html)

with open("contact-us.html", "w", encoding="utf-8") as f:
    f.write(contact_html)

print("Pages created successfully.")
