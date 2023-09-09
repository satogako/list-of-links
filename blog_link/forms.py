from .models import CommentResourse
from django import forms


class ResourseFormComment(forms.ModelForm):
    class Meta:
        model = CommentResourse
        fields = ('comment_field',)