from blackjack import app
from blackjack import socketio
from .views import routes

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", use_reloader=True, log_output=True)
