from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from . models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {
        'title': 'Blog Home',
        'heading': 'Welcome to Our Blog',
    }
    return render(request, 'index.html', context)

@login_required(login_url='user:login')
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {'articles': articles}
    return render(request, 'dashboard.html', context)

@login_required(login_url='user:login')
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    context = {'form': form}
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Article added successfully.')
        return redirect('article:dashboard')
    return render(request, 'addArticle.html', context)

def detail(request, id):
    #keyword = request.GET.get('keyword')
    #if keyword:
        #articles = Article.objects.filter(content__contains = keyword)
        
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    return render(request, 'detail.html', {'article': article})

@login_required(login_url='user:login')
def edit(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None,  instance=article)
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Article updated successfully.')
        return redirect('article:dashboard')
    
    context = {'form': form}
    return render(request, 'edit.html', context)

@login_required(login_url='user:login')
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.info(request, 'Article deleted successfully.')
    return redirect('article:dashboard')

def articles(request):
    keyword = request.GET.get('keyword')
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, 'articles.html', {'articles': articles})
    
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

@login_required(login_url='user:login')
def add_comment(request, id):
    articles = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        comment_name = request.user
        comment_content = request.POST.get('content')
        
        form = Comment(comment_name=comment_name, comment_content=comment_content)
        form.article = articles
        form.save()
        
    return redirect(reverse('article:detail', kwargs={'id': id}))
            