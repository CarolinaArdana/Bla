import conectando_db
import sqlite3

class inserirDados(object):

    def __init__(self, dados):
        self.db = conectando_db.Connect('Datas.db')
        self.dados = dados


    def inserir_um_registro(self):
        try:
            with open('scriptInserir.sql', 'rt') as f:
                com_sql = f.read()
                self.db.cursor.execute(com_sql % self.dados)
            #gravando no bc
            self.db.commit_db()
            self.db.close_db()
            print("Um registro inserido com sucesso.")
        except sqlite3.IntegrityError:
            print("Erro ao inserir dados")
            return False