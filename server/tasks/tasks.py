from __future__ import absolute_import, unicode_literals
from celery import shared_task
from mongo import models
import requests
from mongoengine import connect
from mongoengine.connection import disconnect
from flask_socketio import SocketIO
from datetime import datetime
import json

@shared_task
def load_from_api():

    url = "https://api.twitch.tv/kraken/streams/?language=pt-br"
    
    headers = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": "3n1fwxo1kfd6xiyiymkltmf2bjut1f"
    }

    request = requests.get(url, headers=headers)

    date_fetch = datetime.utcnow().strftime('%d%m%Y%H%M%S')

    insert_in_db.apply_async(args=[request.json()['streams'], date_fetch])
       

@shared_task
def insert_in_db(streams, date_fetch):

    connect(
        'streams',
        host='mongodb+srv://anderson:anderson01021997@cluster0-wbfjv.mongodb.net/test?retryWrites=true&w=majority'
    )

    for data in streams:
        
        data['channel'].pop('created_at')
        data['channel'].pop('updated_at')
        data.pop('created_at')
        data['date_fetch'] = datetime.strptime(date_fetch, '%d%m%Y%H%M%S')
            
        new_stream = models.Stream(**data)
        new_stream.save()

    pipeline = [
        { "$sort": { 'date_fetch' : -1 } },
        { "$limit": 1 }
    ]

    last_result = list(models.Stream.objects.aggregate(*pipeline))[0]

    socketio = SocketIO(message_queue='redis://localhost:6379')
    socketio.emit('most viwed', models.Stream.objects.filter(date_fetch=last_result['date_fetch']).order_by('-viewers').limit(50).to_json())

    disconnect()