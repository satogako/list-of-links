from .models import CommentResourse
from django import forms


class ResourseFormComment(forms.ModelForm):
    '''
    Class creates a form for adding comments to resources 
    based on the CommentResourse model.
    '''
    class Meta:
        model = CommentResourse
        fields = ('comment_field',)
