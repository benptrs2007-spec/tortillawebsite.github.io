import re

with open("products.html", "r", encoding="utf-8") as f:
    content = f.read()

replacement = """Available in Stores Only</span>
                <details style="margin-top: 15px; text-align: center; width: 100%;">
                    <summary style="cursor:pointer; color:var(--accent-dark); font-weight:600; font-size: 0.9rem; text-decoration: underline;">More Details</summary>
                    <p style="margin-top:10px; font-size:0.85rem; color:var(--text-main); line-height: 1.4;">Refrigeration required. Discover the authentic heritage taste baked fresh daily using traditional methods.</p>
                </details>"""

content = content.replace("Available in Stores Only</span>", replacement)

with open("products.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("tallow-products.html", "r", encoding="utf-8") as f:
    t_content = f.read()

new_tallow_cards = """
            <div class="product-card">
                <img src="tallow-chip.webp" alt="Tallow Fried Tortilla Chips" class="product-image">
                <h3 class="product-title">Tallow Fried Tortilla Chips</h3>
                <a href="tallow-chips.html" class="btn-details">More Details</a>
            </div>

            <div class="product-card">
                <img src="kamut.webp" alt="Tallow Kamut Tortillas" class="product-image">
                <h3 class="product-title">Tallow Kamut Tortillas</h3>
                <span class="store-notice">Available in Stores Only</span>
            </div>

            <div class="product-card">
                <img src="unbleached.webp" alt="Tallow Unbleached Tortillas" class="product-image">
                <h3 class="product-title">Tallow Unbleached Tortillas</h3>
                <span class="store-notice">Available in Stores Only</span>
            </div>

            <div class="product-card">
                <img src="spelt.webp" alt="Tallow Spelt Tortillas" class="product-image">
                <h3 class="product-title">Tallow Spelt Tortillas</h3>
                <span class="store-notice">Available in Stores Only</span>
            </div>
"""

t_content = re.sub(
    r'(<div class="product-grid"[^>]*>)\s*<div class="product-card">.*?</div>\s*</div>',
    r'\1' + new_tallow_cards + '\n        </div>',
    t_content,
    flags=re.DOTALL
)

with open("tallow-products.html", "w", encoding="utf-8") as f:
    f.write(t_content)

print("Updates successful")
