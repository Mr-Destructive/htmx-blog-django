import json
from django.shortcuts import render
from django.http import QueryDict
from .models import Article
from .forms import ArticleForm

def createArticle(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            article = form.save()
            return render(request, 'articles/detail.html', {'article': article})
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def listArticle(request):
    articles = Article.objects.filter(author=request.user.id)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/list.html', context)

def detailArticle(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def deleteArticle(request, pk):
    Article.objects.get(id=pk).delete()
    articles = Article.objects.filter(author=request.user)
    print(articles)
    context = {'article': articles}
    return render(request, "articles/list.html", context)

def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    print(request.method)
    if request.method == 'PUT':
        qd = QueryDict(request.body)
        form = ArticleForm(instance=article, data=qd)
        if form.is_valid():
            form.instance.author = request.user
            article = form.save()
            return render(request, 'articles/detail.html', {'article': article})
    form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
