class Series(object):
    def __init__(self, dados):
        self.dados = dados

    def serieMaxAnual(self):
        maxp = []
        aux = []
        data = []
        for i in self.dados:
            if int(i[0][0:2]) == 31 and int(i[0][3:5]) == 12:
                data.append(i[0])
                aux.append(float(i[1]))
                indx = aux.index(max(aux))
                maxp.append([data[indx], max(aux)])
                data = []
                aux = []
            else:
                data.append(i[0])
                aux.append(float(i[1]))

        return maxp

    def serieMaxParcial(self, criterioParcial):
        maxp = []
        aux = []
        data = []
        for i in self.dados:
            if float(i[1]) > criterioParcial:
                aux.append(float(i[1]))
                data.append(i[0][0:10])
            elif float(i[1]) < criterioParcial and len(aux) > 0:
                indx = aux.index(max(aux))
                maxp.append([data[indx], max(aux)])
                data = []
                aux = []
        return maxp

'''
da = Dados.DadosVazao('BancoHidro','Civil', 1, 1980, 2014)
dados = da.Dados()

a = Series(dados)
ser = a.serieMaxAnual()
for i in ser:
    print(i)

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
'''