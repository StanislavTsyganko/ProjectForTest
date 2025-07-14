from django.shortcuts import render, redirect
from .models import Citata
from . import forms
import base64
import logging

def work_with_citates(request):
    return render(request, 'work_with_citate.html')

def all_citates(request):
    citates = Citata.objects.all().order_by('date')
    return render(request, 'all_citates.html', {'citates':citates})

logger = logging.getLogger(__name__)

def add_citate(request):
    if request.method == 'POST':
        form = forms.CreateCitate(request.POST, request=request)
        if form.is_valid():
            try:
                new_citate = form.save(commit=False)
                
                if request.COOKIES.get('quote_user'):
                    try:
                        username = base64.b64decode(request.COOKIES['quote_user']).decode('utf-8')
                    except Exception as e:
                        logger.error(f"Error decoding cookie: {e}")
                        username = 'Анонимно'
                    new_citate.user_name = username
                else:
                    username = (form.cleaned_data.get('user_name') or 'Анонимно').strip()
                    new_citate.user_name = username
                
                new_citate.save()
                response = redirect('citate:citates')
                
                if not request.COOKIES.get('quote_user') and username != 'Анонимно':
                    safe_username = base64.b64encode(username.encode('utf-8')).decode('ascii')
                    response.set_cookie('quote_user', safe_username, max_age=365*24*60*60)
                return response
            except Exception as e:
                logger.exception("Error saving citation")
                form.add_error(None, f"Ошибка при сохранении: {e}")
        return render(request, 'add.html', {'form': form})
    
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