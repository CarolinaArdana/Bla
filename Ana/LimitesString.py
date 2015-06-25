class LimitesString(object):

    def __init__(self, linha = None, ch = None, coluna = 1):
        self.linha = linha
        self.ch = ch
        self.coluna = coluna
        self.indiceInicial = 1
        self.indiceFinal = 0


    def linhaV(self):
        cont = 0
        for i in self.linha:
            if i == self.ch:
                cont += 1
                if cont == self.coluna:
                    break
            if cont < self.coluna-1:
                self.indiceInicial += 1
            if cont <= self.coluna:
                self.indiceFinal += 1

