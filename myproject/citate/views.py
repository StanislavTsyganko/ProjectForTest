from django.shortcuts import render, redirect
# from models import Citata
from . import forms

def work_with_citates(request):
    return render(request, 'work_with_citate.html')

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
    return render(request, 'top.html')

