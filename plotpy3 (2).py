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
dados = da.DadosVazao('F:\\Clebson\\HidroComp\\Ana\\BancoHidro','Hidrologico', 1, 1931, 2014)
dado = dados.Dados()
data,vazao = separaDados(dado)
Limite = limite.LimiteParcial(dado).AchaLimite(2)
Serie = se.Series(dado)
parcial = Serie.serieMaxParcial(Limite)
maxAnual = Serie.serieMaxAnual()
datapa, vazaopa = separaDados(parcial)
dataAn, vazaoAn = separaDados(maxAnual)

#inserir legenda corretamente
plt.plot(data, vazao, 'g-', label = "vazoes diarias")
plt.plot(dataAn, vazaoAn, 'bo', label= 'Maxima')
plt.plot(datapa, vazaopa, 'r*', label = 'Parcial')
plt.plot(data, [Limite for i in data], 'k-', label = "Limite")


plt.title('Hidrograma - Ano Hidrologico')
plt.ylabel('Vazao')
plt.xlabel('Ano')
plt.grid(b=True, which='both', color='k',linestyle='-')
plt.legend(numpoints = 1, loc = "best")
plt.show()
