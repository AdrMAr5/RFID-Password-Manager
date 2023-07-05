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
        return value[0]

    def get_password_for_domain(self, domain):
        cur = self.db.cursor()
        cur.execute('SELECT domain, password FROM passwords WHERE domain=?', (domain,))
        value = cur.fetchall()
        return value

    def get_domains(self):
        cur = self.db.cursor()
        cur.execute('SELECT domain FROM passwords')
        value = cur.fetchall()
        return value


