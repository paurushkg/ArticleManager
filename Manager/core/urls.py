from django.contrib import admin
from django.urls import path

from core.views import(
    article_list,
    article_detail,
    ArticleAPIView,
    ArticleDetail
)

urlpatterns = [
    path('article/', article_list),
    path('Carticle/', ArticleAPIView.as_view()),
    path('detail/<int:pk>', article_detail),
    path('Cdetail/<int:pk>', ArticleDetail.as_view()),
]