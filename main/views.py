from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from .forms import VisitorForm, ItemForm, ImgForm
from .models import Visitor, Item, CarouselImg
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def admin_i(request):
    if request.user.is_authenticated:
        pass
    else:
        raise Http404('Halaman tidak ditemukan')
    
    obj = Visitor.objects.all()
    context = {
        'obj':obj
    }
    return render(request, 'hidden/home.html', context)

def item_list(request):
    if request.user.is_authenticated:
        pass
    else:
        raise Http404('Halaman tidak ditemukan')
    
    obj = Item.objects.all()    
    context = {
        'obj':obj
    }
    return render(request, 'hidden/item_list.html', context)

def add_item(request):
    if request.user.is_authenticated:
        pass
    else:
        raise Http404('Halaman tidak ditemukan')
    
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        
    context = {
        'form':form
    }
    return render(request, 'hidden/add_item.html', context)

def delete_item(request, id):
    if request.user.is_authenticated:
        pass
    else:
        raise Http404('Halaman tidak ditemukan')
    obj = Item.objects.get(id=id)
    obj.delete()
    return redirect('item_list')

def delete_img(request, id):
    if request.user.is_authenticated:
        pass
    else:
        raise Http404('Halaman tidak ditemukan')
    img = CarouselImg.objects.get(id=id)
    img.delete()
    return redirect('img_list')

def img_list(request):
    if request.user.is_authenticated:
        pass
    else:
        raise Http404('Halaman tidak ditemukan')
    img = CarouselImg.objects.all()
    context = {
        'img':img
    }
    return render(request, 'hidden/img_list.html', context)

def add_img(request):
    if request.user.is_authenticated:
        pass
    else:
        raise Http404('Halaman tidak ditemukan')
    form = ImgForm()
    if request.method == 'POST':
        form = ImgForm(request.POST or None, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('img_list')
    else:
        form = ImgForm()
    context = {
        'form':form
    }
    return render(request, 'hidden/add_img.html', context)

def payment_p(request):
    return render(request, 'payment.html')

def home(request):
    item = Item.objects.all()
    img = CarouselImg.objects.all()
    form = VisitorForm()
    if request.method == 'POST':
        form = VisitorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('payment')
    context = {
        'form':form, 
        'item':item,
        'img':img
    }
    
    return render(request, 'home.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('item_list')
        else:
            messages.error(request, "Username Atau Password Salah")
    context = {}
    return render(request, 'hidden/login.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Berhasil')
    return redirect('home')