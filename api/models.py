from django.db import models

import datetime
from django.utils import timezone

import os

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    
    
    # is_anonymous = False

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200, default="")
    dob = models.DateField("Date Of Birth",blank=True, default=timezone.now)
    profileImg = models.ImageField(upload_to='frontend/src/assets/profileImgs/',blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    def was_published_recently(self):
        return self.createdAt >= timezone.now() - datetime.timedelta(days=1)

    def to_dict(self):
        return{
        "id": self.id,
        "username": self.username,
        "email": self.email,
        "dob": self.dob,
        "profileImg": os.path.basename(self.profileImg.name),
        "createdAt": self.createdAt,
        }


    # def blah():
    #     print("BLahh")


class Category(models.Model):
    category = models.CharField(max_length=200)
    categoryImg = models.ImageField(upload_to='frontend/src/assets/categoryImgs/')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
    
    def was_published_recently(self):
         return self.createdAt >= timezone.now() - datetime.timedelta(days=1)

    def to_dict(self):
         return{
         "id": self.id,
         "category": self.category,
         "categoryImg": os.path.basename(self.categoryImg.name),
         "createdAt": self.createdAt,
         }

class FavouriteCategory(models.Model):
    user_fk = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    category_fk = models.ForeignKey(
        "Category", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         user_name = self.user_fk.to_dict()["username"]
         category_name = self.category_fk.to_dict()["category"]
         return f"{user_name} - {category_name}"

    
    def was_published_recently(self):
        return self.createdAt >= timezone.now() - datetime.timedelta(days=1)

    def to_dict(self):
        return{
        "id": self.id,
        # "user_fk": self.user_fk.to_dict(),
        # "category_fk": self.category_fk.to_dict(),
        # "createdAt": self.createdAt,
        "category_fk": self.category_fk.id,
        "category": self.category_fk.category,
         "categoryImg": os.path.basename(self.category_fk.categoryImg.name),
         "createdAt": self.category_fk.createdAt,
        }

class Article(models.Model):
    category_fk = models.ForeignKey(
        "Category", on_delete=models.CASCADE)
    title = models.CharField( max_length=200)
    text = models.CharField(max_length=700)
    articleImg = models.ImageField(upload_to='frontend/src/assets/articleImgs/')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.createdAt >= timezone.now() - datetime.timedelta(days=1)

    def to_dict(self):
        return{
        "id": self.id,
        "title": self.title,
        "text": self.text,
        "articleImg": 'src/assets/articleImgs/'+os.path.basename(self.articleImg.name),
        # "articleImg": os.path.basename(self.articleImg.name),
        "createdAt": self.createdAt,
        "category": self.category_fk.to_dict(),
        }

class ArticleComment(models.Model):
    article_fk = models.ForeignKey(
        "Article", on_delete=models.CASCADE)
    user_fk = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    comment = models.CharField( max_length=400)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    def was_published_recently(self):
        return self.createdAt >= timezone.now() - datetime.timedelta(days=1)

    def to_dict(self):
        return{
        "id": self.id,
        "user_fk": self.user_fk.to_dict(),
        "article_fk": self.article_fk.to_dict(),
        "comment": self.comment,
        "createdAt": self.createdAt,
        }

class CommentReply(models.Model):
    comment_fk = models.ForeignKey(
        "ArticleComment", on_delete=models.CASCADE)
    user_fk = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    comment = models.CharField( max_length=400)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    def was_published_recently(self):
        return self.createdAt >= timezone.now() - datetime.timedelta(days=1)

    def to_dict(self):
        return{
        "id": self.id,
        "comment_fk": self.comment_fk.to_dict()['id'],
        "user_fk": self.user_fk.to_dict(),
        "comment": self.comment,
        "createdAt": self.createdAt,
        }
