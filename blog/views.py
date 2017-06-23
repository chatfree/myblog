from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
#article list
def article_list(request):
    # article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    return render(request,'index.html',{"articles":articles})
    # return HttpResponse("hello word")
#article detail
def article_detail(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'article_detail.html',{"article":article})

def edit_article(request,article_id):
    if str(article_id) =='0':
        return render(request,'edit_article.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request,'edit_article.html',{"article":article})
#save saveArticle
def saveArticle(request):
    id = request.POST.get("id","")
    title = request.POST.get("title")
    content = request.POST.get("content")
    if str(id) != '':
        article = models.Article.objects.get(pk=id)
        article.title = title
        article.content = content
        article.save()
        return render(request,'edit_article.html',{"article":article})
    else:
        models.Article.objects.create(title=title,content=content)
        return HttpResponseRedirect('/blog/index/')
