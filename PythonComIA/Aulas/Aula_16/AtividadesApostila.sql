'''ATIVIDADE PRÁTICA 1
Crie uma tabela "pedidos" com as colunas "id_pedido", "id_cliente" e "data_pedido". Adicione uma constraint de chave estrangeira na coluna "id_cliente" para garantir que um pedido só possa ser feito por um cliente existente na tabela "clientes".'''

CREATE TABLE IF NOT EXISTS pedidos (
id_pedido INT PRIMARY KEY AUTO_INCREMENT,
id_cliente INT,
data_pedido DATE,
FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
);

'''ATIVIDADE PRÁTICA 2
Crie uma tabela "produtos" com as colunas "id_produto", "nome_produto" e "preco". Adicione uma constraint de verificação para garantir que o preço do produto seja maior que zero.'''

CREATE TABLE IF NOT EXISTS produtos(
id_produto INT PRIMARY KEY AUTO_INCREMENT,
nome_produto VARCHAR(100) NOT NULL,
preco FLOAT NOT NULL,
CHECK (preco > 0)
);

'''ATIVIDADE PRÁTICA 3
Adicione uma constraint de restrição única na coluna "email" da tabela "clientes" para garantir que nenhum cliente possa ter o mesmo endereço de e-mail.'''

CREATE TABLE IF NOT EXISTS clientes (
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
estoque.
Clientes: Armazena informações sobre os clientes, incluindo um ID, nome, endereço de e-mail e histórico de compras. 
Pedidos: Registra informações sobre os pedidos feitos pelos clientes, incluindo um ID, data do pedido, ID do cliente e status do pedido.
itens_Pedido: Registra os produtos incluídos em cada pedido, incluindo um ID, ID do pedido, ID do
produto e quantidade.'''

CREATE DATABASE IF NOT EXISTS loja_online;

use loja_online;

CREATE TABLE IF NOT EXISTS clientes(
id_cliente INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
email VARCHAR(50),
historico_compras TEXT
);

CREATE TABLE IF NOT EXISTS produtos(
id_produto INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
preco DOUBLE(10,2),
quantidade_estoque INT 
);

CREATE TABLE IF NOT EXISTS pedidos (
id_pedido INT PRIMARY KEY AUTO_INCREMENT,
id_cliente INT,
data_pedido DATE,
status_pedido VARCHAR(20),
FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
);

CREATE TABLE IF NOT EXISTS itens_pedido(
id_item_pedido INT PRIMARY KEY AUTO_INCREMENT,
id_pedido INT,
id_produto INT,
quantidade INT,
FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
FOREIGN KEY (id_produto) REFERENCES produtos (id_produto)
);

INSERT INTO clientes (nome, email, historico_compras) VALUES
('Amanda Torres', 'amanda.torres@email.com', 'Comprou teclado em 2024'),
('Bruno Andrade', 'bruno.andrade@email.com', 'Comprou notebook em 2023'),
('Camila Souza', 'camila.souza@email.com', 'Nenhuma compra registrada'),
('Daniel Farias', 'daniel.farias@email.com', 'Comprou monitor em 2022'),
('Eduarda Lima', 'eduarda.lima@email.com', 'Cliente novo'),
('Felipe Rocha', 'felipe.rocha@email.com', 'Comprou mouse em 2023'),
('Gabriela Menezes', 'gabriela.m@email.com', 'Comprou cadeira gamer em 2024'),
('Henrique Silva', 'henrique.silva@email.com', 'Comprou headset em 2023'),
('Isabela Castro', 'isabela.castro@email.com', 'Nenhuma compra registrada'),
('João Vitor', 'joao.vitor@email.com', 'Comprou impressora em 2022'),
('Rafael Martins', 'rafael.martins@email.com', 'Nenhuma compra registrada'),
('Tatiane Alves', 'tatiane.alves@email.com', 'Nenhuma compra registrada'),
('Vinícius Pereira', 'vinicius.pereira@email.com', 'Nenhuma compra registrada'),
('Beatriz Gomes', 'beatriz.gomes@email.com', 'Nenhuma compra registrada'),
('Caio Nogueira', 'caio.nogueira@email.com', 'Nenhuma compra registrada');

INSERT INTO produtos (nome, preco, quantidade_estoque) VALUES
('Notebook Dell', 3499.99, 12),
('Mouse Óptico', 79.90, 150),
('Teclado Gamer RGB', 199.99, 85),
('Monitor 27" 4K', 2299.00, 20),
('Cadeira Gamer', 1399.00, 5),
('Headset USB', 249.50, 60),
('Impressora Multifuncional', 899.90, 10),
('Webcam Full HD', 199.00, 33),
('HD Externo 1TB', 379.90, 40),
('Hub USB 4 portas', 49.90, 70);

INSERT INTO pedidos (id_cliente, data_pedido, status_pedido) VALUES
(1, '2025-01-12', 'Enviado'),
(2, '2025-02-03', 'Entregue'),
(3, '2025-02-25', 'Pendente'),
(4, '2025-03-10', 'Cancelado'),
(5, '2025-03-12', 'Enviado'),
(6, '2025-03-22', 'Pendente'),
(7, '2025-03-25', 'Entregue'),
(8, '2025-04-01', 'Em processamento'),
(9, '2025-04-02', 'Enviado'),
(10, '2025-04-03', 'Entregue'),
(NULL, '2025-03-10', 'Pendente'),
(NULL, '2025-03-15', 'Em processamento'),
(NULL, '2025-03-20', 'Cancelado'),
(NULL, '2025-03-25', 'Pendente'),
(NULL, '2025-04-01', 'Em aberto');

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade) VALUES
(1, 1, 1),
(2, 3, 2),
(3, 6, 1),
(4, 4, 1),
(5, 2, 3),
(6, 10, 2),
(7, 5, 1),
(8, 7, 1),
(9, 8, 2),
(10, 9, 1);

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

CREATE DATABASE IF NOT EXISTS vendas; 

use vendas;

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(100) NOT NULL,
    email_cliente VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS produtos(
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(100) NOT NULL,
    preco_produto DECIMAL NOT NULL
);

CREATE TABLE IF NOT EXISTS vendas(
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    data_venda DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
);

INSERT INTO clientes (nome_cliente, email_cliente) VALUES
('Mariana Silva', 'mariana.silva@email.com'),
('Lucas Oliveira', 'lucas.o@email.com'),
('Carla Mendes', 'carla.mendes@email.com'),
('João Batista', 'joao.b@email.com'),
('Fernanda Rocha', 'fernanda.rocha@email.com');

INSERT INTO produtos (nome_produto, preco_produto) VALUES
('Mouse Gamer RGB', 129.90),
('Teclado Mecânico', 249.50),
('Monitor 24" LED', 899.99),
('Cadeira Ergonômica', 1149.00),
('Headset Bluetooth', 299.00);

INSERT INTO vendas (id_cliente, data_venda) VALUES
(1, '2025-04-01'),
(2, '2025-04-02'),
(3, '2025-04-02'),
(1, '2025-04-03'),
(5, '2025-04-05'),
(2, '2022-10-15'),
(4, '2021-12-05'),
(3, '2022-07-20');

'''
a) Crie uma consulta SQL para selecionar todos os clientes cadastrados.
b) Escreva um código SQL para inserir um novo produto chamado "Notebook" com o preço de R$2.500,00 na tabela "Produtos".
c) Atualize o nome do cliente com o id_cliente igual a 1 para "Maria Silva".
d) Remova todos os registros da tabela "Vendas" que ocorreram antes de 01 de janeiro de 2023.'''

SELECT * FROM clientes;
INSERT INTO produtos (nome_produto, preco_produto) VALUES ("Notebook",2500);
UPDATE	clientes SET nome_cliente = "Maria Silva" WHERE id_cliente = 1;
DELETE FROM vendas WHERE data_venda < "2023-01-01";

# VERIFICAR ALTERAÇÕES APLICADAS
SELECT * FROM produtos;
SELECT * FROM clientes;
SELECT * FROM vendas;
