class run():
    if __name__ == '__main__':
        import ListaDadosDB
        import Datas
        import anoI_e_anoF
        import GravaBanco
        import SelecaoRegistro as s
        import conectando_db as conn
        c = (2,3,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
             31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
        '''
        listaReducao = ['Mínima', 'Máxima', 'Falha', 'Média']
        listaVariavel = ['Precipitação', 'Intercepção', 'Evapotranspiração', 'Infiltração', 'Escoamento']
        listaTipoDePosto = ['Fluviométrico', 'Pluviométrico']
        listaUnidade = ['m³/s', 'mm', 'l/s']
        listaNivelConstencia = ['Consistido', 'Bruto', 'Bruto e Consistido']
        listaDiscretizacao = ['Dia', 'Mês', 'Ano']
        listaFonte = ['ANA', 'ONS']
        listaDados = {
            'Reducao': listaReducao,
            'Variavel': listaVariavel,
            'Tipo_Posto': listaTipoDePosto,
            'Unidade': listaUnidade,
            'Nivel_Consistencia': listaNivelConstencia,
            'Discretizacao': listaDiscretizacao,
            'Fonte': listaFonte}
        for i in listaDados:
            GravaBanco.GravaBanco(listaDados[i],'BancoHidro',i).inserirDados()

        #Grava as datas na tabela Serie_Temporal
        ano = anoI_e_anoF.anoI_e_anoF('vazoes.txt')
        ano.anos_I_F()
        listadados = Datas.Datas(ano.anoInicio, ano.anoFim)
        listadados.Rdata()


        #Atualiza os dados na tabela Serie_Temporal
        listadados = ListaDadosDB.LerArquivo(c, "vazoes")
        listadados.DadosAna()
        GravaBanco.GravaBanco(listadados.dados, 'BancoHidro', 'Serie_Temporal').atualizarDados()
        listadados = ListaDadosDB.LerArquivo(nome_arq="xingo")
        listadados.DadosOns()
        GravaBanco.GravaBanco(listadados.dados, 'BancoHidro', 'Serie_Temporal').atualizarDados()

        listaDados = []
        Tipo_Posto_ID = s.Selecao('BancoHidro').lerTipoPosto('Fluviométrico')
        Fonte_ID = s.Selecao('BancoHidro').lerFonte('ANA')
        Codigo_ANA = ListaDadosDB.LerArquivo(c,'vazoes')
        Codigo_ANA.DadosAna()
        listaPosto = [Tipo_Posto_ID, Fonte_ID, Codigo_ANA.codigo]
        listaDados.append(listaPosto)
        Tipo_Posto_ID = s.Selecao('BancoHidro').lerTipoPosto('Fluviométrico')
        Fonte_ID = s.Selecao('BancoHidro').lerFonte('ONS')
        listaPosto = [Tipo_Posto_ID, Fonte_ID, -9999]
        listaDados.append(listaPosto)
        GravaBanco.GravaBanco(listaDados, 'BancoHidro', 'Posto').inserirDados()
        '''