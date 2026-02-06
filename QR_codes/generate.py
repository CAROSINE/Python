import qrcode

url = input("Enter the URl to generate QR code: ").strip() #strip for unnecessary spaces
file_path = "E:\\BitRox\\Python\\QR_codes\\qrcode.png" #file path to save the QR code image

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code was generated and saved at:", file_path)