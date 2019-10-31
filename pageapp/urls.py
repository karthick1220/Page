# 
# from django.urls import path
# from . import views
# from django.shortcuts import render
# 
# urlpatterns = [
#     path('hello/',views.hello,name='hello'),
# ]


#whole
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^hello/', views.hello, name = 'hello'),
   url(r'^article/(\d+)/', views.viewArticle, name = 'article'),
   url(r'^articles/(\d{2})/(\d{4})', views.viewArticles, name = 'articles'),
]