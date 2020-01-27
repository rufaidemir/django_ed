from django.db import models
from page.models import STATUS, DEFAULT_STATUS

class Category(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(default='', max_length=175)
    status = models.TextField(choices=STATUS, default= DEFAULT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    content = models.TextField()
    slug = models.SlugField(default='', max_length=175)
    cover_image = models.ImageField(blank=True, upload_to='product')
    price = models.FloatField()
    stock = models.PositiveSmallIntegerField()
    status = models.TextField(choices=STATUS, default= DEFAULT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title