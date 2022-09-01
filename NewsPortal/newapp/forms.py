
from django import forms
from .models import Post, User
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

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
