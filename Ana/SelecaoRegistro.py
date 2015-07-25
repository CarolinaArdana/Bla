import Ana.conectando_db as conectando_db
import Ana.Datas as Datas

class Selecao(object):
    def __init__(self, nome_db):
        self.nome_db = nome_db
        self.db = conectando_db.Connect(self.nome_db)

    def lerDiscretizacao(self, Discretizacao):
        sql = "SELECT Discretizacao_ID FROM Discretizacao WHERE Tipo = '%s'" % Discretizacao
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchone()[0]

    def lerFonte(self, Fonte):
        sql = "SELECT Fonte_ID FROM Fonte WHERE Fonte = '%s'" % Fonte
        print(sql)
        self.db.cursor.execute(sql)
        id = self.db.cursor.fetchone()
        if id == None:
            return id
        else:
            return id[0]

    def lerNivelConsistencia(self, Nivel):
        sql = "SELECT Tipo_Dados_ID FROM Nivel_Consistencia WHERE Nivel = '%s'" % Nivel
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchone()[0]

    def lerPosto(self, Fonte, Codigo_ANA):
        Fonte_ID = self.lerFonte(Fonte)
        sql = "SELECT Posto_ID FROM Posto WHERE " \
              "Fonte_ID = %s and Codigo_ANA = %s" % (Fonte_ID, Codigo_ANA)
        print(sql)
        self.db.cursor.execute(sql)
        id = self.db.cursor.fetchone()
        if id == None:
            return id
        else:
            return id[0]

    def lerReducao(self, Reducao):
        sql = "SELECT Reducao_ID FROM Reducao WHERE Tipo = '%s'" % Reducao
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchone()[0]

    def lerTipoPosto(self, Tipo):
        sql = "SELECT Tipo_Posto_ID FROM Tipo_Posto WHERE Tipo = '%s'" % Tipo
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchone()[0]

    def lerVariavel(self, Variavel):
        sql = "SELECT Variavel_ID FROM Variavel WHERE Variavel = '%s'" % Variavel
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchone[0]

    def lerUnidade(self, Unidade):
        sql = "SELECT Unidade_ID FROM Unidade WHERE Tipo = '%s'" % Unidade
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchone()[0]

    def lerSerieTemporalID(self):
        self.db.cursor.execute("SELECT MAX (Serie_Temporal_ID) FROM Serie_Temporal")
        id = self.db.cursor.fetchone()
        print(id)
        if id[0] == None:
            id = 0
        else:
            id = int(id[0])
        return id

    def lerSerieTemporalDados(self, SerieTemporalID, anoInicio = 1931, anoFinal = 2014):
        datas = Datas.Datas(anoInicio, anoFinal)
        datas.Rdata()
        stri = ''
        stri2 = ''
        for i in datas.ListaDatas:
            r = str("'%s', " % i[1])
            stri2 += "%s, " % SerieTemporalID
            stri += r
        sql = "SELECT * FROM serie_temporal WHERE Serie_Temporal_ID in (" + stri2[:-2] + ")" + " and Data_e_Hora in (" + stri[:-2] + ")"
        self.db.cursor.execute(sql)
        Lista = self.db.cursor.fetchall()
        self.db.close_db()
        return Lista

    def lerSerieTemporalDadosAnoHi(self, SerieTemporalID, ListaDatas):
        idS = SerieTemporalID
        Lista = []
        for i in ListaDatas:
            sql = "SELECT Data_e_Hora, Dado FROM serie_temporal WHERE Serie_Temporal_ID in (%s) and Data_e_Hora in ('%s')" % (idS, i)
            self.db.cursor.execute(sql)
            Lista.append(self.db.cursor.fetchone())
        self.db.close_db()
        return Lista