# Agenda

Mini agenda de contatos feita em Python. Projeto inicial para treino de Python.

<hr>

> Funcionalidades

1. Ver todos os contatos
2. Buscar um contato por nome
3. Adicionar novo contato
4.  Editar contato existente
5.  Excluir contato
6.   Exportar contatos para CSV
7.  Importar contatos de CSV
8.  Salva e carrega contatos ao iniciar (persistência em arquivo CSV)

<hr>
 Uso
<br>
Ao executar o script python, um menu é exibido permitindo escolher as opções acima.

O estado atual da agenda (contatos e dados) é salvo no arquivo `database.csv` a cada alteração, e carregado novamente na inicialização.
Implementação

A agenda é implementada em Python utilizando um dicionário `AGENDA` para manter os dados em memória.

Cada contato é uma chave deste dicionário apontando para outro dicionário com os campos: telefone, email e endereço.

As funções implementam as diversas operações como adicionar, editar, excluir e buscar contatos interagindo com o dicionário de dados.

Para persistência, os dados são exportados para o CSV database.csv utilizando encoding e decoding próprio em texto.

<hr>
Créditos
Código inicial fornecido pela Solyd Treinamentos.

Documentação e melhorias adicionadas por [Wesley Pereira](https://github.com/wesleyp846)

> Licença
MIT

pip install flet
pip install flet --upgrade