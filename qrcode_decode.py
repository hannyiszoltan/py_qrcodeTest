from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Hannyis Zoltán/Desktop/python/qrcode_test/myqrcode.png')

result = decode(img)

print(result)