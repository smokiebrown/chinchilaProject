from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateNewList,Products
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

def add_products(request):
    isAdded = False
    if request.method == "POST":
        form = Products(request.POST, request.FILES)
        if form.is_valid():
            n = form.cleaned_data["productName"]
            d = form.cleaned_data["productDesc"]
            p = form.cleaned_data["productPrice"]
            i = form.cleaned_data["productImage"]
            product=Product(productName=n,productDesc=d,productPrice=p,productImage=i)
            product.save()
            return HttpResponseRedirect("/")
        else:
            print(form.errors)
    else:
        form = Products()
    return  render(request, "add_products.html", {"form":form, "isAdded":isAdded})

