from django.contrib import admin
from .models import Benefits
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Benefits)
class BenefitsAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('title', 'content',)
