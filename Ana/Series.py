from datetime import date
import Ana.DadosVazaoDB as da
import Ana.LimiteParcial as lp
import matplotlib.pyplot as plt

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

    def separaDados(self):
        data = []
        vazao = []
        for i in self.dados:
            data.append(date(int(i[0][6:10]), int(i[0][3:5]), int(i[0][0:2])))
            vazao.append(float(i[1]))
        return data,vazao

'''
da = Dados.DadosVazao('BancoHidro','Civil', 1, 1980, 2014)
dados = da.Dados()

a = Series(dados)
ser = a.serieMaxAnual()
for i in ser:
    print(i)

dados = da.DadosVazao('BancoHidro', 1, 1995, 2012).Dados()
limite = lp.LimiteParcial(dados).AchaLimite(2)
a = Series(dados)

vazao = []
ano = 0
for i in a.serieMaxParcial(limite):
    if i[1] != -9999.9:
        vazao.append(i[1])

vazao.sort(reverse=True)
n = 17
tem = []
ind = 1
for i in vazao:
    print((n + 1)/ind)
    tem.append((n + 1)/ind)
    ind += 1

plt.plot(tem, vazao, 'bo')
print(tem)
print(vazao)
vazaoa = []
for i in a.serieMaxAnual():
    if i[1] != -9999.9:
        vazaoa.append(i[1])
vazaoa.sort(reverse=True)
na = len(vazaoa)
tema = []
inda = 1
for i in vazaoa:
    proa = inda/(n+1)
    tema.append(1/proa)
    inda += 1
print(tema)
print(vazaoa)
plt.plot(tema, vazaoa, 'r*')

plt.ylabel('Vazao')
plt.xlabel('Tempo de Retorno')
plt.axis([0, 40, 0, 20000])
plt.legend(numpoints = 1, loc = "best")
plt.show()
'''