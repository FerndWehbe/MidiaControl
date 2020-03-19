from flask import Flask, render_template, request
from pyautogui import press, hotkey
from PIL import Image
import qrcode
import socket
import sys
import os

WINDOWSKEY = {
    'start':    'playpause',
    'next':     'nexttrack',
    'back':     'prevtrack',
    'volup':    'volumeup',
    'voldown':  'volumedown',
    'mute':     'volumemute',
}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
IP = s.getsockname()[0]
s.close()
PORT_NUM = 8080 

url = f'http://{IP}:{PORT_NUM}'
qr = qrcode.make(url)
qr.save('login.png')
print(url)
with Image.open('login.png') as img:
    img.show()
    os.remove('login.png')



def dothis(key):
    if key == "close":
        hotkey('alt', 'f4')
        return True
    try:
        press(WINDOWSKEY[key])
        return True
    except KeyError:
        print(key)
        return False
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/pressed')
def key_press():

    key = request.args.get('key', 'None')
    return {'pressed': dothis(key)}

app.run(host='0.0.0.0', debug=False, port=PORT_NUM)