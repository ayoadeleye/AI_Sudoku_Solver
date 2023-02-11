from flask import Flask, render_template, request, flash, redirect
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/ayool/Documents/GitHub/AI_Sudoku_Solver/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

app.config['SECRET_KEY'] = '9a716eae4129c7b4a79e69ae1bb5d7dc'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def upload_image():
    image = request.files["image"]
    if image.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print('save')
        image.save(full_path)

        flash('Image successfully uploaded and displayed')

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

