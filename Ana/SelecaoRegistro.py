import conectando_db
import Datas

class Selecao(object):
    def __init__(self, nome_db):
        self.nome_db = nome_db
        self.db = conectando_db.Connect(self.nome_db)

    def lerDiscretizacao(self, Discretizacao):
        sql = "SELECT Discretizacao_ID FROM Discretizacao WHERE Tipo = '%s'" % Discretizacao
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()[0][0]

    def lerFonte(self, Fonte):
        sql = "SELECT Fonte_ID FROM Fonte WHERE Fonte = '%s'" % Fonte
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()[0][0]

    def lerNivelConsistencia(self, Nivel):
        sql = "SELECT Tipo_Dados_ID FROM Nivel_Consistencia WHERE Nivel = '%s'" % Nivel
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()[0][0]

    def lerPosto(self, Fonte_ID, Codigo_ANA):
        sql = "SELECT Posto_ID FROM Posto WHERE " \
              "Fonte_ID = %s and Codigo_ANA = %s" % (Fonte_ID, Codigo_ANA)
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchone()

    def lerReducao(self, Reducao):
        sql = "SELECT Reducao_ID FROM Reducao WHERE Tipo = '%s'" % Reducao
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()[0][0]

    def lerTipoPosto(self, Tipo):
        sql = "SELECT Tipo_Posto_ID FROM Tipo_Posto WHERE Tipo = '%s'" % Tipo
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()[0][0]

    def lerVariavel(self, Variavel):
        sql = "SELECT Variavel_ID FROM Variavel WHERE Variavel = '%s'" % Variavel
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()[0][0]

    def lerUnidade(self, Unidade):
        sql = "SELECT Unidade_ID FROM Unidade WHERE Tipo = '%s'" % Unidade
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()[0][0]

    def lerSerieTemporal(self):
        self.db.cursor.execute("SELECT MAX (Serie_Temporal_ID) FROM Serie_Temporal")
        id = self.db.cursor.fetchone()
        print(id)
        if id[0] == None:
            id = 0
        else:
            id = int(id[0])
        return id