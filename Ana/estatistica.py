from scipy.stats import genpareto, genextreme
import Ana.LimiteParcial as lp
import Ana.Series as se

class estatistica(object):
    def __init__(self, dadoSerie, tipoSerie):
        self.dadoSerie = dadoSerie
        self.tipoSerie = tipoSerie

    def CalculaParametros(self):

        if self.tipoSerie == 'Parcial':
            #Achando o valor limiar:
            limite = lp.LimiteParcial(self.dadoSerie).AchaLimite(2)
            print(limite)
            Parciais = se.Series(self.dadoSerie).serieMaxParcial(limite)
            datasP, PicosParciais = se.Series(Parciais).separaDados()
            Parametro = genpareto.fit(PicosParciais)
            print('Parametros com Pareto: \nForma: %.f, Localidade: %f, Escala: %f' %
                  (Parametro[0],Parametro[1],Parametro[2]))
            return  Parametro
        elif self.tipoSerie == 'Anual':
            Anuais = se.Series(self.dadoSerie).serieMaxAnual()
            datasA, PicosAnuais = se.Series(Anuais).separaDados()
            Parametro = genextreme.fit(PicosAnuais)
            print('Parametros com Gev: \nForma: %.f, Localidade: %f, Escala: %f' %
                  (Parametro[0],Parametro[1],Parametro[2]))
            return Parametro

    def EstimaMagnitudes(self, Parametros):
        Quantis = []
        TRs = [1.000111,2,5,10,20,50]
        for TR in TRs:
            if self.tipoSerie == 'Parcial':
                Quantil = genpareto.ppf(1-(1/TR), Parametros[0],
                                        loc = Parametros[1],
                                        scale = Parametros[2])
                Quantis.append(Quantil)
                print('Tempo de Retorno: %i  '%TR)
                print('PARETO=> Magnitude: %.2f'%(Quantil))
            elif self.tipoSerie == 'Anual':
                Quantil = genextreme.ppf(1-(1/TR), Parametros[0],
                                         loc = Parametros[1],
                                         scale = Parametros[2])
                Quantis.append(Quantil)
                print('Tempo de Retorno: %i  '%TR)
                print('GEV=> Magnitude: %.2f' % (Quantil))

        return Quantis

    def EstimaFrequencias(self, Parametros):
        if self.tipoSerie == 'Parcial':
            limite = lp.LimiteParcial(self.dadoSerie).AchaLimite(2)
            Parciais = se.Series(self.dadoSerie).serieMaxParcial(limite)
            datasP, PicosParciais = se.Series(Parciais).separaDados()
            PicosParciais.sort(reverse = True)
            print(PicosParciais)
            frequencias = genpareto.cdf(PicosParciais, Parametros[0],
                                        loc = Parametros[1],
                                        scale = Parametros[2])

        elif self.tipoSerie == 'Anual':
            Anuais = se.Series(self.dadoSerie).serieMaxAnual()
            datasA, PicosAnuais = se.Series(Anuais).separaDados()
            PicosAnuais.sort(reverse = True)
            print(PicosAnuais)
            frequencias = genextreme.cdf(PicosAnuais, Parametros[0],
                                            loc = Parametros[1],
                                            scale = Parametros[2])
        return frequencias
