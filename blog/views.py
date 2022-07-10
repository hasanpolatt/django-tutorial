from django.shortcuts import render
from models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def single(request):
    single = Article.objects.get(id=id)
    return render(request, 'single.html', {'single': single})
