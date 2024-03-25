from django.contrib import admin
from .models import Mainhp
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Mainhp)
class MainhpAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('title', 'quote', 'content',)