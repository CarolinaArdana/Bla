import conectando_db
import SelecaoRegistro as s
class inserirDados(object):

    def __init__(self, dados, nome_db):
        self.dados = dados
        self.nome_db = nome_db
        self.db = conectando_db.Connect(self.nome_db)

    def inserirSerieTemporal(self):
        stri = ''
        nDados = 0
        nDadosAdd = 0
        id = s.Selecao(self.nome_db).lerSerieTemporal()+1
        for i in self.dados:
            r = str(", (%s, '%s', '%s')" % (id, i[1], i[0]))
            stri += r
            nDadosAdd += 1
            nDados += 1
            if nDados == 400 or nDadosAdd == len(self.dados):
                sql = "INSERT INTO Serie_Temporal(Serie_Temporal_ID, Data_e_Hora, Dado) VALUES" + stri[1:]
                print(sql)
                self.db.cursor.execute(sql)
                self.db.commit_db()
                print('%d por cento  Concluído' % (nDadosAdd/len(self.dados)*100))
                stri = ''
                nDados = 0

        #gravando no bc
        self.db.close_db()
    def inserirPosto(self):
        stri = ''
        for i in self.dados:
            r = str(", (%s, %s, '%s')" % (i[0], i[1], i[2]))
            stri += r
        sql = "INSERT INTO Posto(Tipo_Posto_ID, Fonte_ID, Codigo_Ana) VALUES" + stri[1:]
        print(sql)
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def inserirSerieOriginal(self):
        stri = ''
        for i in self.dados:
            r = str(", (%s, '%s', %s, %s, %s, %s, %s)" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
            stri += r
        sql = "INSERT INTO Serie_Original(" \
              "Posto_ID, " \
              "Arquivo_Fonte_Data, " \
              "Variavel_ID, " \
              "Tipo_Dado_ID, " \
              "Discretizacao_ID, " \
              "Unidade_ID, " \
              "Serie_Temporal_ID) VALUES" + stri[2:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def inserirSerieReduzida(self):
        stri = ''
        for i in self.dados:
            r = str(", (%i, %i, %i, %i)" % (i[0], i[1], i[2], i[3]))
            stri += r
        sql = "INSERT INTO Serie_Reduzida(" \
              "Serie_Original_ID, " \
              "Discretizacao_ID," \
              "Reducao_ID," \
              "Serie_Temporal_ID) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def inserirNivelConsistencia(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Nivel_Consistencia(Nivel) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def inserirTipoPosto(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Tipo_Posto(Tipo) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def inserirUnidade(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Unidade(Tipo) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def inserirVariavel(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Variavel(Variavel) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def inserirFonte(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Fonte(Fonte) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def inserirDiscretizacao(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Discretizacao(Tipo) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def inserirReducao(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Reducao(Tipo) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()