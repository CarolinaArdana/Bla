import conectando_db
import Ana.SelecaoRegistro as s

class atualizaDados(object):

    def __init__(self, nome_db, dados):
        self.nome_db = nome_db
        self.db = conectando_db.Connect(self.nome_db)
        self.dados = dados

    def atualizarDadosSerieTemporal(self):
        stri = ''
        nDadosAdd = 0
        id = s.Selecao('BancoHidro').lerSerieTemporalID()
        for i in self.dados:
            r = str(" WHEN (Serie_Temporal_ID = %s and Data_e_Hora = '%s')  THEN '%s'" % (id, i[1], i[0]))
            stri += r
            nDadosAdd += 1
            if nDadosAdd == len(self.dados):
                sql = "UPDATE Serie_Temporal SET Dado = CASE" + stri + " ELSE Dado END"
                self.db.cursor.execute(sql)
                self.db.commit_db()
                print('%d por cento  Concluído' % (nDadosAdd/len(self.dados)*100))

        self.db.close_db()
