import sqlite3 as sl


class DatabaseClient:

    def __init__(self):
        self.db = sl.connect('passwords.db')

    def insert_password_record(self, domain, pswd):

        self.db.execute('INSERT INTO passwords(domain, password) VALUES (?, ?)', (domain, pswd))
        self.db.commit()

    def select_card_hash(self):
        cur = self.db.cursor()
        cur.execute('SELECT card_hash FROM secrets')
        value = cur.fetchall()
        return value



