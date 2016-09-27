from flask import Flask

from blog.config.config import DATABASE, DEBUG, SECRET_KEY, USERNAME, PASSWORD, UPLOAD_MUSIC, UPLOAD_IMAGE

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(
    DATABASE=DATABASE,
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    USERNAME=USERNAME,
    PASSWORD=PASSWORD,
    UPLOAD_MUSIC=UPLOAD_MUSIC,
    UPLOAD_IMAGE=UPLOAD_IMAGE
)

from blog.view.view import (login, logout, add_entry, show_entries)
from blog.upload.upload import upload_file




app.add_url_rule('/', view_func=show_entries, methods=['GET'])
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/add', view_func=add_entry, methods=['POST'])
app.add_url_rule('/logout', view_func=logout, methods=['GET'])
app.add_url_rule('/upload_file', view_func=upload_file, methods=['GET', 'POST'])





