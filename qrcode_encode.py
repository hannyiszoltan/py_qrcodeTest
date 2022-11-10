import qrcode

data = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'

#custom qrcode pattern
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/Hannyis Zoltán/Desktop/python/qrcode_test/hehe.png')