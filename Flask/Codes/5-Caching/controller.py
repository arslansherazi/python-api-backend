from flask import render_template, session, request
from werkzeug.utils import redirect

from app import app


# used to avoid saving of requested pages in cache.
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    return response


@app.route('/')
def index():
    if 'username' in session:
        return redirect('/welcome_page')
    return render_template('index.html')


@app.route('/welcome_page')
def welcome_page():
    if 'username' in session:
        username = session['username']
        return render_template('welcome_page.html', user=username)
    return redirect('/')


@app.route('/login_form', methods=['POST'])
def login_form():
    if not 'username' in session:
        session['username'] = request.form['username']
    return redirect('/welcome_page')


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect('/')