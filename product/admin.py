from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model=Category
    prepopulated_fields = {'slug' : ('title',)}
    list_display =[
        'title',
        'gender',
        'status',
        'updated_at',
    ]
    list_filter = [
        'title',
    ]


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model=Product

    prepopulated_fields = {'slug' : ('title',)}
    list_display =[
        'category',
        'title',
        'content',
        'cover_image',
        'stock',
        'status',
        'updated_at',
        'price',
    ]
    list_filter = [
        'category',
        'title',
        'status',
    ]






admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)