# PROJETO II
'''Vamos supor que você conseguiu um trabalho como programador e a tarefa que foi dada a você é desenvolver um sistema de gerenciamento de estoque para uma loja.'''

'''REQUISITOS DO PROJETO
O sistema deve permitir:
- Cadastro de um novo produto.
- Consulta dos produtos cadastrados.
- Atualização das quantidades disponíveis.
- Remoção de produtos do cadastro.
'''

'''BANCO DE DADOS
Persistência de Dados:
Conecte-se ao banco de dados para salvar informações dos produtos, como ID, nome, descrição, entre outros. Essas informações permitem o rastreamento dos produtos em estoque.

A persistência desses dados no banco de dados garante que as informações sejam armazenadas de forma segura e possam ser acessadas e manipuladas conforme necessário pelo sistema.
Utilize um sistema de gerenciamento de banco de dados para garantir a persistência das informações e crie um banco de dados para armazená-las. O banco deve conter, no mínimo, as seguintes tabelas:
- Tabela de Produtos
- Tabela de Vendas

OBS: Caso seja necessário, o banco de dados poderá conter mais tabelas para atender a requisitos adicionais do sistema.
'''

'''OBJETOS
Utilize princípios de Programação Orientada a Objetos (POO) e crie classes para representar os elementos do sistema.

VENDA
    Atributos:
    ID da venda
    ID do produto vendido
    Quantidade vendida
    Data da venda

PRODUTO
    Atributos:
    ID
    Nome
    Descrição
    Quantidade disponível
    Preço

O sistema deve conter uma estrutura mínima de objetos, seguindo os requisitos abaixo:
OBS: Caso seja necessário, o banco de dados poderá conter mais classes para atender a requisitos adicionais do sistema.
'''

import sqlite3

conexao = sqlite3.connect('bd_projeto')
cursor = conexao.cursor()

sql_cria_tabela_produtos = '''CREATE TABLE IF NOT EXISTS produtos(
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        quantidade_disponivel INTEGER,
        preco REAL
)'''
sql_cria_tabela_vendas = '''CREATE TABLE IF NOT EXISTS vendas(
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto_vendido INTEGER NOT NULL,
        quantidade_vendida INTEGER CHECK(quantidade_vendida > 0),
        data_venda DATE CHECK(data_venda LIKE '____-__-__') NOT NULL,
        FOREIGN KEY (id_produto_vendido) REFERENCES produtos(id_produto) ON DELETE CASCADE
)'''

cursor.execute(sql_cria_tabela_produtos)
cursor.execute(sql_cria_tabela_vendas)
conexao.commit()

class Produto:
    def __init__(self, nome, descricao, quantidade_disponivel, preco):
        self.nome = nome
        self.descricao = descricao
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco

    def __str__(self):
        return f"{self.nome}, {self.descricao}, {self.quantidade_disponivel}, {self.preco}"

class Venda:
    def __init__(self, id_produto_vendido, quantidade_vendida, data_venda):
        self.id_produto_vendido = id_produto_vendido
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda

    def __str__(self):
        return f"{self.id_produto_vendido}, {self.quantidade_vendida}, {self.data_venda}"

class Loja:
    def __init__(self, nome_loja):
        self.nome_loja = nome_loja
    
    def cadastrar_produto(self,produto):

        sql = '''INSERT INTO produtos (nome, descricao, quantidade_disponivel, preco) VALUES (?,?,?,?)'''

        produto_cadastrado = cursor.execute(sql,(produto.nome, produto.descricao, produto.quantidade_disponivel, produto.preco))
        conexao.commit()

        return produto_cadastrado
    
    def consultar_produtos_cadastrados(self):
        sql = '''SELECT * FROM produtos'''
        produtos_cadastrados = cursor.execute(sql)

        return produtos_cadastrados.fetchall()

    def atualizar_quantidades_disponiveis(self,id_produto,nova_quantidade):
        sql = '''UPDATE produtos SET quantidade_disponivel = ? WHERE id_produto = ?'''

        produto_atualizado = cursor.execute(sql,(nova_quantidade,id_produto))
        conexao.commit()

        return produto_atualizado

    def remover_produto(self,id_produto):
        sql = '''DELETE FROM produtos WHERE id_produto = ?'''

        cursor.execute(sql,(id_produto,))
        conexao.commit()

        return 'produto removido com sucesso'

# TESTES
# Instanciando a loja para administrar as funcionalidades e os produtos
loja = Loja('Loja Online')
produto_1 = Produto('Fritadeira Tradicional','fritadeira à óleo',15,398.99)
produto_2 = Produto('Fritadeira Elétrica','fritadeira elétrica 110v',20,697.99)
produto_3 = Produto('Liquidificador Oster','liquidificador portencia 400w',8,148.99)
produto_4 = Produto('Batedeira Planetária Arno','batedeira planetária com proteção de borda',18,598.99)
produto_5 = Produto('Mixer Arno','processador de alimentos versátil',17,248.99)

# Cadastrando os produtos na loja
loja.cadastrar_produto(produto_1)
loja.cadastrar_produto(produto_2)
loja.cadastrar_produto(produto_3)
loja.cadastrar_produto(produto_4)
loja.cadastrar_produto(produto_5)

# Consultando todos os produtos cadastrados
print('Todos os produtos cadastrados')
for produto in loja.consultar_produtos_cadastrados():
    print(produto)
print('Atualizando quantidade do produto 1 de 15 para 14, como se tivesse realizado uma venda')
loja.atualizar_quantidades_disponiveis(1,14)
print('Consultando todos os produtos cadastrados após atualização')
for produto in loja.consultar_produtos_cadastrados():
    print(produto)
print('removendo o produto 5')
loja.remover_produto(5)
print('Consultando todos os produtos cadastrados após exclusão')
for produto in loja.consultar_produtos_cadastrados():
    print(produto)

conexao.close()