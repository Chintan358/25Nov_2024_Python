import pyqrcode

data = "Harsh Chuhan"

qr=pyqrcode.create(data)

qr.png('tops.png')
