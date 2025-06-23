import serial
import time

# Configure le port série
ser = serial.Serial(
    port='/dev/serial0',  # Peut être /dev/ttyS0 ou /dev/ttyAMA0 selon la configuration
    baudrate=19200,  # Vérifiez le taux de baud de votre imprimante
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

try:
    # Ouvrir le port série
    ser.open()
    ser.is_open
except Exception as e:
    print("Erreur lors de l'ouverture du port série: ", e)
    exit()

# Envoyer des données à l'imprimante
try:
    ser.write(b'\x1B\x40')  # Commande d'initialisation de l'imprimante
    time.sleep(1)
    ser.write(b'Hello, World!\n')  # Texte à imprimer
except Exception as e:
    print("Erreur lors de l'écriture sur le port série: ", e)

# Fermer le port série
ser.close()
