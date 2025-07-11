from django.shortcuts import render
# from models import Citata

def main(request):
    return render(request, 'main.html')

def top(request):
    return render(request, 'top.html')

