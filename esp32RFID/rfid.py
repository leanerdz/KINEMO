from time import sleep_ms

from machine import Pin, SPI

from mfrc522 import MFRC522

from acceptor import Acceptor


class RFID:

    def __init__(self, rfid_callback):

        self.rfid_callback = rfid_callback
        self.sck = Pin(18, Pin.OUT)
        self.mosi = Pin(23, Pin.OUT)
        self.miso = Pin(19, Pin.OUT)
        self.spi = SPI(baudrate=100000, polarity=0, phase=0, sck=self.sck, mosi=self.mosi, miso=self.miso)
        self.sda = Pin(5, Pin.OUT)
        self.last_uid = None
        self.target_uid = "0x53c13f0f"
        self.target_uid2 = "0x03ac890f"
        self.target_uid3 = "0xe36a75ad"
        self.target_uid4 = "0xc3bfc02f"
        self.target_uid5 = "0x13f69b0f"
        self.target_uid6 = "0xf34b5413"
        self.target_uid7 = "0x9376c82f"
        self.short_long_scan = Acceptor([
            [self.target_uid, None, self.target_uid, self.target_uid, self.target_uid, self.target_uid,
             self.target_uid],
            [self.target_uid, None, None, self.target_uid, self.target_uid, self.target_uid, self.target_uid],
            [self.target_uid, self.target_uid, None, self.target_uid, self.target_uid, self.target_uid,
             self.target_uid],
            [self.target_uid, self.target_uid, None, None, self.target_uid, self.target_uid, self.target_uid],
            [self.target_uid, self.target_uid, None, None, None, self.target_uid, self.target_uid]
        ], self.accept_short_long_scan, self.refuse_scan)
        self.longScan = Acceptor([
            [self.target_uid, self.target_uid, self.target_uid, self.target_uid, self.target_uid, self.target_uid,
             self.target_uid],
        ], self.accept_long_scan, self.refuse_scan)

    def read(self):
        """Lire un UID du lecteur RFID"""
        rdr = MFRC522(self.spi, self.sda)
        uid = None
        (stat, tag_type) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                uid = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
        return uid

    def listen(self):
        current_uid = self.read()
        # print(current_uid)
        #         if current_uid == self.target_uid:
        #             self.short_long_scan.update(current_uid)
        #             self.longScan.update(current_uid)
        #         else:
        #             self.short_long_scan.update(None)
        #             self.longScan.update(None)
        if current_uid == self.target_uid:
            self.rfid_callback('{"name" :"John Doe", "phonenumber" : "+33735405356"}')
        elif current_uid == self.target_uid2:
            self.rfid_callback('{"name" :"Romain", "phonenumber" : "33677089334@c.us"}')
        elif current_uid == self.target_uid3:
            self.rfid_callback('{"name" :"Sarah", "phonenumber" : "33677089334@c.us"}')
        elif current_uid == self.target_uid4:
            self.rfid_callback('{"name" :"Claire", "phonenumber" : "33677089334@c.us"}')
        elif current_uid == self.target_uid5:
            self.rfid_callback('{"name" :"Thomas", "phonenumber" : "33677089334@c.us"}')
        elif current_uid == self.target_uid6:
            self.rfid_callback('{"name" :"Maxime", "phonenumber" : "33677089334@c.us"}')
        elif current_uid == self.target_uid7:
            self.rfid_callback('{"name" :"Lina", "phonenumber" : "33677089334@c.us"}')
        else:
            self.rfid_callback(None)

    def accept_short_long_scan(self):
        print("\n********* Accepted short long SCAN ***********\n")

    def accept_long_scan(self):
        print("\n********* Accepted LONG SCAN ***********\n")

    def refuse_scan(self, refused_seq):
        print("Refused RFID sequence:", refused_seq)


