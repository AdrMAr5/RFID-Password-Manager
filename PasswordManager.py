import time

import serial
from Database import DatabaseClient


class PasswordManager:
    def __init__(self):
        self.db = DatabaseClient()
        self.authenticated = False

    def authenticate(self):
        arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
        arduino.write(bytearray('R', 'ascii'))
        start = time.time()
        print('Przyłóż kartę do czytnika')
        while time.time() - start < 5000:
            received = arduino.readline()
            print(received)
            if received:
                break




    def save_new_password(self, domain, pswd):
        encrypted_pswd = pswd
        try:
            self.db.insert_password_record(domain, encrypted_pswd)
            print('Pomyślnie zapisano')
        except:
            print('Nie udało się zapisać do bazy danych')

    def pass_key(self):
        pass

    def pass_value(self):
        pass

    def get_password(self):
        pass

    def generate_random_string(self):
        pass

    def list_passwords(self):
        pass

