from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

  #  def get(self, request, *args, **kwargs):
  #      return render(request, 'sign_up.html', {})
#
    #def post(self, request, *args, **kwargs):
       # welcome_letter = BaseRegisterForm(
            #email=request.POST['email'],
           # first_name=request.POST['Имя'],
          #  last_name=request.POST['Фамилия'],
         #   message=request.POST['message'],
        #)
        #welcome_letter.save()

        #send_mail(
            #subject=User.username,
           # message='Поздравляем вас с регистрацией на нашем новостном портале',
          #  from_email='georgij.sergeev98@yandex.ru',
         #   recipient_list=['gosha_sergeev12@mail.ru'])
        #return redirect ('/news')

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/news')

