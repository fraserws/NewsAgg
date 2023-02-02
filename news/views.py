from django.shortcuts import render


def article_list(request):
    return render(request, 'news/article_list.html', {})
