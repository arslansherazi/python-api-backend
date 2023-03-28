from django.shortcuts import render, redirect
from Coding.models import Book


def index(request):
    return render(request, "index.html", {})

def addBook(request):
    return render(request, "add_book.html", {})

def viewBooks(request):
    books = Book.objects.all()
    return render(request, "view_books.html", {"books" : books})

def addBookSuccess(request):
    return render(request, "add_book_success.html", {})

def updateBook(request):
    id = request.session['update_id']
    book = Book.objects.get(id = id)
    return render(request, "update_book.html", {"book" : book})

def addBookForm(request):
    id     = request.POST['id']
    name   = request.POST['name']
    author = request.POST['author']
    price  = request.POST['price']

    book = Book(id = id, name = name, author = author, price = price)
    book.save()
    return redirect("/coding/addBookSuccess")

def updateDelete(request):
    id = request.POST['id']
    if 'delete' in request.POST:
        book = Book.objects.get(id = id)
        book.delete()
        return redirect("/coding/viewBooks")
    else:
        request.session['update_id'] = id
        return redirect("/coding/updateBook")

def updateBookForm(request):
    id     = request.POST['id']
    name   = request.POST['name']
    author = request.POST['author']
    price  = request.POST['price']

    book = Book.objects.get(id = id)
    book.name = name
    book.author = author
    book.price = price
    book.save()

    return redirect("/coding/viewBooks")

        
    