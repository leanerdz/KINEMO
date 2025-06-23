import network
import time

#SSID = "Cudy-F810"
#PASSWORD = "13022495"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connection to Wi-Fi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
            print("Waiting for connection")
    print("Connected to Wi-Fi :", wlan.ifconfig())

connect_wifi()

