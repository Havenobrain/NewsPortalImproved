import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'action_every_sunday_at_8:00': {
        'task': 'newapp.tasks.letter_with_news_for_the_week',
        'schedule': crontab(hour=8, minute=0, day_of_week='sunday')
    },
}


app.conf.beat_schedule = {
    'action_after_posting': {
        'task': 'newapp.tasks.notify_for_new_post',
        'schedule': 10
    },
}