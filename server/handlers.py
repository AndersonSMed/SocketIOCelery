from mongoengine import connect
from mongoengine.connection import disconnect
from flask_socketio import SocketIO
from flask import request
from mongo import models

def retrieve_streams():

    connect(
        'streams',
        host='mongodb+srv://anderson:anderson01021997@cluster0-wbfjv.mongodb.net/test?retryWrites=true&w=majority'
    )

    pipeline = [
        { "$sort": { 'date_fetch' : -1 } },
        { "$limit": 1 }
    ]


    last_result = list(models.Stream.objects.aggregate(*pipeline))[0]

    socketio = SocketIO(message_queue='redis://localhost:6379')
    socketio.emit(
        'most viwed',
        models.Stream.objects.filter(date_fetch=last_result['date_fetch']).order_by('-viewers').limit(50).to_json(),
        room=request.sid
    )

    disconnect()