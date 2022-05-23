from django.urls import re_path,include
from . import views
from django.contrib import admin

urlpatterns=[
    re_path('^$',views.news_today,name='newsToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
]