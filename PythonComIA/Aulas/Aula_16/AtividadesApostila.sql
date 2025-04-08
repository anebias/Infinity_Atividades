'''ATIVIDADE PRÁTICA 1
Crie uma tabela "pedidos" com as colunas "id_pedido", "id_cliente" e "data_pedido". Adicione uma constraint de chave estrangeira na coluna "id_cliente" para garantir que um pedido só possa ser feito por um cliente existente na tabela "clientes".'''

CREATE TABLE pedidos (
id_pedido INT PRIMARY KEY AUTO_INCREMENT,
id_cliente INT,
data_pedido DATE,
FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
);

'''ATIVIDADE PRÁTICA 2
Crie uma tabela "produtos" com as colunas "id_produto", "nome_produto" e "preco". Adicione uma constraint de verificação para garantir que o preço do produto seja maior que zero.'''

CREATE TABLE produtos(
id_produto INT PRIMARY KEY AUTO_INCREMENT,
nome_produto VARCHAR(100) NOT NULL,
preco FLOAT NOT NULL,
CHECK (preco > 0)
);

'''ATIVIDADE PRÁTICA 3
Adicione uma constraint de restrição única na coluna "email" da tabela "clientes" para garantir que nenhum cliente possa ter o mesmo endereço de e-mail.'''

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE
);

'''ATIVIDADE PRÁTICA 4
Escreva uma consulta que recupere o nome de todos os alunos que tenham mais de 20 anos e que estejam matriculados em cursos de "Matemática". Use uma subconsulta para realizar essa tarefa.'''

SELECT nome FROM clientes 
WHERE 
idade > 20 and curso = "Matemática"
;

'''DESAFIO PRÁTICO
Sistema de gerenciamento de vendas

Você está criando um banco de dados para gerenciar vendas de produtos em uma loja online.
Você precisa projetar o esquema do banco de dados e escrever consultas SQL para atender a várias
necessidades da loja. Aqui estão os requisitos:
Crie um banco de dados chamado "loja_online" e as seguintes tabelas:
Produtos: Armazena informações sobre produtos, incluindo um ID, nome, preço e quantidade em
estoque.'''


'''DESAFIO PRÁTICO
Sistema de gerenciamento de vendas

Clientes: Armazena informações sobre os clientes, incluindo um ID, nome, endereço de e-mail e histórico de compras. 
Pedidos: Registra informações sobre os pedidos feitos pelos clientes, incluindo um ID, data do pedido, ID do cliente e status do pedido.
itens_Pedido: Registra os produtos incluídos em cada pedido, incluindo um ID, ID do pedido, ID do
produto e quantidade.'''


'''DESAFIO PRÁTICO
Sistema de gerenciamento de vendas

Imagine que você está trabalhando no desenvolvimento de um sistema de
gerenciamento de vendas para uma loja. Você já possui algumas tabelas
básicas criadas no banco de dados. Agora, você precisa criar consultas
SQL para realizar algumas operações específicas. Considere as seguintes
tabelas:
Tabela "Clientes": Colunas: id_cliente (chave primária), nome_cliente, email_cliente.
Tabela "Produtos": Colunas: id_produto (chave primária), nome_produto, preco_produto.
Tabela "Vendas": Colunas: id_venda (chave primária), id_cliente (chave estrangeira
referenciando a tabela "Clientes"), data_venda.'''


'''DESAFIO PRÁTICO
Sistema de gerenciamento de vendas

a) Crie uma consulta SQL para selecionar todos os clientes cadastrados.
b) Escreva um código SQL para inserir um novo produto chamado "Notebook" com o preço de R$2.500,00 na tabela "Produtos".
c) Atualize o nome do cliente com o id_cliente igual a 1 para "Maria Silva".
d) Remova todos os registros da tabela "Vendas" que ocorreram antes de 01 de janeiro de 2023.'''

