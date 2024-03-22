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