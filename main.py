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

        cv_image = cv2.imread(full_path)
        # Perform the image processing operations
        gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        _, threshold_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
        edge_image = cv2.Canny(gray_image, 50, 150)

        # Save the processed image to disk
        processed_filename = os.path.splitext(filename)[0] + "_processed.jpg"
        processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
        cv2.imwrite(processed_path, edge_image)

    return render_template("index.html")
Note that I also used os.path.splitex


if __name__ == '__main__':
    app.run(debug=True)

