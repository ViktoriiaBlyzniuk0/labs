import qrcode #створює кюар з тексту

def run():
    image = qrcode.make("Hello Python")
    image.save("qr.png")
    print("QR-код створено")