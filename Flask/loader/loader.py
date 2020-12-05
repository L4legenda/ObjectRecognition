import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import Tensorflow.model

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'tiff', 'jp2', 'raw']

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'images'

@app.route('/')
def index():
    return render_template('tet_manager.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#chit
@app.route('/', methods=['POST'])
def upload_file():
    if 'img' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['img']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(filename)
        file.save("upload/" + filename)

        answer = Tensorflow.model.recognition(filename)

        return render_template('tet_manager.html', answer=answer)
    return render_template('tet_manager.html')


if __name__ == "__main__":
    app.run(debug=True)