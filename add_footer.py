import glob
import os
import re

footer_html = """
    <footer>
        <div class="footer-content">
            <div class="footer-column">
                <img src="logotransparent-2.webp" alt="J&D Peters Logo" class="footer-logo">
                <p style="font-size: 0.9rem; line-height: 1.6;">Canada's original family-owned tortilla bakery. Crafting authentic, preservative-free tortillas and chips from our farm to your table.</p>
            </div>
            <div class="footer-column">
                <h3>Sitemap</h3>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="products.html">Products</a></li>
                    <li><a href="tallow-products.html">Tallow Products</a></li>
                    <li><a href="where-to-buy.html">Where to Buy</a></li>
                    <li><a href="shop.html">Shop</a></li>
                    <li><a href="contact-us.html">Contact Us</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Follow Us</h3>
                <p style="margin-bottom: 15px; font-size: 0.9rem;">@petersfamilyfarmbakery</p>
                <div class="social-links">
                    <a href="https://facebook.com/petersfamilyfarmbakery" target="_blank">Facebook</a><br>
                    <a href="https://instagram.com/petersfamilyfarmbakery" target="_blank">Instagram</a>
                </div>
            </div>
            <div class="footer-column">
                <h3>Contact</h3>
                <p style="margin-bottom: 10px; font-size: 0.9rem;"><strong>Email:</strong> info@tortillaking.ca</p>
                <p style="margin-bottom: 10px; font-size: 0.9rem;"><strong>Tel:</strong> 519-852-2324</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>Created & Designed by Benjamin Peters</p>
        </div>
    </footer>
"""

footer_css = """
        /* Footer Styles */
        footer {
            background: var(--glass-bg);
            backdrop-filter: blur(var(--blur-val));
            -webkit-backdrop-filter: blur(var(--blur-val));
            border-top: 1px solid var(--glass-border);
            padding: 80px 5% 40px;
            margin-top: 120px;
            color: var(--text-main);
            position: relative;
            z-index: 50;
        }
        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 50px;
        }
        .footer-column h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            color: var(--accent-dark);
            margin-bottom: 25px;
            letter-spacing: 0.5px;
        }
        .footer-column ul {
            list-style: none;
            padding: 0;
        }
        .footer-column ul li {
            margin-bottom: 12px;
        }
        .footer-column ul li a {
            text-decoration: none;
            color: var(--text-main);
            font-size: 0.95rem;
            transition: color 0.3s ease;
            opacity: 0.8;
        }
        .footer-column ul li a:hover {
            color: #7d6e53;
            opacity: 1;
        }
        .footer-logo {
            height: 70px;
            margin-bottom: 25px;
            display: block;
        }
        .social-links a {
            display: inline-block;
            margin-bottom: 10px;
            color: var(--accent-dark);
            font-size: 0.95rem;
            text-decoration: none;
            opacity: 0.8;
            transition: opacity 0.3s ease, color 0.3s ease;
        }
        .social-links a:hover {
            opacity: 1;
            color: #7d6e53;
        }
        .footer-bottom {
            text-align: center;
            margin-top: 60px;
            padding-top: 30px;
            border-top: 1px solid rgba(0,0,0,0.06);
            font-size: 0.8rem;
            color: #888;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        @media (max-width: 600px) {
            .footer-content {
                grid-template-columns: 1fr;
                text-align: center;
            }
            .footer-logo {
                margin: 0 auto 25px;
            }
            .footer-column h3 {
                margin-top: 20px;
            }
        }
"""

def add_footer():
    for fpath in glob.glob("*.html"):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Add CSS
        if "/* Footer Styles */" not in content:
            content = content.replace("</style>", footer_css + "\n    </style>")
        
        # Add HTML
        # Look for the start of the closing script tags or the end of the body
        if "<footer>" in content:
            # Replace existing footer
            content = re.sub(r'<footer>.*?</footer>', footer_html.strip(), content, flags=re.S)
        else:
            # We want it after all content sections but before the scripts
            if "<script>" in content:
                # Find the FIRST script tag after the content
                # Search for it starting from the end of the last section
                sections = content.split("</section>")
                if len(sections) > 1:
                    last_section_index = content.rfind("</section>") + 10
                    content = content[:last_section_index] + footer_html + content[last_section_index:]
                else:
                    content = content.replace("</body>", footer_html + "</body>")
            else:
                content = content.replace("</body>", footer_html + "</body>")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    add_footer()
    print("Footer added to all pages.")
