from PIL import Image #створення редагуання зображення

def run():
    image = Image.new("RGB", (100, 100), "blue")
    image.save("image.png")
    print("Зображення створено:", image.size)