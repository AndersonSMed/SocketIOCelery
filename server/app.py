from flask import Flask
from flask_socketio import SocketIO
import handlers

# Adds a new flask instance
app = Flask(__name__)
# Setup a new instance of socketio
socketio = SocketIO(app, message_queue='redis://localhost:6379')

socketio.on_event('connect', handlers.retrieve_streams)

if __name__ == '__main__':

    socketio.run(app)