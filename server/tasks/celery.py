from __future__ import absolute_import, unicode_literals
from celery import Celery
from mongo import models

app = Celery('celery', include=['tasks.tasks'])

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.tasks.load_from_api',
        'schedule': 15.0
    }
}

app.conf.accept_content = ['json', 'application/json']

app.conf.broker_url = 'redis://localhost:6379'

app.conf.timezone = 'Brazil/West'

if __name__ == '__main__':
    app.start()