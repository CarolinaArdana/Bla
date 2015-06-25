import LimitesString
import StringArquivos

class ListaDados(object):

    def __init__(self, linha = None, ch = None, coluna = 1):
        self.coluna = coluna
        self.ch = ch
        self.linha = linha
        self.listaDados = []

    def Lista(self):

        for i in self.coluna:
            limite = LimitesString.LimitesString(self.linha, self.ch, i)
            limite.linhaV()
            if i == 3:

                data = StringArquivos.StringArquivo(self.linha, limite.indiceInicial+2,
                                                    limite.indiceFinal)
                data.stringLer()
                self.listaDados.append(data.string)
            else:

                dados = StringArquivos.StringArquivo(self.linha, limite.indiceInicial,
                                                     limite.indiceFinal)
                dados.stringLer()
                self.listaDados.append(dados.string)