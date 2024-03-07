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
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts")
    image = CloudinaryField('image', default='placeholder')
    duration = models.TextField(blank=True)
    serves = models.IntegerField(choices=PEOPLE, default=0)
    source_of = models.TextField(blank=True)
    details = models.TextField()
    ingredients = models.TextField(blank=True)
    method = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    