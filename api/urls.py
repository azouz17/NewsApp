"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

from .views import *

urlpatterns = [
    path('', logIn),
    path('main_spa/', main_spa, name='main_spa'),
    path('logout', logout),
    path('signup', addUser),
    path('login', logIn),
    path('users/<int:user_id>', getUsers, name='Users'),
    path('articles', getArticles, name='Get Articles'),
    path('addUser', addUser, name='Add User'),
    path('deleteUser', deleteUser, name='Delete User'),
    path('editUser', editUser, name='Edit User'),
    path('uploadProfileImg/<int:id>', uploadProfileImg, name='Upload User Profile Pic'),
    path('categories', getCategories, name='Categories'),
    path('addCategory', addCategory, name='Add Category'),
    path('deleteCategory', deleteCategory, name='Delete Category'),
    path('editCategory', editCategory, name='Edit Category'),
    path('addFavouriteCategory', addFavouriteCategory, name='Add Favourite Category'),
    path('removeFavouriteCategory', removeFavouriteCategory, name='Remove Favourite Category'),
    path('favoriteCategory/<int:id>', getFavouriteCategories, name='Favorite Category'),
    path('comments/<int:article_id>', getArticleComments, name='Comments'),
    path('editComment', editArticleComment, name='Edit Comment'),
    path('commentReplies/<int:comment_id>', getCommentReplys, name='Comment Replies'),
    path('addArticleComment/', addArticleComment, name='Add Comment'),
    path('addCommentReply/', addCommentReply, name='Add Comment Reply'),
    path('removeArticleComment/<int:comment_id>/<int:article_id>', deleteArticleComment, name='Remove comment'),
    path('getFavouriteArticles/<int:id>', getFavoriteArticles, name='Get Favorite Articles'),
]
