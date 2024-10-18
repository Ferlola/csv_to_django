from django.shortcuts import render
from .models import Books
from django.views import generic
from django.db.models import Q
import sqlite3
import pandas as pd


def index(request):
    total_books = Books.objects.count()
    if total_books == 0:
        con = sqlite3.connect('db.sqlite3')
        df = pd.read_csv('books.csv')
        books = pd.DataFrame(df) 
        books = books.dropna()
        books = books.reset_index(inplace=False)
        books = books.rename(columns={"price (including used books)": "used_books","level_0":"id"},inplace=False)
        books.to_sql('book_books',con, if_exists='replace', index = False)
    return render(request, 'index.html', {'total_books': total_books})

class BookView(generic.ListView):
    model = Books
    template_name = 'book.html'

class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'book_detail.html'

def search(request):
    if request.method == "POST":
        query_title = request.POST.get('title', None)
        query_author = request.POST.get('author', None)
        query_publisher = request.POST.get('publisher', None)
        price_min = request.POST.get('price_min', None)
        price_max = request.POST.get('price_max', None)
        if price_min and price_max:
            precios = Books.objects.filter( price__gte=price_min,price__lte = price_max)\
                .order_by('price')
            return render(request, 'search.html', {"precios":precios})
        if query_title:
            results = Books.objects.filter(title__contains=query_title )
            return render(request, 'search.html', {"results":results})
        if query_publisher:
            results = Books.objects.filter(publisher__contains=query_publisher )
            return render(request, 'search.html', {"results":results})
        if query_author:
            results = Books.objects.filter(author__contains=query_author )
            return render(request, 'search.html', {"results":results})
    return render(request, 'search.html')
            
