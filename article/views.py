from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

def createArticle(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            article = form.save()
            print(article)
            return render(request, 'articles/detail.html', {'article': article})
            #return render()
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
