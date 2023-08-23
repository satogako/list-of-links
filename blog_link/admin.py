from django.contrib import admin
from .models import Resource
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Resource)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


