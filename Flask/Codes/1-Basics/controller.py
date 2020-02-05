from flask import render_template

from app import app


@app.route('/')
def index():
    name = 'Arslan Haider Sherazi'
    cgpa = 3.42
    array = [1, 2, 3, 4, 5]
    return render_template('index.html', data={'name': name, 'cgpa': cgpa, 'array': array})
