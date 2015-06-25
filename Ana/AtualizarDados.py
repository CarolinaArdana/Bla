import conectando_db

class atualizaDados(object):

    def __init__(self, dados, nome_db):
        self.nome_db = nome_db
        self.db = conectando_db.Connect(self.nome_db)
        self.dados = dados

    def atualizarDadosSerieTemporal(self):
        stri = ''
        nDados = 0
        nDadosAdd = 0
        for i in self.dados:
            r = str(" WHEN '%s' THEN '%s'" % (i[1], i[0]))
            stri += r
            nDadosAdd += 1
            nDados += 1
            if nDados == 400 or nDadosAdd == len(self.dados):
                sql = "UPDATE Serie_Temporal SET Dado = CASE Data_e_Hora" + stri + " ELSE Dado END"
                self.db.cursor.execute(sql)
                self.db.commit_db()
                print('%d por cento  Concluído' % (nDadosAdd/len(self.dados)*100))
                stri = ''
                nDados = 0

        self.db.close_db()