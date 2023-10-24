from flask import redirect, render_template, request, url_for
from blackjack import app
from blackjack import socketio


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on("my event")
def handle_custom_event(json):
    print("Message received: " + str(json))
