from django.contrib import admin
from .models import Page, Courusel

class AdminPage(admin.ModelAdmin):
    class Meta:
        model=Page
    prepopulated_fields = {'slug' : ('title',)}
    list_display =[
        'title',
        'status',
        'updated_at',
    ]

    list_filter = [
        'status',
    ]

    
        # list_editable [
        #     'status',
        #     'title',
        # ]
        
    


admin.site.register(Page,AdminPage)
admin.site.register(Courusel)