import sqlite3

class Connect(object):

    def __init__(self, nome_db):
        self.nome_db = nome_db
        self.conn = sqlite3.connect('%s.db' % self.nome_db)
        self.cursor = self.conn.cursor()

        print("Banco: %s " % nome_db)

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada")

    def commit_db(self):
        if self.conn:
            self.conn.commit()
            print("Dado gravado")

