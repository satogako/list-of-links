from django.contrib import admin
from .models import Resource, CommentResourse
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Resource)
class ResourceAdmin(SummernoteModelAdmin):
    '''
    The ResourceAdmin class registers the Resource model with the admin site.
    '''
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('condition', 'created_on', 'tags')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'created_on', 'tag_list', 'condition',)
    search_fields = ['title', 'content']
    actions = ['publish']

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def publish(self, request, queryset):
        queryset.update(condition=1)


@admin.register(CommentResourse)
class CommentResourseAdmin(admin.ModelAdmin):
    '''
    This admin class displays the comment model with filter and search options, 
    and an action to approve comments.
    '''
    list_display = ('name', 'comment_field', 'post', 'created_on', 'approved')
    list_filter = ('created_on', 'approved')
    search_fields = ('name', 'email', 'comment_field')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
