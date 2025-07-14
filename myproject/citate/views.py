from django.shortcuts import render, redirect
from .models import Citata
from . import forms

def work_with_citates(request):
    return render(request, 'work_with_citate.html')

def all_citates(request):
    citates = Citata.objects.all().order_by('date')
    return render(request, 'all_citates.html', {'citates':citates})


def add_citate(request):
    if request.method == 'POST':
        form = forms.CreateCitate(request.POST)
        if form.is_valid():
            new_citate = form.save(commit=False)
            username = request.COOKIES.get('quote_user') or request.POST.get('user_name')
            new_citate.user_name = username
            new_citate.save()
            response = redirect('citate:citates')
            if not request.COOKIES.get('quote_user') and username!='Анонимно':
                response.set_cookie('quote_user', username, max_age=365*24*60*60)
            return response
    else:
        form = forms.CreateCitate()
    return render(request, 'add.html', {'form': form})

def top_citate(request):
    citates_by_raiting = Citata.objects.all().order_by('-raiting')[:10]
    citates_by_views = Citata.objects.all().order_by('-views')[:10]
    return render(request, 'top.html', {'citates_by_raiting':citates_by_raiting, 'citates_by_views':citates_by_views})

def my_citates(request):
    username = request.COOKIES.get('quote_user')
    if not username:
        return redirect('citate:add')
        
    citates = Citata.objects.filter(user_name=username).order_by('-id')
    return render(request, 'my_citates.html', {'citates': citates, 'username': username})

