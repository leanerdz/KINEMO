import time
from websocketclient import *
from rfid import *
import machine

WSCLIENT_ON = True

if (WSCLIENT_ON):
    wsClient = WebSocketClient("User", "192.168.121.225", "8081")


def rfid_callback(message):
    global wsClient
    if message is not None:
        wsClient.send("Kinmo", message)
        print(message)


rfid = RFID(rfid_callback)
i2c = I2C(0, scl=Pin(17), sda=Pin(21), freq=400000)  # Use hardware I2C

while True:
    rfid.listen()
    time.sleep(0.1)

