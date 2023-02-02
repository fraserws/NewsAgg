
from django.urls import re_path, path, include
from . import views

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    re_path(r'^$', views.article_list, name='article_list'),


]
