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

            new_citate.save()
            return redirect('citate:citates')
    else:
        form = forms.CreateCitate()
    return render(request, 'add.html', {'form': form})

def top_citate(request):
    citates_by_raiting = Citata.objects.all().order_by('-raiting')[:10]
    citates_by_views = Citata.objects.all().order_by('-views')[:10]
    return render(request, 'top.html', {'citates_by_raiting':citates_by_raiting, 'citates_by_views':citates_by_views})

