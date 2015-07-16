class run():
    if __name__ == '__main__':
        import Ana.ListaDadosDB as DadosArq
        import datetime
        import Ana.Datas as Data
        import Ana.InserirDados as inserir
        import Ana.AtualizarDados as atualizar

        c = (2,3,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
             31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
        NomeBD = 'BancoHidro'
        LerANA = DadosArq.LerArquivo(c,'vazoes')
        LerANA.DadosAna()
        anoInicio = LerANA.anoInicio
        anoFim = LerANA.anoFim
        dados = LerANA.dados
        print(dados)
        '''
        listaReducao = ['Mínima', 'Máxima', 'Falha', 'Média']
        listaTipoDePosto = ['Fluviométrico', 'Pluviométrico']
        listaVariavel = ['Precipitação', 'Intercepção', 'Evapotranspiração', 'Infiltração', 'Escoamento']
        listaUnidade = ['m³/s', 'mm', 'l/s']
        listaNivelConstencia = ['Consistido', 'Bruto', 'Bruto e Consistido']
        listaDiscretizacao = ['Dia', 'Mês', 'Ano']
        listaFonte = ['ANA', 'ONS']
        CodigoANA = LerANA.codigo
        Datas = Data.Datas(anoInicio,anoFim)
        Datas.Rdata()

        inserir.inserirDados(listaReducao, NomeBD).Reducao()
        inserir.inserirDados(listaVariavel, NomeBD).Variavel()
        inserir.inserirDados(listaTipoDePosto, NomeBD).Tipo_Posto()
        inserir.inserirDados(listaUnidade, NomeBD).Unidade()
        inserir.inserirDados(listaNivelConstencia, NomeBD).Nivel_Consistencia()
        inserir.inserirDados(listaDiscretizacao, NomeBD).Discretizacao()
        inserir.inserirDados(listaFonte, NomeBD).Fonte()
        inserir.inserirDados(CodigoANA, NomeBD).Posto('Fluviométrico', 'ANA')
        inserir.inserirDados(Datas.ListaDatas, NomeBD).Serie_Temporal()
        '''
        atualizar.atualizaDados(dados, NomeBD).atualizarDadosSerieTemporal()

        #Grava as datas na tabela Serie_Temporal

        '''
        listadados = ListaDadosDB.LerArquivo(c, "vazoesp")
        listadados.DadosAna()
        GravaBanco.GravaBanco(listadados.dados, 'BancoHidro', 'Serie_Temporal').atualizarDados()

        ListaDados = []
        Posto_ID = s.Selecao('BancoHidro').lerPosto(s.Selecao('BancoHidro').lerTipoPosto('Fluviométrico'),
                                                    s.Selecao('BancoHidro').lerFonte('ANA'))
        Arquivo_Fonte_Data = 'ANA ' + str(datetime.datetime.now().year)
        Variavel_ID = s.Selecao('BancoHidro').lerVariavel('Escoamento')
        Tipo_Dado_ID = s.Selecao('BancoHidro').lerNivelConsistencia('Bruto e Consistido')
        Discretizacao_ID = s.Selecao('BancoHidro').lerDiscretizacao('Dia')
        Unidade_ID = s.Selecao('BancoHidro').lerUnidade('m³/s')
        Serie_Temporal_ID = s.Selecao('BancoHidro').lerSerieTemporal()
        ListaDados = [[Posto_ID, Arquivo_Fonte_Data, Variavel_ID, Tipo_Dado_ID, Discretizacao_ID,
                      Unidade_ID,Serie_Temporal_ID]]
        print(ListaDados)
        GravaBanco.GravaBanco(ListaDados, 'BancoHidro', 'Serie_Original').inserirDados()


        ano = anoI_e_anoF.anoI_e_anoF('vazoes.txt')
        ano.anos_I_F()
        listadados = Datas.Datas(ano.anoInicio, ano.anoFim)
        listadados.Rdata()
        GravaBanco.GravaBanco(listadados.ListaDatas,'BancoHidro','Serie_Temporal').inserirDados()
        listadados = DadosArq.LerArquivo(nome_arq="xingo")
        listadados.DadosOns()
        GravaBanco.GravaBanco(listadados.dados, 'BancoHidro', 'Serie_Temporal').atualizarDados()

        ListaDados = []
        Posto_ID = selecao.Selecao('BancoHidro').lerPosto(selecao.Selecao('BancoHidro').lerTipoPosto('Fluviométrico'),
                                                    selecao.Selecao('BancoHidro').lerFonte('ONS'))
        Arquivo_Fonte_Data = 'ONS ' + str(datetime.datetime.now().year)
        Variavel_ID = selecao.Selecao('BancoHidro').lerVariavel('Escoamento')
        Tipo_Dado_ID = selecao.Selecao('BancoHidro').lerNivelConsistencia('Bruto')
        Discretizacao_ID = selecao.Selecao('BancoHidro').lerDiscretizacao('Dia')
        Unidade_ID = selecao.Selecao('BancoHidro').lerUnidade('m³/s')
        Serie_Temporal_ID = selecao.Selecao('BancoHidro').lerSerieTemporal()
        ListaDados = [[Posto_ID, Arquivo_Fonte_Data, Variavel_ID, Tipo_Dado_ID, Discretizacao_ID,
                      Unidade_ID,Serie_Temporal_ID]]
        print(ListaDados)

        GravaBanco.GravaBanco(ListaDados, 'BancoHidro', 'Serie_Original').inserirDados()
        '''