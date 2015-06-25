import Lista
import InserirDados
import datetime
class LerArquivo(object):
    def __init__(self, coluna = None, nome_arq = None):
        self.coluna = coluna
        self.cont = 0
        self.nome_arq = nome_arq
        self.arquivo = open('%s.txt' % self.nome_arq, 'r')
        self.ins_db = InserirDados
        self.dia = 0
        self.mes = None
        self.ano = None
        self.data = None
        self.consistencia = []
        self.codigo = None
        self.vazao = None
        self.ListaDatas = []
        self.dados = []

    def DadosAna(self):
        for linha in self.arquivo.readlines():
            self.cont += 1
            self.dia = 0
            ListaLinha = Lista.ListaDados(linha, ';', self.coluna)
            ListaLinha.Lista()
            if self.cont == 13:
                self.codigo = linha[linha.index(':')+2:-1]
            elif self.cont > 17:
                for k in range(2,len(ListaLinha.listaDados)):
                    try:
                        self.dia += 1
                        self.mes = int(ListaLinha.listaDados[1][1:3])
                        self.ano = int(ListaLinha.listaDados[1][4:8])
                        self.data = datetime.datetime(self.ano,
                                                      self.mes,
                                                      self.dia,
                                                      9,
                                                      00).strftime('%d/%m/%Y %H:%M')
                        if ListaLinha.listaDados[0] == '1':
                            cons = 'Bruto'
                        elif ListaLinha.listaDados[0] == '2':
                            cons = 'Consistido'

                        if ListaLinha.listaDados[k] != '':
                            self.vazao = ListaLinha.listaDados[k]
                        else:
                            self.vazao = '-9999,9'
                        self.consistencia.append([cons, self.data])
                        self.dados.append([self.vazao.replace(',','.'), self.data])
                    except ValueError:
                        break

        self.arquivo.close()

    def DadosOns(self):
        for linha in self.arquivo.readlines():
            data, vazao = linha.split(';')
            self.dia = int(data[0:2])
            self.mes = int(data[3:5])
            self.ano = int(data[6:12])
            self.vazao = vazao[0:-1]
            self.data = datetime.datetime(self.ano,
                                          self.mes,
                                          self.dia,
                                          12, 00).strftime('%d/%m/%Y %H:%M')
            self.dados.append([self.vazao, self.data])
            self.consistencia.append([1, self.data])
        self.arquivo.close()

