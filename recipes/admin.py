from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    In the admin page
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.

    Summernote - Adds rich-text editing of content in admin
    """
    list_display = ('title', 'slug', 'status', 'category', 'created_on',)
    search_fields = ['title', 'details', ]
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('duration', 'source_of', 'details',
        'ingredients', 'method', 'excerpt',)

    """
    This will allow me to create, update
    & delete blog posts from the admin panel
    """
    admin.site.register(Comment)
