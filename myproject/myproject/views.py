import random
from django.shortcuts import render
from citate.models import Citata

def find_random_citate(citates):
    score = 0
    for citate in citates:
        score+=citate.weight
    index = random.randint(0,score)
    for citate in citates:
        if score-citate.weight>0:
            score-=citate
        else:
            return citate

def main(request):
    citates = Citata.objects.all()
    citate = find_random_citate(citates)
    return render(request, 'main.html', {'citate':citate})

def top(request):
    return render(request, 'top.html')

