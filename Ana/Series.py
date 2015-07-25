import datetime
import Ana.SelecaoRegistro as s
import Ana.AnoHidrologico as Ano

class Series(object):
    def __init__(self,nome_db):
        self.nome_db = nome_db

    def maxAnual(self, TipoAno, TemporalID, anoInicio = 1931, anoFinal = 2014):
        dicDados = {}
        anoSerie = Ano.Ano(self.nome_db, anoInicio, anoFinal)

        if TipoAno == 'Civil':
            lista = anoSerie.AnoCivil().items()
        elif TipoAno == 'Hidrologico':
            lista = anoSerie.anoHidrologico().items()

        for i in lista:
            dado = s.Selecao(self.nome_db).lerSerieTemporalDadosAnoHi(TemporalID,i[1])
            print(dado)
            dicDados[i[0]] = dado

        return dicDados



a = Series('BancoHidro')

for i in a.maxAnual('Hidrologico', 1).items():
    print(i)