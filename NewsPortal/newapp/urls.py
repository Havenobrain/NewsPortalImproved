from django.urls import path
from .views import (NewsList, NewsDetail, NewsSearchList, NewsCreate, NewsEdit,
                    NewsDelete, ArticleCreate, ArticleEdit, ArticleDelete, ProfileUserEdit, add_subscribe, delete_subscribe)
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', cache_page(60)(NewsList.as_view()), name='news_list'),
   path('<int:id>', cache_page(60*5)(NewsDetail.as_view()), name='news_detail'),
   path('search/', NewsSearchList.as_view(), name='news_search'),
   path('nw/create/', NewsCreate.as_view(), name='news_create'),
   path('nw/<int:pk>/edit/', NewsEdit.as_view(), name='news_update'),
   path('nw/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('ar/create/', ArticleCreate.as_view(), name='article_create'),
   path('ar/<int:pk>/edit/', ArticleEdit.as_view(), name='article_update'),
   path('ar/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('profile/<int:pk>/update/', ProfileUserEdit.as_view(), name='profile_user_update'),
   path('add_subscribe/<int:pk>/', add_subscribe, name='add_subscribe'),
   path('delete_subscribe/<int:pk>/', delete_subscribe, name='delete_subscribe'),
]