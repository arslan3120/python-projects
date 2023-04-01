import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create('Hello muhammad arslan')
qr.png('a.png',scale=8)