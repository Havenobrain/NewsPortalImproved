from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from newapp.models import Author


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


#@login_required
#def upgrade_me(request):
#    user = request.user
#    authors_group = Group.objects.get(name='authors')
#    if not request.user.groups.filter(name='authors').exists():
#        authors_group.user_set.add(user)
#    return redirect('/news')

@login_required
def upgrade_me(request):
    user = request.user
    group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        group.user_set.add(user)
        if not hasattr(user, 'author'):
            Author.objects.create(
                authorUser=User.objects.get(pk=user.id)
            )
    return redirect('/news')