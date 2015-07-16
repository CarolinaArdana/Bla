import LimitesString
import StringArquivos
class anoI_e_anoF(object):
    def __init__(self):
        self.anoInicio = 3000
        self.anoFim = 1900
        self.cont = 0

    def anos_I_F(self):

        for linha in self.arquivo.readlines():
            self.cont += 1
            limite = LimitesString.LimitesString(linha, ';', 3)
            limite.linhaV()
            anoString = StringArquivos.StringArquivo(linha, limite.indiceInicial+6,limite.indiceFinal)
            anoString.stringLer()

            if self.cont > 17:
                if self.anoInicio >= int(anoString.string):
                    self.anoInicio = int(anoString.string)
                if self.anoFim <= int(anoString.string):
                    self.anoFim = int(anoString.string)

        self.arquivo.close()