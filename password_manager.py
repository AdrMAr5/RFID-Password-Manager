import base64
import random
import secrets
import string
import time
from cryptography.fernet import Fernet

import hashlib
import serial
from database import DatabaseClient


class PasswordManager:
    def __init__(self):
        self.db = DatabaseClient()
        self.authenticated = False
        self.master_key = ''

    def authenticate(self):
        card = ''
        arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
        time.sleep(3)
        arduino.write("R".encode())
        arduino.readline()
        start = time.time()
        print('Przyłóż kartę do czytnika')
        while time.time() - start < 10:
            received = arduino.readline()
            if received:
                card = received.decode()
                break
        arduino.close()
        db_hash = self.db.select_card_hash()
        sha512 = hashlib.sha512()
        sha512.update(card.encode())
        if sha512.hexdigest() == db_hash[0]:
            self.authenticated = True
            self.generate_master_key(card)
            print('uwierzytelniono')
            return True
        return False

    def save_new_password(self, domain, pswd):
        f = Fernet(base64.urlsafe_b64encode(self.master_key.encode()))
        encrypted_pswd = f.encrypt(pswd.encode())
        try:
            self.db.insert_password_record(domain, encrypted_pswd)
            print('Pomyślnie zapisano')
        except:
            print('Nie udało się zapisać do bazy danych')

    def display_password_for_domain(self, domain):
        result = self.db.get_password_for_domain(domain)
        f = Fernet(base64.urlsafe_b64encode(self.master_key.encode()))
        decrypted_pswd = f.decrypt(result[0][1]).decode()
        print(f'Domena: {result[0][0]} Hasło: {decrypted_pswd}')

    def update_password_for_domain(self, domain, pswd):
        f = Fernet(base64.urlsafe_b64encode(self.master_key.encode()))
        encrypted_pswd = f.encrypt(pswd.encode())
        self.db.update_password(domain, encrypted_pswd)

    def remove_password(self, domain):
        self.db.remove_record(domain)

    @staticmethod
    def generate_random_string(length):
        st = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(st) for _ in range(length))

    def list_domains(self):
        domains_list = self.db.get_domains()
        for domain in domains_list:
            print(domain[0])

    def generate_master_key(self, seed):
        random.seed(seed)
        num = random.random()
        sha256 = hashlib.sha256()
        sha256.update(str(num).encode())
        key = sha256.hexdigest()[:32]
        self.master_key = key
        print(key)
