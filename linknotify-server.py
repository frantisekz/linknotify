#!/usr/bin/python3

from flask import Flask, request, jsonify
from collections import deque
import zmq

app = Flask(__name__)
context = zmq.Context()
zmq_socket = context.socket(zmq.PUSH)
zmq_socket.bind("tcp://127.0.0.1:5557")

URLS = deque([])

@app.route("/send", methods=['POST'])
def send():
    global URLS
    data = request.get_json()

    URLS.append(data['url'])
    zmq_socket.send_json(data)

    print(URLS)

    return "ok"

@app.route("/get")
def get():
    global URLS

    if URLS:
        url = URLS.popleft()
        print(URLS)
        return jsonify({
            'status': True,
            'url': url
        })
    else:
        print(URLS)
        return jsonify({
            'status': False
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0")
