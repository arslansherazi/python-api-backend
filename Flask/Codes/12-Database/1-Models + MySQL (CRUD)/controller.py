from flask import render_template, request, session
from werkzeug.utils import redirect

from app import app, db
from models import *


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_book')
def add_book():
    return render_template('add_book.html')


@app.route('/view_books')
def view_books():
    books = Book.query.all()
    return render_template('view_books.html', books=books)


@app.route('/message')
def message():
    message = session['message']
    return render_template('message.html', message=message)


@app.route('/update_book')
def update_book():
    book_id = session['book_id']
    book = Book.query.get(book_id)
    return render_template('update_book.html', book=book)


@app.route('/add_book_form', methods=['POST'])
def add_book_form():
    code = request.form['code']
    name = request.form['name']
    author = request.form['author']
    price = request.form['price']
    availability = request.form['availability']

    book = Book(code=code, name=name, author=author, price=price, is_available=int(availability))
    try:
        db.session.add(book)
        db.session.commit()
        session['message'] = 'Book is added successfully'
        return redirect('/message')
    except Exception as e:
        session['message'] = str(e)
        return redirect('/message')


@app.route('/update_or_delete_book', methods=['POST'])
def update_or_delete_book():
    book_id = request.form['book_id']
    if 'delete' in request.form:
        try:
            book = Book.query.get(book_id)
            db.session.delete(book)
            db.session.commit()
            session['message'] = 'Book is deleted successfully'
            return redirect('/message')
        except Exception as e:
            session['message'] = str(e)
            return redirect('/message')
    else:
        session['book_id'] = book_id
        return redirect('/update_book')


@app.route('/update_book_form', methods=['POST'])
def update_book_form():
    book_id = request.form['book_id']
    name = request.form['name']
    author = request.form['author']
    price = request.form['price']
    availability = request.form['availability']

    try:
        book = Book.query.get(book_id)
        book.name = name
        book.author = author
        book.price = price
        book.is_available = int(availability)

        db.session.commit()
        session['message'] = 'Book is updated successfully'
        return redirect('/message')
    except Exception as e:
        session['message'] = str(e)
        return redirect('/message')
