import Ana.SelecaoRegistro as s
import pandas as p
import datetime
class Ano(object):
    def __init__(self, nome_db, anoInicioSerie, anoFinalSerie):
        self.nome_db = nome_db
        self.anoInicioSerie = anoInicioSerie
        self.anoFinalSerie = anoFinalSerie

    def anoHidrologico(self):
        ano = s.Selecao(self.nome_db).lerSerieTemporalDados(1)
        dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        for i in ano:
            for j in dic:
                if j == int(i[1][3:5]):
                    dic[j] += float(i[2])

        Lista = (list(dic.values()))
        mes = Lista.index(min(Lista))+1
        anosHid = {}
        datas = []
        for i in range(self.anoInicioSerie, self.anoFinalSerie):
            anoinico = i
            anofim = i+1
            inicio = datetime.datetime(anoinico,mes,1)
            fim = datetime.datetime(anofim,mes-1,31)
            for i in p.date_range(inicio,fim):
                data = (datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S').
                            date().strftime('%Y/%m/%d'))
                aano, ames, adia = data.split('/')

                datas.append(datetime.datetime(int(aano),int(ames),int(adia),9,00).
                                           strftime('%d/%m/%Y %H:%M'))
                anosHid[anoinico] = datas
            datas = []
        return anosHid


    def AnoCivil(self):
        anosCivil = {}
        datas = []
        for i in range(self.anoInicioSerie, self.anoFinalSerie+1):
            ano = i
            inicio = datetime.datetime(ano,1,1)
            fim = datetime.datetime(ano,12,31)
            for i in p.date_range(inicio,fim):
                data = (datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S').
                            date().strftime('%Y/%m/%d'))
                aano, ames, adia = data.split('/')

                datas.append(datetime.datetime(int(aano),int(ames),int(adia),9,00).
                                           strftime('%d/%m/%Y %H:%M'))
                anosCivil[ano] = datas
            datas = []
        return anosCivil

'''
a = Ano('BancoHidro',1931,2014)
for i in a.AnoCivil().items():
    print(i)
'''