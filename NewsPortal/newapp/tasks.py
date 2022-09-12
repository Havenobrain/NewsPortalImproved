from django_apscheduler.models import DjangoJobExecution
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *


def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

def letter_with_news_for_the_week():
    for category in Category.objects.all():
        for subscribers in CategorySubscribers.objects.filter(CategorySubscribers=category):
            post = PostCategory.object.filter(categoryThrough=category)
            msg = EmailMultiAlternatives(
                subject=f'Все новости за неделю в категории {category}',
                from_email='gosha_sergeev12@mail.ru',
                to=[user.email],)
            html_content = render_to_string(
                'subscribe_message_weekly.html',
                {
                    'post': post,
                    'subscriber': subscribers

                }

                                        )
            msg.attach_alternative(html_content, "text/html")
            msg.send()