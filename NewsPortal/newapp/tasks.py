from django_apscheduler.models import DjangoJobExecution
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *
from celery import shared_task
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


@shared_task
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


@shared_task
@receiver(m2m_changed, sender=Post)
def notify_for_new_post(sender, instance, action, **kwargs):
    # Добавление задания на отправку письма
    if action == 'post_add' and instance.__class__.__name__ == 'Post':
        notify_subscribers_about_new_post.apply_async(
            (instance.id, instance.name, instance.content),
            countdown=300,
        )

def notify_subscribers_about_new_post(sender, instance, action, **kwargs):
    mass =[]
    if action == 'post_add':
        for i in instance.postCategory.all():
            for j in i.subscribers.all():
                mass.append(j)
        for user in set(mass):
            msg = EmailMultiAlternatives(
                subject=f'В категорию, на которую вы подписаны, добавлен новый пост с заголовком {instance.title}',
                from_email='gosha_sergeev12@mail.ru',
                to=[user.email],)
            html_content = render_to_string(
                'sub_message.html',
                {
                    'user': user,
                    'post': instance,
                }
                                            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()