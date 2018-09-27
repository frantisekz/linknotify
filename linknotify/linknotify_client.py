from pgi.repository import Notify
import requests
from time import sleep
import zmq

from . import settings

Notify.init("linknotify")

context = zmq.Context()
#consumer_receiver = context.socket(zmq.PULL)
consumer_receiver = context.socket(zmq.SUB)
consumer_receiver.connect(settings.SERVER)
consumer_receiver.setsockopt(zmq.SUBSCRIBE, settings.USER.encode('utf-8'))

def main():
    while True:
        #data = consumer_receiver.recv_json()
        [_, url] = consumer_receiver.recv_multipart()
        n = Notify.Notification.new("Link", url.decode('utf-8'), "notification-message-im")
        n.show()


if __name__ == "__main__":
    main()