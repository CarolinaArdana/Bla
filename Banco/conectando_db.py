import sqlite3

class Connect(object):

    def __init__(self, nome_db):
        try:
            self.conn = sqlite3.connect(nome_db)
            self.cursor = self.conn.cursor()
            print("Banco: %s " % nome_db)

        except sqlite3.Error:
            print("Erro")
            return False

    def close_db(self):
        if self.conn:
            self.conn.close()

    def commit_db(self):
        if self.conn:
            self.conn.commit()
            print('Dado Gravado')
