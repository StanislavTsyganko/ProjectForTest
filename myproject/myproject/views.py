from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def add(request):
    return render(request, 'add.html')

def top(request):
    return render(request, 'top.html')