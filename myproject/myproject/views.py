from django.shortcuts import render
from citate.models import Citata

def find_random_citate(citates):
    score = 0
    for citate in citates:
        score+=citate.weight
    math.rand()

def main(request):
    citates = Citata.objects.all()
    return render(request, 'main.html', {'citates':citates})

def top(request):
    return render(request, 'top.html')

