import qrcode

url = "https://www.instagram.com/gdscvitchennai"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("redirect_qrcode.png")
print(dir("redirect_qrcode.png"))