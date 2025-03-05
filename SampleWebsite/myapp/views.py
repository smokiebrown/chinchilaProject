from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateNewList
from .models import TodoItem, Product
from django.conf import settings

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, "home.html",{"products": products,'MEDIA_URL': settings.MEDIA_URL})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TodoItem(title=n)
            t.save()

        return HttpResponseRedirect("/todos")
    else:
        form = CreateNewList()
    return  render(response, "create.html", {"form":form})

def add_products(response):
    isAdded = False
    if response.method == "POST":
        form = Product(response.POST)

        if form.is_valid():
            n = form.cleaned_data["productName"]
            d = form.cleaned_data["productDesc"]
            p = form.cleaned_data["productPrice"]
            i = form.cleaned_data["image"]
            product=Product(productName=n, productDesc=d, productPrice=p, productImage=i)
            product.save()
            isAdded=True
        return HttpResponseRedirect("/add_products")
    else:
        form = Product()
    return  render(response, "create.html", {"form":form, "isAdded":isAdded})

