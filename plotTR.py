from datetime import date
import matplotlib.pyplot as plt
import Ana.DadosVazaoDB as da
import Ana.estatistica as est
import Ana.Series as se
import Ana.LimiteParcial as lp
dados = da.DadosVazao('F:\\Clebson\\HidroComp\\Ana\\BancoHidro', 3, 1978, 2014)
dado = dados.Dados()
dadAn = se.Series(dado).serieMaxAnual()
dadpa = se.Series(dado).serieMaxParcial(lp.LimiteParcial(dado).AchaLimite(2))
datapa, parc = se.Series(dadpa).separaDados()
data, anual = se.Series(dadAn).separaDados()
estat = est.estatistica(dado, 'Parcial')
para = estat.CalculaParametros()
mag = estat.EstimaMagnitudes(para)
fre = estat.EstimaFrequencias(para)
estatAn = est.estatistica(dado, 'Anual')
paraAn = estatAn.CalculaParametros()
magAn = estatAn.EstimaMagnitudes(paraAn)
freAn = estatAn.EstimaFrequencias(paraAn)

pro = [1 - i for i in fre]
tr = [1/i for i in pro]
tr1 = [1/i for i in freAn]
print(tr)
anual.sort(reverse = True)
parc.sort(reverse = True)
tr1.sort(reverse=True)
print(tr1)
plt.plot(tr, parc, 'bo')
plt.plot(tr1, anual, 'r*')
plt.show()