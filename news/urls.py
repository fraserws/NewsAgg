
from django.urls import re_path, path, include
from . import views

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    re_path(r'^$', views.article_list, name='articles_list'),
    re_path(r'^feeds/new', views.new_feed, name='feed_new'),
    re_path(r'^feeds/', views.feeds_list, name='feeds_list'),


]
