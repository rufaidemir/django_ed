from django.shortcuts import render
from .models import Courusel, Page
from .forms import CoruselCreateForm, PageCreateForm
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.text import slugify
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    context = dict()
    carusel_list = Courusel.objects.filter(status = 'published').exclude(cover_image='')
    context['carusel_list'] = carusel_list
    return render(request, 'home/index.html', context)

def corusel_create(request):
    context = dict()
    carousel_model = Courusel()
    form = CoruselCreateForm(request.POST, request.FILES)
    context['form']= form
    if form.is_valid():
        form.save()
        messages.success(request, 'Bur seyler eklendi ama ne bilmiyoruz')
        # redirect('carousel:corusel_create')
    return render(request, 'manage/caurousel_form.html', context)

def carousel_list(request):
    context = dict()
    carousel = Courusel.objects.all().order_by('-pk')
    context['carousel']= carousel
    return render(request, 'manage/carousel_index.html', context)

def carousel_update(request, pk):
    carousel_model = Courusel.objects.get(pk= pk)
    form = CoruselCreateForm(request.POST, request.FILES, instance=carousel_model)
    context= dict()
    context['form'] = form
    if form.is_valid:
        form.save()
        messages.success(request, 'Form Guncellendi')
        return redirect('carousel:corusel_index')
    return render(request, 'manage/caurousel_form.html', context)

def manage(request):
    context = dict()
    return render(request, 'manage/manage.html', context)

@staff_member_required
def page_list(request):
    context = dict()
    page = Page.objects.all().order_by('-pk')
    context['items']= page
    return render(request, 'manage/page_index.html', context)

def page_create(request):
    def get_unique_slug(slug):
        counter =0
        while Page.objects.filter(slug = slug).exists():
            counter += 1
            slug = '{}-{}'.format(slug, counter)
        return slug 
    context = dict()
    model = Page()
    form = PageCreateForm(request.POST, request.FILES, instance=model)
    context['form']= form
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.slug = get_unique_slug(slugify(new_form.title.replace('ı','i')))
        new_form.save()
        # messages.success(request, 'Bur seyler eklendi.')
        return redirect('carousel:page_list')
    
    return render(request, 'manage/caurousel_form.html', context)

def page_update(request, pk):
    def get_unique_slug(slug):
        counter =0
        while Page.objects.filter(slug = slug).exists():
            counter += 1
            slug = '{}-{}'.format(slug, counter)
        return slug
    page_model = Page.objects.get(pk=pk)
    form = PageCreateForm(request.POST or None, request.FILES or None, instance=page_model)
    context= dict()
    context['form'] = form
    if form.is_valid:
        new_form =form.save(commit= False)
        if new_form.slug=="":
            new_form.slug=get_unique_slug(new_form.title.replace('ı','i'))
        new_form.save()
        messages.success(request, 'Form Guncellendi')
        # return redirect('carousel:page_list')
    return render(request, 'manage/caurousel_form.html', context)

def page_delete(request, pk):
    page=Page.objects.get(pk=pk)
    page.status= "deleted"
    page.save()
    return redirect('carousel:page_list')