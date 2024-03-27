from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Mainhp


@admin.register(Mainhp)
class MainhpAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('title', 'quote', 'content',)
