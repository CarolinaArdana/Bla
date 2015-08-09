import Ana.ListaDadosDB as DadosArq
import datetime
import Ana.Datas as Data
import Ana.InserirDados as inserir
import Ana.AtualizarDados as atualizar
import Ana.DadosVazaoDB as da
import Ana.LimiteParcial as li
class run():
    def __init__(self, NomeBD):
        self.NomeBD = NomeBD
        self.Fonte = None
        self.dados = None
        self.CodigoANA = None
        self.DatasSerie = None
        self.Tipo_Posto = None

    def getDados(self, NomeArquivo, Fonte, Tipo_Posto, Variavel, Tipo_Dados, Unidade, Discretizacao_Orig, Discretizacao_Red, Reducao,
                 mediaPorAno = None, limite = None):
        c = (2,3,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
         31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
        LerANA = DadosArq.LerArquivo(c,NomeArquivo)
        if Fonte == 'ONS':
            LerANA.DadosOns()
        elif Fonte == 'ANA':
            LerANA.DadosAna()
        elif Fonte == 'CHESF':
            LerANA.DadosOns()

        anoInicio = LerANA.anoInicio
        anoFim = LerANA.anoFim
        Datas = Data.Datas(anoInicio,anoFim)
        Datas.Rdata()
        self.Tipo_Posto = Tipo_Posto
        self.Fonte = Fonte
        self.Variavel = Variavel
        self.Tipo_Dados = Tipo_Dados
        self.Unidade = Unidade
        self.Discretizacao_Orig = Discretizacao_Orig
        self.Discretizacao_Red = Discretizacao_Red
        self.Reducao = Reducao
        self.Arquivo_Fonte_Data = '%s - %s' % (self.Fonte, datetime.datetime.now().date().strftime('%d/%m/%Y'))
        self.dados = LerANA.dados
        self.CodigoANA = LerANA.codigo
        self.DatasSerie = Datas.ListaDatas

get = run('BancoHidro')
get.getDados('Xingoreal', 'CHESF', 'Fluviométrico', 'Escoamento', 'Consistido', 'm³/s', 'Dia', 'Ano', 'Máxima')
'''
listaReducao = ['Mínima', 'Máxima', 'Falha', 'Média', 'Parcial']
listaTipoDePosto = ['Fluviométrico', 'Pluviométrico']
listaVariavel = ['Precipitação', 'Intercepção', 'Evapotranspiração', 'Infiltração', 'Escoamento']
listaUnidade = ['m³/s', 'mm', 'l/s']
listaNivelConstencia = ['Consistido', 'Bruto', 'Bruto e Consistido']
listaDiscretizacao = ['Dia', 'Mês', 'Ano']

inserir.inserirDados(get.NomeBD, listaReducao).Reducao()
inserir.inserirDados(get.NomeBD, listaVariavel).Variavel()
inserir.inserirDados(get.NomeBD, listaTipoDePosto).Tipo_Posto()
inserir.inserirDados(get.NomeBD, listaUnidade).Unidade()
inserir.inserirDados(get.NomeBD, listaNivelConstencia).Nivel_Consistencia()
inserir.inserirDados(get.NomeBD, listaDiscretizacao).Discretizacao()

inserir.inserirDados(get.NomeBD, get.Fonte).Fonte(get.Fonte)
inserir.inserirDados(get.NomeBD, get.CodigoANA).Posto(get.Tipo_Posto, get.Fonte)
inserir.inserirDados(get.NomeBD, get.DatasSerie).Serie_Temporal()
atualizar.atualizaDados(get.NomeBD, get.dados).atualizarDadosSerieTemporal()
inserir.inserirDados(get.NomeBD).Serie_Original(get.Fonte, get.CodigoANA, get.Arquivo_Fonte_Data,
                                                get.Variavel, get.Tipo_Dados, get.Discretizacao_Orig,
                                                get.Unidade)
'''
get = run('BancoHidro')
get.getDados('Xingoreal', 'CHESF', 'Fluviométrico', 'Escoamento', 'Consistido', 'm³/s', 'Dia', 'Ano', 'Parcial')
for i in [1.65, 2, 3]:
    dados = da.DadosVazao('BancoHidro',2,1995,2009).Dados()
    parcial_Mi = i
    parcial_U = li.LimiteParcial(dados).AchaLimite(parcial_Mi)
    inserir.inserirDados(get.NomeBD).Serie_Reduzida(get.Fonte, get.CodigoANA, get.Arquivo_Fonte_Data,
                                                    get.Variavel, get.Tipo_Dados, get.Discretizacao_Orig,
                                                    get.Unidade, get.Discretizacao_Red, get.Reducao,
                                                    parcial_Mi, parcial_U)
get = run('BancoHidro')
get.getDados('Xingoreal', 'CHESF', 'Fluviométrico', 'Escoamento', 'Consistido', 'm³/s', 'Dia', 'Ano', 'Máxima')
inserir.inserirDados(get.NomeBD).Serie_Reduzida(get.Fonte, get.CodigoANA, get.Arquivo_Fonte_Data,
                                                    get.Variavel, get.Tipo_Dados, get.Discretizacao_Orig,
                                                    get.Unidade, get.Discretizacao_Red, get.Reducao)