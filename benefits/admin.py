from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Benefits


@admin.register(Benefits)
class BenefitsAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('title', 'content',)
