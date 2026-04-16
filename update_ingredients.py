import re

tortillas_data = {
    "Mexican Flour Tortillas": "<strong>Ingredients:</strong> Unbleached Enriched Flour, Water, Sunflower Oil, Vinegar, Salt, Baking Soda.<br><strong>Allergen:</strong> Wheat<br><em>NO PRESERVATIVES</em>",
    "Unbleached Flour Tortillas": "<strong>Ingredients:</strong> Certified Organic Unbleached Wheat Flour, Water, Sunflower Oil, Vinegar, Sea Salt, Baking Soda.<br><strong>Allergen:</strong> Wheat<br><em>NO PRESERVATIVES</em>",
    "Kamut Tortillas": "<strong>Ingredients:</strong> Organic Kamut Flour, Water, Sunflower Oil, Sea Salt, Vinegar, Baking Soda.<br><strong>Allergen:</strong> Wheat<br><em>NO PRESERVATIVES</em>",
    "Spelt Tortillas": "<strong>Ingredients:</strong> Organic Spelt Flour, Water, Sunflower Oil, Sea Salt, Vinegar, Baking Soda.<br><strong>Allergen:</strong> Wheat<br><em>NO PRESERVATIVES</em>",
    "Whole Wheat Tortillas": "<strong>Ingredients:</strong> Organic Stone Ground Wheat Flour, Water, Sunflower Oil, Sea Salt, Vinegar, Baking Soda.<br><strong>Allergen:</strong> Wheat<br><em>NO PRESERVATIVES</em>",
    "Spinach Tortillas": "<strong>Ingredients:</strong> Organic Unbleached Flour, Water, Sunflower Oil, Vinegar, Sea Salt, Spinach, Baking Soda, Parsley.<br><strong>Allergen:</strong> Wheat<br><em>NO PRESERVATIVES</em>",
    "Tomato Basil Tortillas": "<strong>Ingredients:</strong> Unbleached Flour*, Water, Sunflower Oil, Tomato Paste, (Tomatoes), Basil, Parsley *Organic<br><strong>Contains:</strong> Wheat<br><em>NO PRESERVATIVES</em>",
    # Tallow variations
    "Tallow Kamut Tortillas": "<strong>Ingredients:</strong> Organic Kamut Flour, Water, 100% Pure Beef Tallow, Sea Salt, Vinegar, Baking Soda.<br><strong>Allergen:</strong> Wheat<br><em>NO PRESERVATIVES</em>",
    "Tallow Unbleached Tortillas": "<strong>Ingredients:</strong> Certified Organic Unbleached Wheat Flour, Water, 100% Pure Beef Tallow, Vinegar, Sea Salt, Baking Soda.<br><strong>Allergen:</strong> Wheat<br><em>NO PRESERVATIVES</em>",
    "Tallow Spelt Tortillas": "<strong>Ingredients:</strong> Organic Spelt Flour, Water, 100% Pure Beef Tallow, Sea Salt, Vinegar, Baking Soda.<br><strong>Allergen:</strong> Wheat<br><em>NO PRESERVATIVES</em>"
}

