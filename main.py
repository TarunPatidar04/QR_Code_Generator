import qrcode as qr

img=qr.make("https://github.com/TarunPatidar04")
# print(img)
img.save("my_github.png")