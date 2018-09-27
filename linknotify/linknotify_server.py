from flask import Flask, request, jsonify
from collections import deque
import zmq

from . import settings

app = Flask(__name__)
context = zmq.Context()
#zmq_socket = context.socket(zmq.PUSH)
zmq_socket = context.socket(zmq.PUB)
zmq_socket.bind(settings.SERVER)


@app.route("/send", methods=['POST'])
def send():
    data = request.get_json()
    
    #zmq_socket.send_json(data)

    if 'url' not in data or 'user' not in data:
        return "not ok"

    zmq_socket.send_multipart([data['user'].encode('utf-8'), data['url'].encode('utf-8')])

    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
