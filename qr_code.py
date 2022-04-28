import qrcode

qr = qrcode.QRCOĐE(
    version=1,
    box_size=15,
    border=5
)

data = 'ouritword.github.io/group21/'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color ='white')
img.save('myQR.png')