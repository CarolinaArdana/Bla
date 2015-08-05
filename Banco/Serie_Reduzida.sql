CREATE TABLE Serie_Reduzida(
    Serie_Reduzida_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Serie_Original_ID INTEGER NOT NULL,
    Discretizacao_ID INTEGER NOT NULL,
    Reducao_ID INTEGER NOT NULL,
    Serie_Temporal_ID INTEGER NOT NULL,
    Parcial_Mi FLOAT NULL,
    Parcial_U INTEGER NULL,
    FOREIGN KEY(Serie_Original_ID) REFERENCES Serie_Original(Serie_Original_ID),
    FOREIGN KEY(Discretizacao_ID) REFERENCES Discretizacao(Discretizacao_ID),
    FOREIGN KEY(Reducao_ID) REFERENCES Reducao(Reducao_ID),
    FOREIGN KEY(Serie_Temporal_ID) REFERENCES Serie_Temporal(Serie_Temporal_ID)
);