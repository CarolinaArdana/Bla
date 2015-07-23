import datetime
import SelecaoRegistro

class Series(object):
    def __init__(self):
            self.ListaMaxAnual = []
            self.ListaMaxMensal = []
            self.dic = {}

    def maxAnual(self, nome_db, fonte, anoInicio = 1931, anoFinal = 2014):
        vazao = []
        auxA = anoInicio
        s = SelecaoRegistro.Selecao(nome_db).lerSerieTemporalDados(fonte, anoInicio, anoFinal)
        for ano in range(anoInicio, anoFinal+1):
            for i in s:
                if int(i[1][6:10]) == ano:
                    vazao.append(float(i[2]))
            self.dic[ano] = vazao
        print(self.dic)

    '''
            ano = int(i[1][6:10])
            if ano == auxA:
                vazao.append(float(i[2]))
            else:
                self.dic[auxA] = vazao
                vazao = []
                vazao.append(float(i[2]))
                auxA = ano
            self.dic[auxA]= vazao
        listano = list(self.dic.keys())
        listano.sort()
        for i in listano:
            l = list(self.dic[i])
            maxi = max(self.dic[i])
            indice = l.index(maxi)
            data = (datetime.datetime(i,1,1, 9,00) +
                    datetime.timedelta(indice)).strftime('%d/%m/%Y %H:%M')
            self.ListaMaxAnual.append([data, maxi])
    '''

    def maxMensal(self, nome_db, SerieTemporalID):
        s = SelecaoRegistro.Selecao(nome_db).lerSerieTemporalDados(SerieTemporalID)
        auxDic = {}
        vazao = []
        auxA = 1931
        auxM = 1
        for i in s:
            ano = int(i[1][6:10])
            mes = int(i[1][3:5])
            if mes == auxM:
                vazao.append(float(i[2]))
            else:
                auxDic[auxM] = vazao
                vazao = []
                vazao.append(float(i[2]))
                auxM = mes

            if ano != auxA:
                auxA = ano
                self.dic[auxA-1] = auxDic
                auxDic = {}
            auxDic[12] = vazao
            self.dic[auxA] = auxDic

        listano = list(self.dic.keys())
        listano.sort()
        for i in listano:
            listames = list(self.dic[i].keys())
            for j in listames:
                l = list(self.dic[i][j])
                dia = l.index(max(self.dic[i][j]))
                data = datetime.datetime(i, j, dia+1, 9, 00).strftime('%d/%m/%Y %H:%M')
                self.ListaMaxMensal.append([data, max(self.dic[i][j])])


s = Series()
s.maxAnual('BancoHidro', 1)
