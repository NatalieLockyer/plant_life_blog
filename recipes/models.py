from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

import datetime

STATUS = ((0, "Draft"), (1, "Published"))
PEOPLE = ((0, "Serves 1"), (1, "Serves 2"), (2, "Serves 2 - 4"))

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts")
    image = CloudinaryField('image', default='placeholder')
    duration = models.TextField(max_length=20, default=False)
    serves = models.IntegerField(choices=PEOPLE, default=0)
    source_of = models.TextField(max_length=50, default=False)
    details = models.TextField()
    ingredients = models.TextField(max_length=300, default=False)
    method = models.TextField(max_length=500, default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(max_length=200, default=False)
    updated_on = models.DateTimeField(auto_now=True)
    