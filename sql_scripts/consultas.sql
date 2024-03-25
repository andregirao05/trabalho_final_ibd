USE livraria;

-- a) (SELECT) Listar os nomes de todos os autores que têm edições de seus
--    livros publicados com uma determinada editora (id da editora dado como
--    entrada).
SELECT DISTINCT  
 autor.nome
FROM autor
JOIN escreve
	ON autor.codigo = escreve.codigo_autor
JOIN livro 
    ON escreve.codigo_livro = livro.codigo
JOIN edicao
    ON livro.codigo = edicao.codigo_livro
JOIN editora
    ON editora.codigo = edicao.codigo_editora
WHERE editora.codigo = 51;

-- b) (SELECT) Dada uma palavra “XXX” dada como entrada, listar as
--    informações das edições (número da edição, editora, título do livro e seu
--    primeiro autor) que tenha a palavra dada no título do livro da edição.
SELECT 
	edicao.isbn AS isbn_edicao,
    editora.nome AS editora,
    livro.titulo AS titulo_livro,
    autor.nome AS nome_primeiro_autor
FROM livro 
JOIN 
	(SELECT MIN(codigo_autor) AS codigo_autor, codigo_livro FROM escreve GROUP BY codigo_livro) AS escreve
		ON escreve.codigo_livro = livro.codigo
JOIN autor 
	ON autor.codigo = escreve.codigo_autor
JOIN edicao
	ON edicao.codigo_livro = livro.codigo
JOIN editora
	ON editora.codigo = edicao.codigo_editora
WHERE livro.titulo LIKE "%poder%";

-- c) (SELECT) Dada uma string “XXX” dada como entrada, listar as informações
-- das edições (id das edições, editoras, títulos dos livros) onde a string
-- fornecida esteja presente no nome de pelo menos um dos autores dos livros.
SELECT DISTINCT
	edicao.isbn AS isbn_edicao,
    editora.nome AS editora,
    livro.titulo AS titulo_livro
FROM livro 
JOIN escreve
	ON escreve.codigo_livro = livro.codigo
JOIN autor 
	ON autor.codigo = escreve.codigo_autor
JOIN edicao
	ON edicao.codigo_livro = livro.codigo
JOIN editora
	ON editora.codigo = edicao.codigo_editora
WHERE autor.nome LIKE "%Enrico%";
	
-- d) (UPDATE) Atualizar a quantidade de estoque de todas as edições de livros
-- de uma editora dada como entrada - aumentando em 20%.
UPDATE edicao
SET quantidade_estoque = quantidade_estoque * 1.2
WHERE codigo_editora = 51;

-- e) (INSERT) Inserir uma nova edição de um livro que já existe, considerando
-- que essa edição continua associada à editora anterior.
INSERT INTO edicao (isbn, ano, numero_paginas, valor, quantidade_estoque, codigo_livro, codigo_editora)
VALUES ('9780732155278', 1978, 678, 267.99, 360, 503, 37);