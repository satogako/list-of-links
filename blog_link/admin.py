from django.contrib import admin
from .models import Resource, CommentResourse
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Resource)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('condition', 'created_on', 'tags')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'created_on', 'tag_list', 'condition',)
    search_fields = ['title', 'content']
    actions = ['publish']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def publish(self, request, queryset): #перевірити потім чи плтрібно буде request!!!
        queryset.update(condition=1)


@admin.register(CommentResourse)
class CommentResourse(admin.ModelAdmin):

    list_display = ('name', 'comment_field', 'post', 'created_on', 'approved')
    list_filter = ('created_on', 'approved' )
    search_fields = ('name', 'email', 'comment_field')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):  #перевірити потім чи плтрібно буде request!!!
        queryset.update(approved=True)
       


    


