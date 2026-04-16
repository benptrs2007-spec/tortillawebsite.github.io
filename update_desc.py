import re

descriptions = {
    "dill-pickle-chips.html": "Experience the unmistakable crunch and quality of J&D Peters Dill Pickle Tortilla Chips. Handcrafted with our signature blend of tangy dill and savoury spices, these chips deliver a mouth-watering zing perfectly balanced by authentic stone-ground corn. No artificial flavors, just simple, recognizable ingredients.",
    "sea-salt-chips.html": "Experience the unmistakable crunch and quality of J&D Peters Sea Salt Tortilla Chips. Perfectly seasoned with coarse sea salt, these classic chips let the rich, authentic flavor of our locally-grown, stone-ground corn shine through every bite. No artificial flavors, just simple, recognizable ingredients.",
    "kale-chips.html": "Experience the unmistakable crunch and quality of J&D Peters Kale Tortilla Chips. Blended seamlessly with real kale, these authentic chips offer a vibrant, earthy flavor profile without sacrificing the hearty heritage-quality crunch. No artificial flavors, just simple, recognizable ingredients.",
    "multigrain-chips.html": "Experience the unmistakable crunch and quality of J&D Peters Multigrain Tortilla Chips. Crafted from a wholesome blend of buckwheat, oat, and flax seed alongside our traditional stone-ground corn, these artisan chips boast a deep, robust crunch. No artificial flavors, just simple, recognizable ingredients.",
    "mexican-spice-chips.html": "Experience the unmistakable crunch and quality of J&D Peters Mexican Spice Tortilla Chips. Handcrafted with a fiery, authentic blend of jalapeño peppers, garlic, and bold spices, these chips bring the heat and authentic heritage taste straight to your tastebuds. No artificial flavors, just simple, recognizable ingredients.",
    "nacho-cheese-chips.html": "Experience the unmistakable crunch and quality of J&D Peters Nacho Cheese Tortilla Chips. Generously dusted with a rich, savory blend of real cheddar and parmesan cheeses, these chips provide an authentic explosion of flavor you won't find anywhere else. No artificial flavors, just simple, recognizable ingredients.",
    "variety-box.html": "Experience the unmistakable crunch and quality of J&D Peters Variety Chip Box. Handcrafted with care from our family to yours, this ultimate collection lets you sample our most popular artisan flavors. Enjoy heritage-quality taste you won't find anywhere else, made with simple, recognizable ingredients."
}

for fname, new_desc in descriptions.items():
    try:
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace the description paragraph text
        content = re.sub(r'(<p class="description">).*?(</p>)', rf'\g<1>{new_desc}\g<2>', content)

        with open(fname, "w", encoding="utf-8") as f:
            f.write(content)
    except FileNotFoundError:
        pass

print("Descriptions successfully updated")
