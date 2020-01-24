from django.db import models

DEFAULT_STATUS= 'draft'
STATUS = [
    ('draft','taslak'),
    ('published','yayinlandi'),
    ('deleted', 'silindi'),
]

class Page(models.Model):
    title = models.CharField(max_length = 75)
    content = models.TextField()
    slug = models.SlugField(default='', max_length=80)
    cover_image = models.ImageField(blank=True,upload_to='page')
    status = models.TextField(choices=STATUS, default= DEFAULT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Courusel(models.Model):
    title = models.CharField(max_length = 100, blank =True, null =True)
    cover_image = models.ImageField(blank=True,upload_to='couresel')
    status = models.TextField(choices=STATUS, default= DEFAULT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    
