import http
from flask import Response, request
from flask_socketio import emit, send
from blackjack import socketio
from blackjack.models.Player import Player
from blackjack import app


@app.route("/api/active-players")
def handle_get_active_players():
    return Player.get_active_players_json()

@app.route("/api/verify-player-name", methods=["POST"])
def handle_submit_player():

    if request.get_json() is None:
        return Response("Expected json payload", http.HTTPStatus.BAD_REQUEST)

    if "playerName" not in request.get_json():
        return Response("Missing field 'playerName'", http.HTTPStatus.BAD_REQUEST)

    if "playerBalance" not in request.get_json():
        return Response("Missing field 'playerBalance'", http.HTTPStatus.BAD_REQUEST)

    new_player = Player.add_player(
        request.get_json()["playerName"], request.get_json()["playerBalance"]
    )
    if new_player is None:
        return Response("Player name is already in use", http.HTTPStatus.CONFLICT)

    return {
        "active_players": Player.get_active_players_json(),
    }
