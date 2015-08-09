import Ana.SelecaoRegistro as s
import Ana.AnoHidrologico as Ano

class DadosVazao(object):

    def __init__(self, nome_db, TipoAno, TemporalID, anoInicio = 1931, anoFinal = 2014):
        self.nome_db = nome_db
        self.TipoAno = TipoAno
        self.TemporalID = TemporalID
        self.anoInicio = anoInicio
        self.anoFinal = anoFinal

    def Dados(self):
        anoSerie = Ano.Ano(self.nome_db, self.TemporalID, self.anoInicio, self.anoFinal)

        if self.TipoAno == 'Civil':
            lista = anoSerie.AnoCivil()
        elif self.TipoAno == 'Hidrologico':
            lista = anoSerie.anoHidrologico()

        dados2 = s.Selecao(self.nome_db).lerSerieTemporalDadosAnoHi(self.TemporalID,lista)
        dados = []
        for i in dados2:
            if i[1] != '-9999.9':
                dados.append(i)
        return dados


