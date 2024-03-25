CREATE DATABASE IF NOT EXISTS livraria;

USE livraria;

CREATE TABLE nacionalidade (
	codigo CHAR(2) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE autor (
	codigo INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(100) NOT NULL,  
    data_nascimento DATE NOT NULL, 
    nota_bibliografica TEXT, 
    codigo_nacionalidade CHAR(2) NOT NULL,
    FOREIGN KEY (codigo_nacionalidade) REFERENCES nacionalidade (codigo)
);

CREATE TABLE editora (
	codigo INT AUTO_INCREMENT PRIMARY KEY, 
	nome VARCHAR(255) NOT NULL, 
	telefone VARCHAR(18) NOT NULL, 
	endereco VARCHAR(255) NOT NULL
);

CREATE TABLE idioma (
	codigo CHAR(3) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE livro (
	codigo INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    ano YEAR,
    codigo_idioma CHAR(3) NOT NULL,
    FOREIGN KEY (codigo_idioma) REFERENCES idioma (codigo)
);

CREATE TABLE escreve (
	codigo_autor INT NOT NULL,
    codigo_livro INT NOT NULL,
    PRIMARY KEY (codigo_autor, codigo_livro),
    FOREIGN KEY (codigo_autor) REFERENCES autor (codigo),
    FOREIGN KEY (codigo_livro) REFERENCES livro (codigo)
);

CREATE TABLE edicao (
	isbn CHAR(13) PRIMARY KEY,
    ano YEAR NOT NULL,
    numero_paginas SMALLINT NOT NULL,
    valor DECIMAL(12, 2) NOT NULL,
    quantidade_estoque INT NOT NULL,
    codigo_livro INT NOT NULL,
    codigo_editora INT NOT NULL,
    FOREIGN KEY (codigo_livro) REFERENCES livro (codigo),
    FOREIGN KEY (codigo_editora) REFERENCES editora (codigo)
);

CREATE VIEW livros_com_mais_estoque AS
SELECT
	edicao.isbn AS codigo_ISBN_edicao,
    top_livros.codigo_livro AS codigo_livro,
	top_livros.titulo AS titulo_livro,
    top_livros.ano AS ano_lancamento_livro,
    idioma.nome AS idioma,
    top_livros.codigo_idioma AS codigo_idioma,
    autor.nome AS nome_autor,
    autor.codigo AS codigo_autor,
    editora.nome AS nome_editora,
    editora.codigo AS codigo_editora,
    edicao.ano AS ano_lancamento_edicao,
    edicao.numero_paginas AS numero_paginas_edicao,
    edicao.valor AS valor_edicao,
    edicao.quantidade_estoque AS quantidade_estoque_edicao,
    top_livros.total_estoque AS total_estoque_livro
FROM (
		SELECT 
			livro.codigo AS codigo_livro,
			livro.titulo,
            livro.ano,
            livro.codigo_idioma,
			SUM(edicao.quantidade_estoque) AS total_estoque
		FROM edicao
		JOIN livro ON edicao.codigo_livro = livro.codigo
		GROUP BY livro.codigo, livro.titulo
		ORDER BY total_estoque DESC
        LIMIT 10
	) AS top_livros
JOIN edicao ON edicao.codigo_livro = top_livros.codigo_livro
JOIN editora ON edicao.codigo_editora = editora.codigo
JOIN idioma ON top_livros.codigo_idioma = idioma.codigo
JOIN escreve ON escreve.codigo_livro = top_livros.codigo_livro
JOIN autor ON escreve.codigo_autor = autor.codigo;