from django.contrib import admin
from .models import Mainhp
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Mainhp)
class MainhpAdmin(SummernoteModelAdmin):

    summernote_fields = ('title', 'quote', 'content',)