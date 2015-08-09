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

    def mesInicioAnoHidrologico(self):
        ano = s.Selecao(self.nome_db).lerSerieTemporalDados(self.TemporalID)
        dic = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
        for i in ano:
            for j in dic:
                if j == int(i[1][3:5]):
                    dic[j].append(float(i[2]))
        for i in dic:
            dic[i] = sum(dic[i])/len(dic[i])

        Lista = (list(dic.values()))
        mes = Lista.index(min(Lista))+1
        return mes

    def anoHidrologico(self):
        print(self.mesInicioAnoHidrologico())
        mesInicio = int(input('Mês Inicio Ano Hidrológico'))
        datas = []
        for i in range(self.anoInicioSerie, self.anoFinalSerie):
            anoinicio = i
            inicio = datetime.datetime(anoinicio,mesInicio,1)
            if ((anoinicio+1)%4) == 0: dias = 365
            else: dias = 364
            fim = inicio + relativedelta(days=+dias)

            for i in p.date_range(inicio,fim):
                data = (datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S').
                            date().strftime('%Y/%m/%d'))
                aano, ames, adia = data.split('/')

                datas.append(datetime.datetime(int(aano),int(ames),int(adia),9,00).
                                           strftime('%d/%m/%Y %H:%M'))

        return datas

    def AnoCivil(self):
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
        return datas
'''
a = Ano('BancoHidro', 1, 1980, 2014)
for i in a.anoHidrologico():
    print(i)
'''