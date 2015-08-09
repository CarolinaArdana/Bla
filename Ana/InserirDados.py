import conectando_db
import Ana.SelecaoRegistro as s

class inserirDados(object):
    def __init__(self, nome_db, dados = None):
        #if (type(dados) == type([]) or type(dados) == type({}) or type(dados) == type(())):
        #    self.dados = dados
        #else:

        self.dados = dados
        self.nome_db = nome_db
        self.db = conectando_db.Connect(self.nome_db)

    def Serie_Temporal(self):
        stri = ''
        nDados = 0
        nDadosAdd = 0
        id = s.Selecao(self.nome_db).lerSerieTemporalID()+1
        for i in self.dados:
            r = str(", (%s, '%s', '%s')" % (id, i[1], i[0]))
            stri += r
            nDadosAdd += 1
            nDados += 1
            if nDados == 500 or nDadosAdd == len(self.dados):
                sql = "INSERT INTO Serie_Temporal(Serie_Temporal_ID, Data_e_Hora, Dado) VALUES" + stri[1:]
                self.db.cursor.execute(sql)
                self.db.commit_db()
                print('%d por cento  Concluído' % (nDadosAdd/len(self.dados)*100))
                stri = ''
                nDados = 0

        #gravando no bc
        self.db.close_db()
    def Posto(self, Tipo_Posto, Fonte):
        Tipo_Posto_ID = s.Selecao(self.nome_db).lerTipoPosto(Tipo_Posto)
        Fonte_ID = s.Selecao(self.nome_db).lerFonte(Fonte)
        Codigo = self.dados
        if (s.Selecao('BancoHidro').lerPosto(Fonte, Codigo) == None):
            sql = "INSERT INTO Posto(Tipo_Posto_ID, Fonte_ID, Codigo_Ana) "\
                  "VALUES(%s, %s,'%s')" %(Tipo_Posto_ID, Fonte_ID, Codigo)
            self.db.cursor.execute(sql)
            self.db.commit_db()
            self.db.close_db()
    def Serie_Original(self,Fonte, Codigo, Arquivo_Fonte_Data, Variavel, Tipo_Dados, Discretizacao, Unidade):
        Posto_ID = s.Selecao(self.nome_db).lerPosto(Fonte, Codigo)
        Variavel_ID = s.Selecao(self.nome_db).lerVariavel(Variavel)
        Tipo_Dado_ID = s.Selecao(self.nome_db).lerNivelConsistencia(Tipo_Dados)
        Discretizacao_ID = s.Selecao(self.nome_db).lerDiscretizacao(Discretizacao)
        Unidade_ID = s.Selecao(self.nome_db).lerUnidade(Unidade)
        Serie_Temporal_ID = s.Selecao(self.nome_db).lerSerieTemporalID()

        stri = str("(%s, '%s', %s, %s, %s, %s, %s)" %
                   (Posto_ID, Arquivo_Fonte_Data, Variavel_ID, Tipo_Dado_ID, Discretizacao_ID, Unidade_ID, Serie_Temporal_ID))
        sql = "INSERT INTO Serie_Original(" \
              "Posto_ID, " \
              "Arquivo_Fonte_Data, " \
              "Variavel_ID, " \
              "Tipo_Dado_ID, " \
              "Discretizacao_ID, " \
              "Unidade_ID, " \
              "Serie_Temporal_ID) VALUES" + stri
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def Serie_Reduzida(self, Fonte, Codigo, Arquivo_Fonte_Data, Variavel, Tipo_Dados, Discretizacao_Orig,
                       Unidade, Discretizacao_Red, Reducao, parcial_Mi=None, parcial_U=None):
        Serie_Original = s.Selecao(self.nome_db).lerSerieOriginal(Fonte, Codigo, Arquivo_Fonte_Data,
                                                                     Variavel, Tipo_Dados, Discretizacao_Orig,
                                                                     Unidade)
        Discretizacao_ID = s.Selecao(self.nome_db).lerDiscretizacao(Discretizacao_Red)
        Reducao_ID = s.Selecao(self.nome_db).lerReducao(Reducao)
        print(Serie_Original)
        Serie_Original_ID = Serie_Original[0]
        Serie_Temporal_ID = Serie_Original[1]
        if parcial_Mi == None and parcial_U == None:
            stri = str("(%s, %s, %s, %s)" % (Serie_Original_ID, Discretizacao_ID, Reducao_ID, Serie_Temporal_ID))
        else:
            stri = str("(%s, %s, %s, %s, %s, %s)" % (Serie_Original_ID, Discretizacao_ID, Reducao_ID,
                                                     Serie_Temporal_ID, parcial_Mi, parcial_U))
        sql = "INSERT INTO Serie_Reduzida(" \
              "Serie_Original_ID, " \
              "Discretizacao_ID," \
              "Reducao_ID," \
              "Serie_Temporal_ID) VALUES" + stri
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def Nivel_Consistencia(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Nivel_Consistencia(Nivel) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def Tipo_Posto(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Tipo_Posto(Tipo) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def Unidade(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Unidade(Tipo) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def Variavel(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Variavel(Variavel) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def Fonte(self, Fonte):
        if s.Selecao(self.nome_db).lerFonte(Fonte) == None:
            sql = "INSERT INTO Fonte(Fonte) VALUES('%s')" % self.dados
            self.db.cursor.execute(sql)
            self.db.commit_db()
            self.db.close_db()
    def Discretizacao(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Discretizacao(Tipo) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()
    def Reducao(self):
        stri = ''
        for i in self.dados:
            r = str(", ('%s')" % i)
            stri += r
        sql = "INSERT INTO Reducao(Tipo) VALUES" + stri[1:]
        self.db.cursor.execute(sql)
        self.db.commit_db()
        self.db.close_db()