from flask import Flask, request, render_template
from comands import dothis
from PIL import Image
import qrcode
import socket
import sys
import os

PORT_NUM = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()
url = f"http://{IP}:{PORT_NUM}"
qr = qrcode.make(url)
qr.save("login.png")
with Image.open("login.png") as img:
    img.show()
    os.remove("login.png")

if getattr(sys, "frozen", False):
    template_folder = os.path.join(sys._MEIPASS, "templates")
    static_folder = os.path.join(sys._MEIPASS, "static")
    app = Flask(
        __name__, template_folder=template_folder, static_folder=static_folder
    )
else:
    app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pressed")
def key_press():
    key = request.args.get("key", "None")
    return {"pressed": dothis(key)}


app.run(host="0.0.0.0", port=PORT_NUM)
