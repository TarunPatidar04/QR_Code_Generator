import qrcode 

from PIL import Image
import qrcode.constants


qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=4,border=2)

qr.add_data("https://github.com/TarunPatidar04")
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")
img.save("qrcode.png")