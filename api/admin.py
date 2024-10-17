from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(FavouriteCategory)
admin.site.register(Article)
admin.site.register(ArticleComment)
admin.site.register(CommentReply)