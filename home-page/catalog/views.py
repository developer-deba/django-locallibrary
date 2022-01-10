from django.shortcuts import render

# Create your views here.
from .models import Book,Author,Genre,Bookinstance
def index(request):
    num_books = Book.objects.all().count()
    num_instances = Bookinstance.objects.all().count()
    num_instances_available = Bookinstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context={
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors
    }
    return render(request, 'index.html',context)
