import conectando_db
import Datas

class Selecao(object):
    def __init__(self, nome_db):
        self.nome_db = nome_db
        self.db = conectando_db.Connect(self.nome_db)

    def lerDiscretizacao(self, Discretizacao):
        sql = "SELECT Discretização_ID FROM Discretizacao WHERE Tipo = '%s'" % Discretizacao
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

    def lerPosto(self, Tipo_Posto_ID, Fonte_ID):
        sql = "SELECT Posto_ID FROM Tipo_Posto WHERE " \
              "Tipo_Posto_ID = %s and Fonte_ID = %s" % (Tipo_Posto_ID, Fonte_ID)
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()[0][0]

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

    def lerSerieTemporal(self, fonte, anoInicio = 1931, anoFinal = 2014):
        datas = Datas.Datas(anoInicio, anoFinal, fonte)
        datas.Rdata()
        stri = ''
        for i in datas.ListaDatas:
            r = str("'%s', " % i[1])
            stri += r
        sql = "SELECT * FROM serie_temporal WHERE Data_e_Hora in (" + stri[:-2] + ")"
        self.db.cursor.execute(sql)
        Lista = self.db.cursor.fetchall()
        self.db.close_db()
        return Lista