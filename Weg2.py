import qrcode

#Funktion
def make_qr(filename,msg):
    img = qrcode.make(msg)
    img.save(filename)
    img.show()

#Link eingeben
make_qr("Laptop.png","https://www.youtube.com/watch?v=WLP_L7Mgz6M")