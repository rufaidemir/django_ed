from django.shortcuts import render
from .models import Courusel
def index(request):
    context = dict()
    carusel_list = Courusel.objects.all()
    context['carusel_list'] = carusel_list
    return render(request, 'home/index.html', context)

