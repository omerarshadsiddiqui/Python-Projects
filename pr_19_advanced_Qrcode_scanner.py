import qrcode 
from PIL import Image

qr = qrcode.QRCode(version= 1, error_correction= qrcode.ERROR_CORRECT_H, box_size=12 ,border= 4)

qr.add_data("https://github.com/omerarshadsiddiqui")
qr.make(fit=True)

image = qr.make_image(fill_color="#DA70D6",back_colour="#E6E6FA")
image.save("omerGithub.png")