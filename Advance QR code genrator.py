import qrcode #importing functions
from PIL import Image

qr = qrcode.QRCode(version=1, #set your version
                error_correction=qrcode.ERROR_CORRECT_H, #set your correction level
                box_size=10,border=4) #set your box size and border specification
qr.add_data("https://pypi.org/project/image/") #set your link in the box for which you want to create qr code
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue") #set your color and background color for qr code
img.save("python_web.png") #give your name by which you want to save your qr

