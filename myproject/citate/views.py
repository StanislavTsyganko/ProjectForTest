from django.shortcuts import render, redirect
from .models import Citata
from . import forms
import base64

def work_with_citates(request):
    return render(request, 'work_with_citate.html')

def all_citates(request):
    citates = Citata.objects.all().order_by('date')
    return render(request, 'all_citates.html', {'citates':citates})


def add_citate(request):
    if request.method == 'POST':
        form = forms.CreateCitate(request.POST, request=request)
        if form.is_valid():
            new_citate = form.save(commit=False)

            username = request.COOKIES.get('quote_user') or new_citate.user_name
            if username:
                username = base64.b64decode(username).decode('utf-8')
                new_citate.user_name = username
            else:
                username = new_citate.user_name or 'Анонимно'
                new_citate.user_name = username

            new_citate.save()
            response = redirect('citate:citates')
            if not request.COOKIES.get('quote_user') and username!='Анонимно':
                safe_username = base64.b64encode(username.encode('utf-8')).decode('ascii')
                response.set_cookie('quote_user', safe_username, path='/', max_age=365*24*60*60)
            return response
    else:
        form = forms.CreateCitate(request=request)
    return render(request, 'add.html', {'form': form})

def top_citate(request):
    citates_by_raiting = Citata.objects.all().order_by('-raiting')[:10]
    citates_by_views = Citata.objects.all().order_by('-views')[:10]
    return render(request, 'top.html', {'citates_by_raiting':citates_by_raiting, 'citates_by_views':citates_by_views})

def my_citates(request):
    username = request.COOKIES.get('quote_user')
    if not username:
        return redirect('citate:add')

    try:
        username = base64.b64decode(username).decode('utf-8')
    except:
        username = username
        
    citates = Citata.objects.filter(user_name=username).order_by('-id')
    return render(request, 'my_citates.html', {'citates': citates, 'username': username})


def logout_view(request):
    response = redirect('citate:citates')
    response.delete_cookie('quote_user')
    return response