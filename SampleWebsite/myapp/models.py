from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    productName = models.CharField(max_length=200)
    productDesc = models.TextField()
    productPrice = models.DecimalField(max_digits=10,decimal_places=2)
    productImage = models.ImageField(null=True,blank=True,upload_to='product_images/')

    def __str__(self):
        return self.productName
    