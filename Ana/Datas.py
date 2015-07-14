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
        for i in lista:
            data = (datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S').
                    date().strftime('%Y/%m/%d'))
            ano, mes, dia = data.split('/')
            self.ListaDatas.append(['-9999.9', datetime.datetime(int(ano),int(mes),int(dia),9,00).
                                   strftime('%d/%m/%Y %H:%M')])