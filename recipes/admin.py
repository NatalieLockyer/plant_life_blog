from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    In the admin page 
    - Organises the posts by the list display
    - Allows for the posts to be filtered by status - draft or published.
    """
    list_display = ('title', 'slug', 'status', 'category', 'created_on',)
    search_fields = ['title', 'details', 'category']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('duration', 'source_of', 'details', 'ingredients', 'method', 'excerpt',)

"""
This will allow me to create, update 
& delete blog posts from the admin panel
"""
admin.site.register(Comment)
