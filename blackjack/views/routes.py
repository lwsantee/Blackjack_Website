from flask import render_template
from blackjack import app
from blackjack import socketio


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on("my event")
def handle_custom_event(json):
    print("Message received: " + str(json))
