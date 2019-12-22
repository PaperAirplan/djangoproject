from django.shortcuts import render
from .models import Booklist
from django.http import HttpResponseRedirect
from .forms import AddForm


def book_list(request):
    books_view = Booklist.objects.all()
    return render(request, 'mybooks/mainpage.html', {'books': books_view})


def add_book(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/OK!/')
    else:
        form = AddForm()
    return render(request, {'form': form})