chips_data = {
    "tallow-chips.html": "<strong>INGREDIENTS:</strong> ORGANICALLY GROWN STONE GROUND NON-GMO CORN, 100% PURE BEEF TALLOW, SEA SALT, CALCIUM HYDROXIDE.",
    "sea-salt-chips.html": "<strong>INGREDIENTS:</strong> STONE GROUND NON-GMO CORN, SUNFLOWER OIL, SEA SALT, CALCIUM HYDROXIDE.",
    "kale-chips.html": "<strong>INGREDIENTS:</strong> STONE GROUND NON-GMO CORN, KALE, SUNFLOWER OIL, SEA SALT, PARSLEY, CALCIUM HYDROXIDE.<br><strong>MAY CONTAIN:</strong> MILK",
    "multigrain-chips.html": "<strong>INGREDIENTS:</strong> STONE GROUND NON-GMO CORN, BUCKWHEAT FLOUR, OAT FLOUR, FLAX SEED, SUNFLOWER OIL, SEA SALT, CALCIUM HYDROXIDE.<br><strong>MAY CONTAIN:</strong> MILK",
    "mexican-spice-chips.html": "<strong>INGREDIENTS:</strong> STONE GROUND NON-GMO CORN, SUNFLOWER OIL, SEA SALT, HERBS & SPICES (INCLUDING JALAPENO PEPPERS, DEHYDRATED PARSLEY) DEHYDRATED VEGETABLES (GARLIC, ONION, RED & GREEN BELL PEPPER) DEXTROSE, YEAST EXTRACT, VEGETABLE OIL(CORN, SOY, CANOLA) SILICON DIOXIDE, CALCIUM HYDROXIDE.<br><strong>MAY CONTAIN:</strong> MILK",
    "nacho-cheese-chips.html": "<strong>INGREDIENTS:</strong> STONE-GROUND NON-GMO CORN, SUNFLOWER OIL, SEA SALT, CHEESE MIX (CHEDDAR.PARMESAN), DEXTROSE, SALT, CORN FLOUR. MODIFIED MILK INGREDIENTS, SPICES, ONION POWDER, TOMATO POWDER, GARLIC POWDER, CITRIC ACID, NATURAL FLAVORS, SILICON DIOXIDE, CANOLA OIL, CALCIUM HYDROXIDE.<br><strong>CONTAINS:</strong> MILK",
    "dill-pickle-chips.html": "<strong>INGREDIENTS:</strong> STONE GROUND NON-GMO CORN, SUNFLOWEROIL, DILL PICKLE SEASONING (MODIFIED MILK INGREDIENTS, SALT, SUGAR, SODIUM DIACETATE, YEAST EXTRACT, GARLIC POWDER, VINEGAR POWDER, SPICE EXTRACT, MALIC ACID, DISODIUM GUANYLATE AND DISODIUM INOSINATE, (SILICON DIOXIDE), CALCIUM HYDROXIDE.<br><strong>CONTAINS:</strong> MILK"
}

# 1. Update tortillas in products.html and tallow-products.html
for file_name in ["products.html", "tallow-products.html"]:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()

        def replacer(match):
            card_content = match.group(0)
            # Find the title to lookup ingredients
            title_match = re.search(r'<h3 class="product-title">(.*?)</h3>', card_content)
            if not title_match:
                return card_content
            
            title = title_match.group(1)
            
            # Use original ingredients if missing, though it's manually added via dict
            ingredient_html = tortillas_data.get(title, "")
            
            # If it has a <details> tag, replace its internal <p> contents.
            if '<details' in card_content:
                # Replace the generic <p> text completely with the new ingredients info
                new_p = f'<p style="margin-top:10px; font-size:0.85rem; color:var(--text-main); line-height: 1.5; text-align: left;">{ingredient_html}</p>'
                card_content = re.sub(r'<p style=".*?">.*?</p>', new_p, card_content, count=1, flags=re.DOTALL)
            else:
                # For `tallow-products.html` which might not have the `<details>` yet since I missed it:
                if 'Available in Stores Only</span>' in card_content:
                    replacement = f"""Available in Stores Only</span>
                <details style="margin-top: 15px; text-align: left; width: 100%;">
                    <summary style="cursor:pointer; color:var(--accent-dark); font-weight:600; font-size: 0.9rem; text-decoration: underline;">More Details</summary>
                    <p style="margin-top:10px; font-size:0.85rem; color:var(--text-main); line-height: 1.5;">{ingredient_html}</p>
                </details>"""
                    card_content = card_content.replace('Available in Stores Only</span>', replacement)

            return card_content

        # Match each product card
        updated_content = re.sub(r'<div class="product-card">.*?</div>(?=\s*(?:<div class="product-card">|</div))', replacer, content, flags=re.DOTALL)

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(updated_content)

    except FileNotFoundError:
        pass


# 2. Update the chips on their individual pages
for chip_file, ingredients in chips_data.items():
    try:
        with open(chip_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        ingredients_div = f"""
            <div class="ingredients-box" style="margin-top: 25px; padding-top: 20px; border-top: 1px solid var(--glass-border); text-align: left; font-size: 0.85rem; color: var(--accent-dark); line-height: 1.4;">
                <h4 style="margin-bottom: 8px; font-family: 'Inter', sans-serif;">Nutritional Info</h4>
                {ingredients}
            </div>
"""

        # Only insert once and place it precisely after the image tag in .product-image-wrapper
        if 'ingredients-box' not in content:
            content = re.sub(r'(<img src=".*?\.webp" alt=".*?">)', r'\1' + ingredients_div, content)

            with open(chip_file, "w", encoding="utf-8") as f:
                f.write(content)
    except FileNotFoundError:
        pass

print("Ingredients injected successfully!")
