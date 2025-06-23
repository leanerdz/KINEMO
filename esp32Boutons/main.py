import time
import uasyncio
from websocketclient import *
import machine
from machine import Pin

WSCLIENT_ON = True

if WSCLIENT_ON:
    wsClient = WebSocketClient("button", "192.168.121.225", "8081")

# Configuration des pins pour les boutons
button_pin_1 = Pin(15, Pin.IN, Pin.PULL_UP)
button_pin_2 = Pin(16, Pin.IN, Pin.PULL_UP)
button_pin_3 = Pin(13, Pin.IN, Pin.PULL_UP)
led_pin = Pin(4, Pin.OUT)

button_clicked_1 = False
button_clicked_2 = False
button_clicked_3 = False

previous_button_state_1 = True
previous_button_state_2 = True
led_pin.on()


def button_1():
    global button_pin_1, button_clicked_1, previous_button_state_1, message
    # Vérification du bouton 1
    current_button_state_1 = button_pin_1.value()
    if current_button_state_1 == 0 and previous_button_state_1 == 1:
        button_clicked_1 = not button_clicked_1
        try:
            if button_clicked_1:
                wsClient.send("Kinmo", 'SEND')
                print("Données envoyées pour le bouton 1 :", 'SEND')
        except Exception as e:
            print("Erreur lors de l'envoi des données pour le bouton 1 :", e)
    previous_button_state_1 = current_button_state_1


def button_2():
    global button_pin_2, button_clicked_2, previous_button_state_2, message
    # Vérification du bouton 2
    current_button_state_2 = button_pin_2.value()
    if current_button_state_2 == 0 and previous_button_state_2 == 1:
        button_clicked_2 = not button_clicked_2
        try:
            if button_clicked_2:
                wsClient.send("Kinmo", 'RESET')
                print("Données envoyées pour le bouton 2 :", 'RESET')
        except Exception as e:
            print("Erreur lors de l'envoi des données pour le bouton 2 :", e)
    previous_button_state_2 = current_button_state_2


def button_3():
    global button_pin_3, button_clicked_3, previous_button_state_3, message_to_send, message

    current_button_state_3 = button_pin_3.value()

    if current_button_state_3 == 0 and previous_button_state_3 == 1:
        button_clicked_3 = not button_clicked_3
        try:
            if button_clicked_3:
                if WSCLIENT_ON:
                    led_pin.off()
                    wsClient.send("Kinmo", 'RECORD')
                    print("Données envoyées pour le bouton 3 :", 'RECORD')
            else:
                if WSCLIENT_ON:
                    led_pin.on()
                    wsClient.send("Kinmo", 'STOP')  # Message différent pour le deuxième état
                    print("Données envoyées pour le bouton 3 :", 'STOP')
        except Exception as e:
            print("Erreur lors de l'envoi des données pour le bouton 3 :", e)

    previous_button_state_3 = current_button_state_3


while True:
    button_1()
    button_2()
    button_3()
    time.sleep(0.1)


