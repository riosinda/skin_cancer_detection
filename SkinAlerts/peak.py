from flask import Flask, render_template, request, redirect
import keras
import cv2 as cv
import numpy as np
from werkzeug.utils import secure_filename
import os


model = keras.models.load_model('cnn2_MobileNet_700_black.h5')
print('Model loaded')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'D:/SkinAlertsDataset'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')

@app.route('/database')
def database():
    return render_template('database.html')

@app.route('/dataprivacy')
def dataprivacy():
    return render_template('dataprivacy.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/detection/sccbcc', methods=['GET', 'POST'])
def sccbcc(model=model):
    if request.method == "POST":
        image = request.files['file']

        if image.filename == '':
            print('No selected file')
            return redirect(request.url)
        
        filename = secure_filename(image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        img = cv.imread('D:/SkinAlertsDataset/' + filename)
        rimg1 = cv.resize(img, dsize=(150, 150), interpolation=cv.INTER_CUBIC)
        image = rimg1.astype('float32') / 255

        if round(model.predict(np.array([image]))[0][0]) == 1:
            print('bcc')
        else:
            print('scc')

        return render_template('sccbcc.html')
    return render_template('sccbcc.html')

@app.route('/detection/malben', methods=['GET', 'POST'])
def malben(model=model):
    if request.method == "POST":
        image = request.files['file']

        if image.filename == '':
            print('No selected file')
            return redirect(request.url)
        
        filename = secure_filename(image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        img = cv.imread('D:/SkinAlertsDataset/' + filename)
        rimg1 = cv.resize(img, dsize=(150, 150), interpolation=cv.INTER_CUBIC)
        image = rimg1.astype('float32') / 255

        if round(model.predict(np.array([image]))[0][0]) == 1:
            print('bcc')
        else:
            print('scc')

        return render_template('malben.html')
    return render_template('malben.html')

@app.route('/detection/melnomel', methods=['GET', 'POST'])
def melnomel(model=model):
    if request.method == "POST":
        image = request.files['file']

        if image.filename == '':
            print('No selected file')
            return redirect(request.url)
        
        filename = secure_filename(image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        img = cv.imread('D:/SkinAlertsDataset/' + filename)
        rimg1 = cv.resize(img, dsize=(150, 150), interpolation=cv.INTER_CUBIC)
        image = rimg1.astype('float32') / 255

        if round(model.predict(np.array([image]))[0][0]) == 1:
            print('bcc')
        else:
            print('scc')

        return render_template('melnomel.html')
    return render_template('melnomel.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)