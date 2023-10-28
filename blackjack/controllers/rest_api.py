import http
from flask import Response, request
from flask_socketio import emit, send
from blackjack import socketio
from blackjack.models.Player import Player
from blackjack import app


@app.route("/api/active-players", methods=["GET"])
def handle_get_active_players():
    return Player.get_active_players_json()


@app.route("/api/player-join", methods=["POST"])
def handle_player_join():

    if request.get_json() is None:
        return Response("Expected json payload", http.HTTPStatus.BAD_REQUEST)

    required_fields = ["playerName", "playerBalance", "playerSeat"]
    for field in required_fields:
        if field not in request.get_json():
            return Response(f"Missing field '{field}'", http.HTTPStatus.BAD_REQUEST)

    new_player = Player.add_player(
        request.get_json()["playerName"],
        request.get_json()["playerBalance"],
        request.get_json()["playerSeat"],
    )
    if new_player is None:
        return Response("Player name is already in use", http.HTTPStatus.CONFLICT)

    socketio.emit("display-other-players",
                  {new_player.name: new_player.to_json()})

    return {
        "active_players": Player.get_active_players_json(),
    }
