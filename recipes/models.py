from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

import datetime

STATUS = ((0, "Draft"), (1, "Published"))
PEOPLE = ((0, "Serves 1"), (1, "Serves 2"), (2, "Serves 2 - 4"), (3, "Serves 4 - 6"), (4, "Serves 8 - 12"))
CATEGORY = ((0, "Breakfast"), (1, "Dinner"), (2, "Desserts"), (3, "Drinks"))

# class Category(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post")
    featured_image = CloudinaryField('image', default='placeholder')
    category = models.IntegerField(choices=CATEGORY, default=0)
    duration = models.TextField(max_length=20,)
    serves = models.IntegerField(choices=PEOPLE, default=0)
    source_of = models.TextField(max_length=50,)
    details = models.TextField()
    ingredients = models.TextField(max_length=2000,)
    method = models.TextField(max_length=2000,)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders the recipes from newest to oldest creation time
        """
        ordering = ["created_on"]

    def __str__(self):
        return f" {self.title}"

class Comment(models.Model):
    """
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """
        Orders the comments from newest to oldest creation time
        """
        ordering = ["created_on"]

    def __str__(self):
        return f" Users comment: - {self.body} by {self.author}"
