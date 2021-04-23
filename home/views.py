from django.shortcuts import render, redirect
from .models import News, Comment, Category
from django.contrib import messages


# Create your views here.

def home(request):
    news = News.objects.all()
    trendings = News.objects.filter(is_trending=True)
    categories = Category.objects.all()
    topviews = News.objects.all().exclude(views__lt=4)
    context = {
        'news': news,
        'trendings': trendings,
        'categories': categories,
        'topviews': topviews,
    }
    return render(request, 'index.html', context)

def category(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'category.html', context)

def about_us(request):

    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact.html')

def latest(request):
    news = News.objects.all();
    context = {
        'news': news,
    }
    return render(request, 'latest_news.html', context)

def blog_single(request, id):
    news = News.objects.get(pk=id)
    news.views += 1
    news.save()
    
    comments = Comment.objects.filter(post = news, is_parent=None)
    replies = Comment.objects.filter(post = news).exclude(is_parent=None)

    return render(request, 'details.html', {'news': news, 'comments': comments, 'replies':replies})

def handle_comment(request):
    if request.method == "POST":
        comment = request.POST.get('message') 
        user = request.user
        news_id = request.POST.get('news_id')
        news = News.objects.get(pk=news_id)
        parent_id = request.POST['parent_id']
        if parent_id == "":

            comment = Comment(comment_text=comment, author = user, post = news)
            comment.save()
            messages.success(request, "your comment has been posted successfully")
        else:
            parent= Comment.objects.get(pk=parent_id)
            comment = Comment(comment_text=comment, author = user, post = news, is_parent=parent)
            comment.save()
            messages.success(request, "your reply has been posted successfully")




        # return redirect("/")


    return redirect(f"/detail/{news.pk}")

