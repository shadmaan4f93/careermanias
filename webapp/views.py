from django.shortcuts import render

def index(request):
    context = {'data':"Success"}
    return render(request, 'home/home.html', context)

def about(request):
    context = {'data':"Success"}
    return render(request, 'home/about.html', context)

def listings(request):
    context = {'data':"Success"}
    return render(request, 'listings.html', context)

def coaching(request):
    return render(request, 'coaching.html', {})