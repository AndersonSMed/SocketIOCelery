from __future__ import absolute_import, unicode_literals
from celery import shared_task
from mongo import models
import requests
from mongoengine import connect
from mongoengine.connection import disconnect
from flask_socketio import SocketIO

@shared_task
def load_from_api():
    connect(
        'streams',
        host='mongodb+srv://anderson:anderson01021997@cluster0-wbfjv.mongodb.net/test?retryWrites=true&w=majority'
    )

    url = "https://api.twitch.tv/kraken/streams/?language=pt-br"
    
    headers = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": "3n1fwxo1kfd6xiyiymkltmf2bjut1f"
    }

    request = requests.get(url, headers=headers)

    for data in request.json()['streams']:
        
        data['channel'].pop('created_at')
        data['channel'].pop('updated_at')
        data.pop('created_at')

        new_stream = models.Stream(**data)
        new_stream.save()
    
    disconnect()

@shared_task
def emit_ten_viwed():
    connect(
        'streams',
        host='mongodb+srv://anderson:anderson01021997@cluster0-wbfjv.mongodb.net/test?retryWrites=true&w=majority'
    )

    socketio = SocketIO(message_queue='redis://localhost:6379')
    socketio.emit('most viwed', models.Stream.objects.order_by('-viewers')[:10].to_json())

    disconnect()