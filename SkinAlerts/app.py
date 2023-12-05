#app.py
#app.py
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import keras
import cv2 as cv
import numpy as np
import os
import csv


model = keras.models.load_model('cnn2_MobileNet_700_black.h5')
print('Model loaded')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'D:/SkinAlertsDataset/'
app.config['SECRET_KEY'] = 'UAZUDEM$2023'

def save_to_csv(data):
    csv_file = 'data.csv'
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, 'a', newline='') as file:
        fieldnames = ['date', 'age', 'anatom_site', 'country', 'ethnic_group', 'gender', 'result']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

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
        date = request.form['date']
        age = int(request.form['age'])
        anatom_site = request.form['anatom_site']
        country = request.form['country']
        ethnic_group = request.form['ethnic_group']
        gender = request.form['gender']
        image = request.files['file']

        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        img = cv.imread(image_path)
        rimg1 = cv.resize(img, dsize=(150, 150), interpolation=cv.INTER_CUBIC)
        image_array = rimg1.astype('float32') / 255

        if round(model.predict(np.array([image_array]))[0][0]) == 1:
            result = 'bcc'
        else:
            result = 'scc'
        
        print(result)
        data = {
            'date': date,
            'age': age,
            'anatom_site': anatom_site,
            'country': country,
            'ethnic_group': ethnic_group,
            'gender': gender,
            'result': result
        }

        save_to_csv(data)

        return render_template('sccbcc.html')
    return render_template('sccbcc.html')

@app.route('/detection/malben', methods=['GET', 'POST'])
def malben(model=model):
    if request.method == "POST":
        date = request.form['date']
        age = int(request.form['age'])
        anatom_site = request.form['anatom_site']
        country = request.form['country']
        ethnic_group = request.form['ethnic_group']
        gender = request.form['gender']
        image = request.files['file']

        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        img = cv.imread(image_path)
        rimg1 = cv.resize(img, dsize=(150, 150), interpolation=cv.INTER_CUBIC)
        image_array = rimg1.astype('float32') / 255

        if round(model.predict(np.array([image_array]))[0][0]) == 1:
            result = 'bcc'
        else:
            result = 'scc'
        
        print(result)
        data = {
            'date': date,
            'age': age,
            'anatom_site': anatom_site,
            'country': country,
            'ethnic_group': ethnic_group,
            'gender': gender,
            'result': result
        }

        save_to_csv(data)

        return render_template('malben.html')
    return render_template('malben.html')

@app.route('/detection/melnomel', methods=['GET', 'POST'])
def melnomel(model=model):
    if request.method == "POST":
        date = request.form['date']
        age = int(request.form['age'])
        anatom_site = request.form['anatom_site']
        country = request.form['country']
        ethnic_group = request.form['ethnic_group']
        gender = request.form['gender']
        image = request.files['file']

        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        img = cv.imread(image_path)
        rimg1 = cv.resize(img, dsize=(150, 150), interpolation=cv.INTER_CUBIC)
        image_array = rimg1.astype('float32') / 255

        if round(model.predict(np.array([image_array]))[0][0]) == 1:
            result = 'bcc'
        else:
            result = 'scc'
        
        print(result)
        data = {
            'date': date,
            'age': age,
            'anatom_site': anatom_site,
            'country': country,
            'ethnic_group': ethnic_group,
            'gender': gender,
            'result': result
        }

        save_to_csv(data)

        return render_template('melnomel.html')
    return render_template('melnomel.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)