from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect


import feedparser as fp
import datetime as dt
from bs4 import BeautifulSoup


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
                description = BeautifulSoup(
                    entry.description, "html.parser").get_text()
                description = ' '.join(description.split()[:100]) + ' ...'
                article = Article(title=entry.title, url=entry.link,
                                  description=description,
                                  publication_date=dt.datetime(
                                      *entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M:%S'),
                                  feed=feed)
                article.save()
            return redirect('feeds_list')
    else:
        form = FeedForm()
    return render(request, 'news/new_feed.html', {'form': form})
