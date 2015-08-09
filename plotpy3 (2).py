#FUNCTIONS
from datetime import date
import matplotlib.pyplot as plt
import Ana.DadosVazaoDB as da
import Ana.LimiteParcial as limite
import Ana.Series as se

def separaDados(dados):
    data = []
    vazao = []
    for i in dados:
        data.append(date(int(i[0][6:10]), int(i[0][3:5]), int(i[0][0:2])))
        vazao.append(float(i[1]))
    return data,vazao
#MAIN
dados = da.DadosVazao('F:\\Clebson\\HidroComp\\Ana\\BancoHidro', 1, 1995, 2009)
dado = dados.Dados()
data,vazao = separaDados(dado)
Limite1 = limite.LimiteParcial(dado).AchaLimite(1.65)
Limite2 = limite.LimiteParcial(dado).AchaLimite(2)
Limite3 = limite.LimiteParcial(dado).AchaLimite(3)
Serie = se.Series(dado)
parcial1 = Serie.serieMaxParcial(Limite1)
parcial2 = Serie.serieMaxParcial(Limite2)
parcial3 = Serie.serieMaxParcial(Limite3)
datapa1, vazaopa1 = separaDados(parcial1)
datapa2, vazaopa2 = separaDados(parcial2)
datapa3, vazaopa3 = separaDados(parcial3)
maxAnual = Serie.serieMaxAnual()
dataAn, vazaoAn = separaDados(maxAnual)

#inserir legenda corretamente
plt.plot(data, vazao, 'g-', label = "vazoes diarias")
plt.plot(dataAn, vazaoAn, 'bo', label= 'Maxima')
plt.plot(datapa1, vazaopa1, 'r*', label = 'Parcial')
plt.plot(data, [Limite1 for i in data], 'r-', label = "Limite 1.65")
plt.plot(datapa2, vazaopa2, 'c*', label = 'Parcial')
plt.plot(data, [Limite2 for i in data], 'c-', label = "Limite 2")
plt.plot(datapa3, vazaopa3, 'y*', label = 'Parcial')
plt.plot(data, [Limite3 for i in data], 'y-', label = "Limite 3")

plt.title('Hidrograma')
plt.ylabel('Vazao')
plt.xlabel('Ano')
plt.legend(numpoints = 1, loc = "best")
plt.show()
