from django.shortcuts import render

from .models import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    context = {
        "title": "Главная страница",
        "categories": categories,
        "articles": articles
    }

    return render(request, "blog/index.html", context)


def category_page_view(request, category_id):
    articles = Article.objects.filter(
        category=category_id
    ).order_by(
        '-created_at'
    )
    trends = Article.objects.all().order_by('-views')

    context = {
        "title": f"Категория: {Category.objects.get(id=category_id)}",
        'articles': articles,
        'trends': trends
    }

    return render(request, "blog/category_page.html", context)


def about_us_page_view(request):
    return render(request, "blog/about_us.html")


def our_team_page_view(request):
    return render(request, "blog/our_team.html")



def article_detail_page_view(request, article_id):
    article = Article.objects.get(id=article_id)
    last_articles = Article.objects.all().order_by('-created_at')[:3]

    context = {
        "title": f"Статья: {article.title}",
        "article": article,
        "last_articles": last_articles
    }

    return render(request, "blog/article_detail.html", context)
