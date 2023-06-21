DROP TABLE IF EXISTS solicitante CASCADE;
DROP TABLE IF EXISTS pagamento CASCADE;
DROP TABLE IF EXISTS protocolo CASCADE;
DROP TABLE IF EXISTS certidao CASCADE;
CREATE TABLE solicitante (
    cpf_cnpj Varchar(20),
    nome Varchar(60),
    PRIMARY KEY (cpf_cnpj)
);
CREATE TABLE pagamento (
    idpix Serial,
    cpf_cnpj Varchar(20),
    valor Numeric(12,2) NOT NULL,
    createdby Varchar(8) NOT NULL,
    createdat Timestamp NOT NULL,
    updatedby Varchar(8),
    updatedat Timestamp,
    status Varchar(12) NOT NULL,
    txtid Varchar(37),
    pixcopiacola varchar(250),
    PRIMARY KEY (idpix),
    FOREIGN KEY (cpf_cnpj) REFERENCES solicitante(cpf_cnpj) ON DELETE CASCADE
);
CREATE TABLE protocolo (
    idprot Serial,
    num INTEGER,
    idpix INT NOT NULL,
    PRIMARY KEY (idprot),
    FOREIGN KEY (idpix) REFERENCES pagamento(idpix) ON DELETE CASCADE
);
CREATE TABLE certidao (
    idcert Serial,
    ano SMALLINT,
    num INTEGER,
    idpix INT NOT NULL,
    PRIMARY KEY (idcert),
	FOREIGN KEY (idpix) REFERENCES PAGAMENTO(idpix) ON DELETE CASCADE
);