from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


#@receiver(m2m_changed, sender=Post.postCategory.through)
#def notify_subscribers(sender, instance, action, **kwargs):
   # mass =[]
   # if action == 'post_add':
   #     for i in instance.postCategory.all():
    #        for j in i.subscribers.all():
        #        mass.append(j)
       # for user in set(mass):
          #  msg = EmailMultiAlternatives(
         #       subject=f'В категорию, на которую вы подписаны, добавлен новый пост с заголовком {instance.title}',
         #       from_email='gosha_sergeev12@mail.ru',
         #       to=[user.email],)
          #  html_content = render_to_string(
         #       'sub_message.html',
         #       {
          #          'user': user,
          #          'post': instance,
          ##
# msg.attach_alternative(html_content, "text/html")
           # msg.send()




