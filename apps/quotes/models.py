from __future__ import unicode_literals
from ..login.models import *
from django.db import models

# Create your models here.
class Quote(models.Model):
    posted_by = models.ForeignKey(User, related_name= "user_posts")
    author = models.CharField(max_length=45)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name= "user_favorites")
    quote = models.ForeignKey(Quote, related_name = "quote_favorites")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
