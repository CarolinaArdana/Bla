import Ana.SelecaoRegistro as s
import Ana.AnoHidrologico as Ano

class DadosVazao(object):

    def __init__(self, nome_db, TemporalID, anoInicio = 1931, anoFinal = 2014):
        self.nome_db = nome_db
        self.TemporalID = TemporalID
        self.anoInicio = anoInicio
        self.anoFinal = anoFinal

    def Dados(self):
        anoSerie = Ano.Ano(self.nome_db, self.TemporalID, self.anoInicio, self.anoFinal)
        lista = anoSerie.anoHidrologico()

        dados2 = s.Selecao(self.nome_db).lerSerieTemporalDadosAnoHi(self.TemporalID,lista)
        dados = []
        for i in dados2:
            if float(i[1]) > 0:
                dados.append(i)
        return dados


