import datetime
import Ana.SelecaoRegistro as s
import Ana.AnoHidrologico as Ano

class Series(object):
    def __init__(self, nome_db, TipoAno, TemporalID, anoInicio = 1931, anoFinal = 2014):
        self.nome_db = nome_db
        self.TipoAno = TipoAno
        self.TemporalID = TemporalID
        self.anoInicio = anoInicio
        self.anoFinal = anoFinal
    def Dados(self):
        dicDados = {}
        anoSerie = Ano.Ano(self.nome_db, self.TemporalID, self.anoInicio, self.anoFinal)

        if self.TipoAno == 'Civil':
            lista = anoSerie.AnoCivil().items()
        elif self.TipoAno == 'Hidrologico':
            lista = anoSerie.anoHidrologico().items()

        for i in lista:
            dado = s.Selecao(self.nome_db).lerSerieTemporalDadosAnoHi(self.TemporalID,i[1])
            dicDados[i[0]] = dado
        return dicDados

    def serieMaxAnual(self):
        vazoesMax = {}

        for i in self.Dados().items():
            aux = []
            for j in i[1]:
                aux.append(float(j[1]))
            vazoesMax[i[0]] = max(aux)
        return vazoesMax

    def serieMaxParcial(self, criterioParcial):
        vazoesMaxParcial = {}

        for i in self.Dados().items():
            aux = []
            for j in i[1]:
                aux.append(float(j[1]))
            vazoesMaxParcial[i[0]] = [x for x in aux if x > criterioParcial]
        return vazoesMaxParcial


a = Series('BancoHidro','Hidrologico', 2,1985, 2012)
vazao = []

for i in a.serieMaxAnual().items():
    vazao.append(i[1])
    if i[1] == -9999.9:
        vazao.remove(-9999.9)
vazao.sort(reverse=True)
n = len(vazao)
res = []
ind = 1
for i in vazao:
    pro = ind/(n+1)
    tem = 1/pro
    res.append("%i;%.2f;%.4f;%.2f" % (ind, i, pro, tem))
    ind += 1
print("i;Vazao;Prop;TempoR")
for i in res:
    print(i)