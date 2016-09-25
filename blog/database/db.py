import sqlite3
from flask import g
from blog.config.config import DATABASE
from blog import app


def connect_db():
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    with app.app_context():
         db = get_db()
         with app.open_resource('database/schema.sql', mode='r') as f:
             db.cursor().executescript(f.read())
         db.commit()


init_db()



