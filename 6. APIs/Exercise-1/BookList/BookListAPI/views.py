from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Book

# Create your views here.
def Books(request):
    if request.method == "GET":
        books = Book.objects.all().values()
        return JsonResponse({"books": list(books)})
    
    elif request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        price = request.POST.get("price")

        book = Book(title=title, author=author, price=price).save()

        return JsonResponse(model_to_dict(book), status=201)