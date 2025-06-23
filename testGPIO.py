import RPi.GPIO as GPIO
import time

# Configuration des broches GPIO
TX_PIN = 14  # Broche GPIO 14 (TXD)
RX_PIN = 15  # Broche GPIO 15 (RXD)
GND_PIN = 6  # Broche GND (broche 6 sur le Raspberry Pi)
VCC_PIN = 2  # Broche 5V (broche 2 sur le Raspberry Pi)

# Configuration des broches GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TX_PIN, GPIO.OUT)
GPIO.setup(RX_PIN, GPIO.IN)
GPIO.setup(GND_PIN, GPIO.OUT)
GPIO.setup(VCC_PIN, GPIO.OUT)

# Définir GND et VCC
GPIO.output(GND_PIN, GPIO.LOW)
GPIO.output(VCC_PIN, GPIO.HIGH)

# Fonction pour envoyer un bit
def send_bit(bit):
    GPIO.output(TX_PIN, bit)
    time.sleep(0.001)  # Délai pour simuler la vitesse de transmission

# Fonction pour envoyer un octet
def send_byte(byte):
    for i in range(8):
        bit = (byte >> i) & 1
        send_bit(bit)

# Fonction pour envoyer une chaîne de caractères
def send_string(s):
    for char in s:
        send_byte(ord(char))

# Exemple d'utilisation
try:
    # Envoyer une commande d'initialisation
    send_byte(0x1B)  # ESC
    send_byte(0x40)  # @

    # Envoyer du texte
    send_string("Hello, World!\n")

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
