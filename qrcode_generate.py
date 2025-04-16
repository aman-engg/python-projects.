
# 1.  pip install qrcode
# 2. pip install pillow

import qrcode
def qr_code(data):

 
 qr = qrcode.make(data)
 qr.save("linkedin_profile.png")

 print("QR code generated and saved as 'linkedin_profile.png'")

# calling function
qr_code("https://www.linkedin.com/in/aman-u-350a8a284/")




