from django import forms
from .models import Courusel, Page


class CoruselCreateForm(forms.ModelForm):
    class Meta:
        model=Courusel
        fields = ('title','cover_image')
    

class PageCreateForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'title',
            'content',
            'cover_image',
            'status',
        ]