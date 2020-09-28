from django.contrib import admin
from django.urls import path

from core.views import article_list

urlpatterns = [
    path('article/', article_list),
]