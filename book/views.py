from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def detail(req):
    books = Book.objects.all()
    print(books)
    return render(req, 'book/index.html', {'books' : books})

def getData(req, prkey):
    book = Book.objects.get(pk = prkey)
    return render(req, 'book/item.html', {'book' : book})
