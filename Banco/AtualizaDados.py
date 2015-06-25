import sqlite3
import conectando_db

class atualizaDados(object):

    def __init__(self, dados):
        self.db = conectando_db.Connect('Datas.db')
        self.dados = dados


    def atualiza(self):
        try:
            with open('scriptAtualiza.sql', 'rt') as f:
                com_sql = f.read()
                print(self.dados)
                self.db.cursor.execute(com_sql, self.dados)
                print('Dados atualizados')

            self.db.commit_db()
            self.db.close_db()
        except sqlite3.IntegrityError:
            print('Erro ao atualizar dados')
            return False