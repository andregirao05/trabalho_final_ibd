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