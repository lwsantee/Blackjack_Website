import http
from flask import Response, request
from flask_socketio import emit, send
from blackjack import socketio
from blackjack.models.Player import Player
from blackjack import app


@socketio.on('connect')
def handle_connect():
    print('A user connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected')
