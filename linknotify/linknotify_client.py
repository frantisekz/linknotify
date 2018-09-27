from pgi.repository import Notify
import requests
from time import sleep
import zmq

from . import settings

Notify.init("linknotify")

context = zmq.Context()
consumer_receiver = context.socket(zmq.PULL)
consumer_receiver.connect(settings.SERVER)

def main():
    while True:
        data = consumer_receiver.recv_json()
        n = Notify.Notification.new("Link", data['url'], "notification-message-im")
        n.show()


if __name__ == "__main__":
    main()