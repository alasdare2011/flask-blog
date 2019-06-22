#blog.py - controller

#imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3
from functools import wraps

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'Q;9y!^F*Fn<n$9Ne'

app = Flask(__name__)

# pull in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# determine who can access main page
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                request.form['password'] != app.config['PASSWORD']:
            error = ' Invalid Credentials. Please try again.'
            status_code = 401
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    
    return render_template("login.html", error=error), status_code

@app.route('/main')
@login_required
def main():
    return render_template("main.html")

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
