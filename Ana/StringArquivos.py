class StringArquivo(object):
    def __init__(self, linha = None, inicioString = None, fimString = None):
        self.linha = linha
        self.inicioString = inicioString
        self.fimString = fimString
        self.string = None

    def stringLer(self):
        self.string = str(self.linha[self.inicioString : self.fimString])