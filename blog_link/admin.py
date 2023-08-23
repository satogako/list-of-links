from django.contrib import admin
from .models import Resource
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Resource)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('condition', 'created_on', 'tags')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'condition', 'created_on', 'tag_list')
    search_fields = ['title', 'content']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


