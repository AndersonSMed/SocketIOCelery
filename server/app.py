from flask import Flask
from flask_socketio import SocketIO


# Adds a new flask instance
app = Flask(__name__)
# Setup a new instance of socketio
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)