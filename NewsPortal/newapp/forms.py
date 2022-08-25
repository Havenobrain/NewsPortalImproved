
from django import forms
from .models import Post
class NewsForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'author',
           'postCategory',
           'title',
           'text',
       ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'postCategory',
            'title',
            'text',
        ]