from dataclasses import dataclass
from datetime import date

@dataclass
class Nacionalidade:
    codigo: str
    nome: str

@dataclass
class Autor:
    nome: str
    data_nascimento: date
    nota_biografica: str
    nacionalidade: Nacionalidade
    codigo: int = None

@dataclass
class Editora:
    nome: str
    telefone: str
    endereco: str
    codigo: int = None

@dataclass
class Idioma:
    codigo: str
    nome: str

@dataclass
class Edicao:
    isbn: str
    valor: float
    ano: int
    qtd_estoque: int
    num_pagninas: int
    editora: Editora

@dataclass
class Livro:
    titulo: str
    ano: int 
    idioma: Idioma
    edicoes: list[Edicao]
    codigo: int = None