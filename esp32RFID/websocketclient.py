import uwebsockets.client
import uasyncio
import json

class WebSocketClient:

    def __init__(self, srcName, ip, port):
        self.uri = f"ws://{ip}:{port}"
        self.websocket = uwebsockets.client.connect(self.uri)
        self.srcName = srcName
        self.send_presentation_message()

    def send_presentation_message(self):
        presentation_message = {
            "client_name": self.srcName
        }
        self.websocket.send(json.dumps(presentation_message))
        print(f"Message de présentation envoyé: {presentation_message}")

    def send(self, dest, data):
        self.websocket.send(self.generate_json(self.srcName, dest, data))

    def generate_json(self, src, dest, param):
        return json.dumps({
            "src": src,
            "dest": dest,
            "data": param
        })



