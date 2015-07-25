CREATE TABLE Serie_Temporal(
    Serie_Temporal_ID INTEGER NOT NULL,
    Data_e_Hora DATETIME NOT NULL,
    Dado VARCHAR(20) NULL,
    PRIMARY KEY (Serie_Temporal_ID, Data_e_Hora)
);