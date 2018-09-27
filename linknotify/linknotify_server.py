from flask import Flask, request, jsonify
from collections import deque
import zmq

from . import settings

app = Flask(__name__)
context = zmq.Context()
zmq_socket = context.socket(zmq.PUSH)
zmq_socket.bind(settings.SERVER)


@app.route("/send", methods=['POST'])
def send():
    data = request.get_json()

    zmq_socket.send_json(data)

    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
