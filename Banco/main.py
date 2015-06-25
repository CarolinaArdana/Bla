if __name__ == '__main__':

    import CriarTabela
    c = CriarTabela

    lista = ['Posto',
             'Tipo_Posto',
             'Fonte',
             'Variavel',
             'Unidade',
             'Nivel_Consistencia',
             'Discretizacao',
             'Serie_Original',
             'Serie_Temporal',
             'Serie_Reduzida',
             'Reducao']
    for i in lista:
        c.Tabela(i).criar_tabelas()
