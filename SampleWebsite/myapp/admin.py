from django.contrib import admin
from .models import TodoItem,Product
# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Product)