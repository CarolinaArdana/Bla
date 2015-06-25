import datetime
import pandas
class Datas():

    def __init__(self, anoInicio = 1931, anoFim = 2014, fonte = None):
        self.ListaDatas = []
        self.anoInicio = anoInicio
        self.anoFim = anoFim
        self.data = None
        self.dia = 0
        self.fonte = fonte

    def Rdata(self):
        dataInicio = datetime.datetime(self.anoInicio,1,1)
        dataFim = datetime.datetime(self.anoFim,12,31)

        lista = pandas.date_range(dataInicio, dataFim)
        if self.fonte == 'ANA':
            for i in lista:
                data = (datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S').
                        date().strftime('%Y/%m/%d'))
                ano, mes, dia = data.split('/')
                self.ListaDatas.append(['-9999.9', datetime.datetime(int(ano),int(mes),int(dia),9,00).
                                       strftime('%d/%m/%Y %H:%M')])
        elif self.fonte == 'ONS':
            for i in lista:
                data = (datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S').
                        date().strftime('%Y/%m/%d'))
                ano, mes, dia = data.split('/')
                self.ListaDatas.append(['-9999.9', datetime.datetime(int(ano),int(mes),int(dia),12,00).
                                       strftime('%d/%m/%Y %H:%M')])
        else:
            lista = Datas(self.anoInicio, self.anoFim,'ANA')
            lista.Rdata()
            ana = lista.ListaDatas
            lista = Datas(self.anoInicio, self.anoFim,'ONS')
            lista.Rdata()
            ons = lista.ListaDatas

            for i in ana:
                self.ListaDatas.append(i)
            for x in ons:
                self.ListaDatas.append(x)