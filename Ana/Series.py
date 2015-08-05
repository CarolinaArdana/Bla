import datetime
import Ana.SelecaoRegistro as s
import Ana.AnoHidrologico as Ano
import matplotlib.pyplot as plt

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
            data = []
            for j in i[1]:
                aux.append(float(j[1]))
                data.append(j[0])
            vazoesMax[i[0]] = ([data[aux.index(max(aux))],max(aux)])
        return vazoesMax
    def serieMaxParcial(self, criterioParcial):
        vazoesMaxParcial = {}


        for i in self.Dados().items():
            maxp = []
            aux = []
            data = []
            for j in i[1]:
                if float(j[1]) > criterioParcial:
                    aux.append(float(j[1]))
                    data.append(j[0][0:10])
                elif float(j[1]) < criterioParcial and len(aux) > 0:
                    indx = aux.index(max(aux))
                    maxp.append([data[indx], max(aux)])
                    data = []
                    aux = []
            vazoesMaxParcial[i[0]] = maxp
            #vazoesMaxParcial[i[0]] = [x for x in aux if x > criterioParcial]
        return vazoesMaxParcial


a = Series('BancoHidro','Hidrologico', 1,1980, 2014)

vazao = []
ano = 0
for i in a.serieMaxParcial(2700).items():
    ano+=1
    for j in i[1]:
        vazao.append(j[1])
        if j[1] == -9999.9:
            vazao.remove(-9999.9)

vazao.sort(reverse=True)
n = len(vazao)
tem = []
ind = 1
for i in vazao:
    tem.append((ano + 1)/ind)
    ind += 1

j = 0
while j < len(tem):
    plt.plot(tem[j], vazao[j], 'bo')
    j+=1

vazaoa = []
for i in a.serieMaxAnual().items():
    vazaoa.append(i[1][1])
    if i[1][1] == -9999.9:
        vazaoa.remove(-9999.9)
vazaoa.sort(reverse=True)
na = len(vazaoa)
tema = []
inda = 1
for i in vazaoa:
    proa = inda/(na+1)
    tema.append(1/proa)
    inda += 1

j = 0
while j < len(tema):
    plt.plot(tema[j], vazaoa[j], 'r*')
    j+=1

plt.ylabel('Vazao')
plt.xlabel('Tempo de Retorno')
plt.axis([0, 40, 0, 20000])
plt.legend(numpoints = 1, loc = "best")
plt.show()