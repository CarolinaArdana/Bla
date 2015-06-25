import sqlite3

#Criando e Conectando-se com o banco
conn = sqlite3.connect('Banco_Hidro.db')
#Cursor do banco
cursor = conn.cursor()

#Tabela Posto
cursor.execute("""
CREATE TABLE Posto(
    Posto_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Tipo_Posto_ID INTEGER NOT NULL,
    Fonte_ID INTEGER NOT NULL,
    Codigo_Ana VARCHAR(20) NULL,
    FOREIGN KEY(Tipo_Posto_ID) REFERENCES Tipo_Posto(Tipo_Posto_ID),
    FOREIGN KEY(Fonte_ID) REFERENCES Fonte(Fonte_ID)
);
""")

#Tabela Tipo Posto
cursor.execute("""
CREATE TABLE Tipo_Posto(
    Tipo_Posto_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Tipo VARCHAR(20) NOT NULL
    );
""")

#Tabela Fonte
cursor.execute("""
CREATE TABLE Fonte(
    Fonte_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Fonte VARCHAR(20) NOT NULL
);
""")
#Tabela Variavel
cursor.execute("""
CREATE TABLE Variavel(
    Variavel_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Variavel VARCHAR(20) NOT NULL
);
""")
#Tabela Unidade
cursor.execute("""
CREATE TABLE Unidade(
    Unidade_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Tipo VARCHAR(20) NOT NULL
);
""")
#Tabela Nivel de Consistência
cursor.execute("""
CREATE TABLE Nivel_Consistencia(
    Tipo_Dados_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nivel VARCHAR(20) NOT NULL
);
""")
#Tabela de Discretização
cursor.execute("""
CREATE TABLE Discretizacao(
    Discretização_ID  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Tipo VARCHAR(20) NOT NULL
);
""")
#Tabela Série Temporal
cursor.execute("""
CREATE TABLE Serie_Temporal(
    Serie_Temporal_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Data_e_Hora VARCHAR(20) NOT NULL,
    Dado VARCHAR(20) NOT NULL
);
""")
#Tabela Redução
cursor.execute("""
CREATE TABLE Reducao(
    Reducao_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Tipo VARCHAR(20) NOT NULL
);
""")
#Tabela Série Origial
cursor.execute("""
CREATE TABLE Serie_Original(
    Serie_Original_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Posto_ID INTEGER NOT NULL,
    Arquivo_Fonte_Data VARCHAR(20) NOT NULL,
    Variavel_ID INTEGER NOT NULL,
    Tipo_Dado_ID INTEGER NOT NULL,
    Discretizacao_ID INTEGER NOT NULL,
    Unidade_ID INTEGER NOT NULL,
    Serie_Temporal_ID INTEGER NOT NULL,
    FOREIGN KEY(Posto_ID) REFERENCES Tipo_Posto(Posto_ID),
    FOREIGN KEY(Variavel_ID) REFERENCES Variavel(Variavel_ID),
    FOREIGN KEY(Tipo_Dado_ID) REFERENCES Nivel_Consistencia(Tipo_Dado_ID),
    FOREIGN KEY(Discretizacao_ID) REFERENCES Discretizacao(Discretizacao_ID),
    FOREIGN KEY(Unidade_ID) REFERENCES Unidade(Unidade_ID),
    FOREIGN KEY(Serie_Temporal_ID) REFERENCES Serie_Temporal(Serie_Temporal_ID)
);
""")
#Tabela Série Reduzida
cursor.execute("""
CREATE TABLE Serie_Reduzida(
    Serie_Reduzida_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Serie_Original_ID INTEGER NOT NULL,
    Discretizacao_ID INTEGER NOT NULL,
    Reducao_ID INTEGER NOT NULL,
    Serie_Temporal_ID INTEGER NOT NULL,
    FOREIGN KEY(Serie_Original_ID) REFERENCES Serie_Original(Serie_Original_ID),
    FOREIGN KEY(Discretizacao_ID) REFERENCES Discretizacao(Discretizacao_ID),
    FOREIGN KEY(Reducao_ID) REFERENCES Reducao(Reducao_ID),
    FOREIGN KEY(Serie_Temporal_ID) REFERENCES Serie_Temporal(Serie_Temporal_ID)
);
""")

print('Banco criando com sucesso!')
#Fechando Conexão
cursor.close()