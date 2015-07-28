import Ana.SelecaoRegistro as s
import pandas as p
import datetime
from dateutil.relativedelta import relativedelta
class Ano(object):
    def __init__(self, nome_db, TemporalID, anoInicioSerie, anoFinalSerie):
        self.nome_db = nome_db
        self.TemporalID = TemporalID
        self.anoInicioSerie = anoInicioSerie
        self.anoFinalSerie = anoFinalSerie

    def anoHidrologico(self):
        ano = s.Selecao(self.nome_db).lerSerieTemporalDados(self.TemporalID)
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
            anoinicio = i
            inicio = datetime.datetime(anoinicio,mes,1)
            if ((anoinicio+1)%4) == 0: dias = 365
            else: dias = 364
            fim = inicio + relativedelta(days=+dias)

            for i in p.date_range(inicio,fim):
                data = (datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S').
                            date().strftime('%Y/%m/%d'))
                aano, ames, adia = data.split('/')

                datas.append(datetime.datetime(int(aano),int(ames),int(adia),9,00).
                                           strftime('%d/%m/%Y %H:%M'))
                anosHid[anoinicio] = datas
            datas = []
        return anosHid


    def AnoCivil(self):
        anosCivil = {}
        datas = []
        for i in range(self.anoInicioSerie, self.anoFinalSerie+1):
            anoinicio = i
            inicio = datetime.datetime(anoinicio,1,1)
            if ((anoinicio)%4) == 0: dias = 365
            else: dias = 364
            fim = inicio + relativedelta(days=+dias)

            for i in p.date_range(inicio,fim):
                data = (datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S').
                            date().strftime('%Y/%m/%d'))
                aano, ames, adia = data.split('/')

                datas.append(datetime.datetime(int(aano),int(ames),int(adia),9,00).
                                           strftime('%d/%m/%Y %H:%M'))
                anosCivil[anoinicio] = datas
            datas = []
        return anosCivil
'''
a = Ano('BancoHidro', 1, 1999, 2014)

for i in a.AnoCivil().items():
    print(i)
'''