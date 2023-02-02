
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.article_list, name='article_list'),


]
