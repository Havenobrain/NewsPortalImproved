from django.urls import path
from .views import (NewsList, NewsDetail, NewsSearchList, NewsCreate, NewsEdit,
                    NewsDelete, ArticleCreate, ArticleEdit, ArticleDelete, ProfileUserEdit)

urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:id>', NewsDetail.as_view(), name='news_detail'),
   path('search/', NewsSearchList.as_view(), name='news_search'),
   path('nw/create/', NewsCreate.as_view(), name='news_create'),
   path('nw/<int:pk>/edit/', NewsEdit.as_view(), name='news_update'),
   path('nw/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('ar/create/', ArticleCreate.as_view(), name='article_create'),
   path('ar/<int:pk>/edit/', ArticleEdit.as_view(), name='article_update'),
   path('ar/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('profile/<int:pk>/update/', ProfileUserEdit.as_view(), name='profile_user_update')
]