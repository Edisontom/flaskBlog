from flask import abort, request, session, redirect, url_for, \
    render_template, flash
from blog.database.db import get_db
from blog.config.config import (PASSWORD, USERNAME )




def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            error = 'Invalid username '
        elif request.form['password'] != PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

def show_entries():
    db = get_db()
    cur = db.execute('select title, text, image, music from entries order by id desc')
    entries = [dict(title = row[0],text = row[1], image = row[2], music = row[3]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text, image, music) values (?, ?, ?, ?)',
               [request.form['title'], request.form['text'], request.form['image'], request.form['music']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
















