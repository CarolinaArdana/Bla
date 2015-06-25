import sqlite3
import conectando_db

class Tabela(object):

    def __init__(self, tb_nome):
        self.db = conectando_db.Connect("BancoHidro.db")
        self.tb_nome = '%s.sql' % tb_nome

    def criar_tabelas(self):
        print("Criando tabela %s" % self.tb_nome)

        try:
            with open(self.tb_nome, 'rt') as f:
                com_sql = f.read()
                self.db.cursor.executescript(com_sql)
        except sqlite3.Error:

            return False
        print("Tabela %s criada com sucesso." % self.tb_nome)