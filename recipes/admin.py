from django.contrib import admin
from .models import Post, Comment


"""
This will allow me to create, update 
& delete blog posts from the admin panel
"""
admin.site.register(Post)
admin.site.register(Comment)
