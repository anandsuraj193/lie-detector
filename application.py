"""Run flask App Locally in Debug Mode"""

from lie_to_me import app, socketio


if __name__ == "__main__":
    socketio.run(app, host='127.0.0.1',debug=True)
