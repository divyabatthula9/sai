from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def articles(request):
    return render(request,'articles.html')
def contact(request):
    return render(request,'contact.html')
def fullwidth(request):
    return render(request,'full-width.html')
def portfolio(request):
    return render(request,'portfolio.html')
