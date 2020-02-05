from flask import render_template, request

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form1')
def form1():
    return render_template('form1.html')


@app.route('/form2')
def form2():
    return render_template('form2.html')


@app.route('/form1_handling', methods=['POST'])
def form1_handling():
    # username = request.form['username']
    # password = request.form['password']
    return render_template('success1.html', data=request.form)


@app.route('/form2_handling', methods=['GET'])
def form2_handling():
    name = request.args['name']
    roll_no = request.args['roll_no']
    degree = request.args['degree']
    cgpa = request.args['cgpa']
    return render_template('success2.html', data=request.args)
