import Ana.DadosVazaoDB as se

class LimiteParcial(object):
    def __init__(self, dados):
        self.dados = dados

    def NPicos(self, limite, vetor):
        qt=0
        aux = 0
        aux2 = 0
        for i in vetor:
            if i > limite:
                aux += 1
                aux2 = 1
            elif aux2 == 1 and aux > 0:
                qt+=1
                aux2 = 0
        return qt

    def AchaLimite(self, mediaPorAno):
        vetor = []
        vetor2 = []
        data = []
        print(self.dados)
        for i in self.dados:
            vetor.append(float(i[1]))
            vetor2.append(float(i[1]))
            data.append(i[0][0:10])
        #Anos da Série
        dataInicio = int(data[0][6:10])
        dataFinal = int(data[-1][6:10])
        qtAnos = dataFinal - dataInicio - 1
        limite = max(vetor) - 1
        for i in vetor2:
            qt = self.NPicos(limite, vetor2)
            vetor.remove(max(vetor))
            limite = max(vetor)
            if qt >= mediaPorAno*qtAnos:
                break

        return limite
'''
dados = se.DadosVazao('BancoHidro','Hidrologico', 1, 1980, 2014)
a = LimiteParcial(dados.Dados())
print(a.AchaLimite(2))
'''