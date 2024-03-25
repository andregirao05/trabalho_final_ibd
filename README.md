# Trabalho Final da Disciplina de Introdução a Banco de Dados (2023/2)

## Instalação de dependências

Para instalar as dependências necessárias para utilizar este projeto, execute o seguinte comando:
```
pip install -r requirements.txt
```

## Variáveis de ambiente

Os scripts necessitam de algumas variáveis de ambiente. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
DB_HOST="<ip do host>"
DB_NAME=<nome do banco de dados>
DB_USER=<usuario do banco de dados>
DB_PASSWORD=<senha do usuario>
```

## Execução dos scripts

Certifique-se que o banco de dados está ativo e com as tabelas já criadas (o script de criação do banco de dados `MYSQL` escontra-se em `sql_scripts/create_database.sql`).

Para ver o projeto em funcionamento, execute o arquivo principal:
```
python src/main.py
```

## (OPICIONAL) Carregar todos os dados (DUMP do banco de dados)

Todos os dados do banco de dados que foram utilizados neste trabalho estão em `sql_scripts/dump_database.sql`.
