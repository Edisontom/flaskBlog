from blog.config.config import IMAGE_EXTENSIONS, MUSIC_EXTENSIONS, UPLOAD_IMAGE, UPLOAD_MUSIC, IMG_WIDTH
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import PIL
import os


def allowed_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in IMAGE_EXTENSIONS

def allowed_music(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in MUSIC_EXTENSIONS



def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_image(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_IMAGE, filename))
            return redirect(url_for('show_entries'))
        elif file and allowed_image(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_MUSIC, filename))


            img = Image.open(os.path.join(UPLOAD_IMAGE, filename))
            if img.size[0] > IMG_WIDTH:
               ratio = (IMG_WIDTH / float(img.size[0]))
               height = int((float(img.size[1]) * float(ratio)))
               new_image = img.resize((IMG_WIDTH, height), PIL.Image.ANTIALIAS)
               new_image.save(os.path.join(UPLOAD_IMAGE, filename))
            return redirect(url_for('show_entries', filename=filename))
        return render_template('show_entries.html')

