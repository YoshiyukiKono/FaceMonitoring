from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np
import cv2
from image_process import canny, face
from datetime import datetime
import os
import string
import random

import base64
from io import BytesIO

# pip install pillow
from PIL import Image


SAVE_DIR = "./images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

app = Flask(__name__, static_url_path="")

def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

def load_image():
    #filename = "./images/test.png"
    filename = "./images/download.jpg"
    img = cv2.imread(filename)
    new_img = face(img)
    #new_img = img
    new_img = new_img[:, :, ::-1]
    #pil_img = Image.fromarray(np.uint8(new_img))
    pil_img = Image.fromarray(new_img)
    binary = BytesIO()
    pil_img.save(binary,"JPEG")
    #with open(filename, 'rb') as f:
    #    binary = f.read()
    #pil_img.save(buf,format="png")
    #b64str = base64.b64encode(buf.getvalue()).decode("utf-8")

    #img_binarystream = io.BytesIO(img_binary)
    #img_pil = Image.open(img_binarystream)
    #img_numpy = np.asarray(img_pil)

    b64str = base64.b64encode(binary.getvalue()).decode("utf-8")
    b64data = "data:image/jpg;base64,{}".format(b64str)
    return b64data

@app.route('/')
def index():
    return render_template('index.html', images=os.listdir(SAVE_DIR)[::-1], b64img=load_image())

@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory(SAVE_DIR, path)

@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:
        stream = request.files['image'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        img = canny(img)

        dt_now = datetime.now().strftime("%Y_%m_%d%_H_%M_%S_") + random_str(5)
        save_path = os.path.join(SAVE_DIR, dt_now + ".png")
        cv2.imwrite(save_path, img)

        print("save", save_path)

        return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
