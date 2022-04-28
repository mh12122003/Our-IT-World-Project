# ref: https://www.youtube.com/watch?v=5ud8Bfbo9vk
import qrcode

qr = qrcode.QRCODE(
    version=1,
    box_size=15,
    border=5
)

data = 'abcxyz.com'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color ='white')
img.save('myQR.png')
