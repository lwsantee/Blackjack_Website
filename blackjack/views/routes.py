from flask import render_template
from flask_socketio import SocketIO
from blackjack import app


@app.route('/')
def index():
    return render_template('index.html')


@SocketIO.on('connect')
def handle_connect():
    # Handle client connection
    print("Client connected")


@SocketIO.on('disconnect')
def handle_disconnect():
    # Handle client disconnection
    print("Client disconnected")


@SocketIO.on('start_game')
def start_game(data):
    # Start the game and broadcast updates to all clients
    players = data['players']
    # blackjack_game.start_game(players)
    SocketIO.emit('game_started', {'message': 'Game started!'}, broadcast=True)


@SocketIO.on('player_action')
def player_action(data):
    # Handle player actions (hit, stand, etc.) and broadcast updates
    player_id = data['player_id']
    action = data['action']
    # blackjack_game.player_action(player_id, action)

    # Broadcast the updated game state to all clients
    # SocketIO.emit('update_game_state', {'state': blackjack_game.get_state()}, broadcast=True)
