import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np



UPLOAD_FOLDER = 'C:/Users/ayool/Documents/GitHub/AI_Sudoku_Solver/uploads'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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


if __name__ == '__main__':
    app.run(debug=True)

