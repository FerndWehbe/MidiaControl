from PIL import Image
import qrcode
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
s.getsockname()[0]
print(s.getsockname()[0])

#print(IP)