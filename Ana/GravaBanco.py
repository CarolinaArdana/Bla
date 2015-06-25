import InserirDados
import AtualizarDados

class GravaBanco(object):

    def __init__(self, dados, nome_db, nome_tb):
        self.dados = dados
        self.nome_tb = nome_tb
        self.nome_db = nome_db

    def inserirDados(self):
        if self.nome_tb == 'Serie_Temporal':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirSerieTemporal()
        elif self.nome_tb == 'Posto':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirPosto()
        elif self.nome_tb == 'Reducao':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirReducao()
        elif self.nome_tb == 'Fonte':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirFonte()
        elif self.nome_tb == 'Discretizacao':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirDiscretizacao()
        elif self.nome_tb == 'Serie_Original':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirSerieOriginal()
        elif self.nome_tb == 'Tipo_Posto':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirTipoPosto()
        elif self.nome_tb == 'Unidade':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirUnidade()
        elif self.nome_tb == 'Variavel':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirVariavel()
        elif self.nome_tb == 'Serie_Reduzida':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirSerieReduzida()
        elif self.nome_tb == 'Nivel_Consistencia':
            InserirDados.inserirDados(self.dados, self.nome_db).inserirNivelConsistencia()

    def atualizarDados(self):
        if self.nome_tb == 'Serie_Temporal':
            AtualizarDados.atualizaDados(self.dados, self.nome_db).atualizarDadosSerieTemporal()