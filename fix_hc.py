import glob

files = glob.glob("*-chips.html") + ["variety-box.html"]
for f in files:
    try:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            
        content = content.replace("Handcrafted", "Crafted")
        content = content.replace("handcrafted", "crafted")
        
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
    except FileNotFoundError:
        pass

print("Updated chips descriptions.")
