from blackjack import app
from blackjack import socketio
from .views import routes
from .controllers import ws_handlers
from .controllers import rest_api

if __name__ == "__main__":
    socketio.run(app, debug=True,
                 use_reloader=True, log_output=True)
