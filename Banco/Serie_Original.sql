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
    FOREIGN KEY(Serie_Temporal_ID) REFERENCES Serie_Tempora(Serie_Temporal_ID)
);