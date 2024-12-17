from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def articleList(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articleList.html', {'artList':articles})

def articleDetails(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except:
        msg = 'You came here because you did not use the normal channel'
        msg += '<br>'
        msg += 'Slug "' + slug + '" does not exist; Try other name'
        return HttpResponse(msg)

    return render(request, 'articles/articleDetail.html', {'artDetail':article})
    #return HttpResponse(show)

# add a decorator to createArticle function (i.e. extends the function, add
# additional functionality to it without changing the function itself)
@login_required(login_url="/accounts/login/")
def createArticle(request):
    if request.method == 'POST':
        # validate the data received (request.POST) against the model form
        # CreateArticle; uploaded files do not go with POST object
        # it goes in a separate object called FILES
        articleForm = forms.CreateArticle(request.POST, request.FILES)
        if articleForm.is_valid():
            # save to DB
            # give me an instance of the form before saving to add user to it
            instance = articleForm.save(commit=False)
            instance.author = request.user
            instance.save()
            article = Article.objects.get(slug=instance.slug)
            return render(request, 'articles/articleDetail.html', {'artDetail': article})

    else: # it is a GET request
        articleForm = forms.CreateArticle()
    return render(request, 'articles/createArticle.html', {'form': articleForm})

def showMyArticles(request):
    found = True
    try:
        articles = Article.objects.filter(author=request.user)
        if len(articles) == 0:
            found = False
    except:
        msg = 'You have not used the normal channels to get here. Please review your practices'
        msg += '<br> Press BACK button and try again'
        return HttpResponse(msg)
    return render(request, 'articles/myArticles.html', {'myArticles': articles})
