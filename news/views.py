from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect


import feedparser as fp
import datetime as dt


def article_list(request):
    articles = Article.objects.all()
    rows = [articles[x:x+1] for x in range(0, len(articles), 1)]
    return render(request, 'news/articles_list.html', {'rows': rows})


def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feeds_list.html', {'feeds': feeds})


def new_feed(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            feedData = fp.parse(feed.url)
            feed.title = feedData.feed.title
            feed.save()
            for entry in feedData.entries:
                article = Article()
                article.title = entry.title
                article.url = entry.link
                article.description = entry.description
                d = dt.datetime(*entry.published_parsed[:6])
                article.publication_date = d.strftime('%Y-%m-%d %H:%M:%S')

                article.feed = feed

                article.save()
            return redirect('feeds_list')

    else:
        form = FeedForm()
    return render(request, 'news/new_feed.html', {'form': form})
