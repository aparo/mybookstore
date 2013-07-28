from django.shortcuts import render
from django.http import Http404
from bookshop.models import Book

def index(request):
    context = {'books': Book.objects.all()}
    return render(request, 'shop/index.html', context)


def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404
    return render(request, 'shop/detail.html', {'book': book})

