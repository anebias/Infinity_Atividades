# CLAUSULA GROUP BY
'''A cláusula GROUP BY é usada em consultas SQL para agrupar
linhas de dados com base em valores em uma ou mais colunas
e aplicar funções de agregação a esses grupos. Ela é
comumente usada em conjunto com funções de agregação,
como SUM, COUNT, MAX, MIN, entre outras.'''

SELECT departamento, count(*) AS total_funcionarios 
FROM funcionarios
GROUP BY departamento;

# RELACIONAMENTOS MUITOS PARA MUITOS
'''Um relacionamento muitos-para-muitos (N:M) em bancos de
dados SQL ocorre quando múltiplos registros em uma tabela
podem estar relacionados a múltiplos registros em outra tabela.
Para representar esse tipo de relacionamento, você
normalmente usa uma tabela intermediária ( também conhecida
como tabela de junção) que associa registros de ambas as
tabelas. O relacionamento muitos-para-muitos é comumente
usado para modelar associações complexas entre entidades em
um banco de dados.'''

# EXEMPLO:
CREATE TABLE alunos (
id_aluno INT PRIMARY KEY AUTO_INCREMENT,
nome_aluno VARCHAR(100) NOT NULL
);

CREATE TABLE cursos(
id_curso INT PRIMARY KEY AUTO_INCREMENT,
nome_curso VARCHAR(100) NOT NULL
);

# As tabelas ALUNOS e CURSOS têm relacionamento MUITOS-PARA-MUITOS
# Tabela intermediária: MATRICULAS

CREATE TABLE matriculas(
id_matricula INT PRIMARY KEY AUTO_INCREMENT,
id_aluno INT,
id_curso INT,
FOREIGN KEY (id_aluno) REFERENCES alunos (id_aluno),
FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
);

'''ATIVIDADE PRÁTICA 1
Suponha que você tenha uma tabela "clientes" e uma tabela "pedidos". Escreva uma consulta SQL que retorne o nome do cliente e o número do pedido para todos os clientes, incluindo aqueles que não fizeram nenhum pedido. Utilizando as mesmas tabelas de "clientes" e "pedidos", escreva uma consulta SQL que retorne o nome do cliente e o número do pedido para todos os pedidos, incluindo os pedidos que não estão associados a nenhum cliente.'''

CREATE DATABASE IF NOT EXISTS loja_online;

use loja_online;

CREATE TABLE IF NOT EXISTS clientes(
id_cliente INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
email VARCHAR(50),
historico_compras TEXT
);

CREATE TABLE IF NOT EXISTS pedidos (
id_pedido INT PRIMARY KEY AUTO_INCREMENT,
id_cliente INT,
data_pedido DATE,
status_pedido VARCHAR(20),
FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
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

SELECT nome,id_pedido FROM clientes C LEFT JOIN pedidos P ON C.id_cliente = P.id_cliente;

SELECT nome,id_pedido FROM clientes C RIGHT JOIN pedidos P ON C.id_cliente = P.id_cliente;


'''ATIVIDADE PRÁTICA 2
Suponha que você tenha uma tabela "vendedores" e uma tabela "vendas". Escreva uma consulta SQL que retorne o nome do vendedor e o valor da venda para todas as vendas e todos os vendedores, incluindo os vendedores que não fizeram nenhuma venda e as vendas não associadas a nenhum vendedor.'''

# COMANDO FULL OUTER JOIN NÃO SUPORTADO PELO MYSQL
SELECT nome_vendedor, id_venda FROM vendedores V FULL OUTER JOIN vendas VD ON V.id_vendedor = VD.id_vendedor;

'''ATIVIDADE PRÁTICA 3
Suponha que você tenha tabelas "Pessoas" e "Documentos de Identidade" com um relacionamento um-para-um. Escreva uma consulta para recuperar o nome de cada pessoa e o número do documento de identidade, se estiverem disponíveis.'''

SELECT nome, numero_documento FROM pessoas P INNER JOIN documentos_identidade D 
ON P.id_pessoa = D.id_pessoa;

'''ATIVIDADE PRÁTICA 4
Suponha que você tenha tabelas "Autores" e "Livros" com um relacionamento um-para-muitos. Escreva uma consulta que retorne o nome de cada autor e os títulos dos livros que eles escreveram.'''

SELECT nome_autor, titulo_livro FROM autores A INNER JOIN livros L
ON A.id_autor = L.id_autor;

'''ATIVIDADE PRÁTICA 5
Dado um cenário com tabelas "Músicos" e "Bandas" com um relacionamento muitos-para-muitos, escreva uma consulta que liste o nome de cada músico e as bandas em que eles tocam.'''

CREATE DATABASE IF NOT EXISTS atividade;

use atividade;

CREATE TABLE musicos (
id_musico INT PRIMARY KEY AUTO_INCREMENT,
nome_musico VARCHAR(100) NOT NULL
);

CREATE TABLE bandas (
id_banda INT PRIMARY KEY AUTO_INCREMENT,
nome_banda VARCHAR(100) NOT NULL
);

CREATE TABLE grupos_musicais (
id_grupo INT PRIMARY KEY AUTO_INCREMENT,
id_musico INT,
id_banda INT,
FOREIGN KEY (id_musico) REFERENCES musicos (id_musico),
FOREIGN KEY (id_banda) REFERENCES bandas (id_banda)
);

INSERT INTO musicos (nome_musico) VALUES
('Carlos Santana'),
('Fernanda Reis'),
('João Paulo Andrade'),
('Lívia Torres'),
('Marcos Vinícius'),
('Ana Clara Ribeiro'),
('Gustavo Martins'),
('Tatiane Alves');

INSERT INTO bandas (nome_banda) VALUES
('Os Astronautas do Som'),
('Rock de Quinta'),
('Jazz Brasil'),
('Samba Raiz'),
('Fusão Alternativa');

INSERT INTO grupos_musicais (id_musico, id_banda) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 3),
(6, 4),
(7, 5),
(8, 5),
(1, 2),  -- Carlos em duas bandas
(4, 5);  -- Lívia em duas bandas

INSERT INTO musicos (nome_musico) VALUES
('Ricardo Luz'),
('Bianca Almeida'),
('Lucas Ferraz'),
('Juliana Costa'),
('Pedro Henrique'),
('Sofia Martins'),
('André Carvalho'),
('Manuela Dias');

INSERT INTO bandas (nome_banda) VALUES
('Som do Interior'),
('Os Improvisados'),
('Voz & Corda'),
('Batuque Moderno'),
('Nova Frequência');

INSERT INTO grupos_musicais (id_musico, id_banda) VALUES
(9, 6),
(10, 6),
(11, 7),
(12, 7),
(13, 8),
(14, 8),
(15, 9),
(16, 9),
(9, 7),
(10, 9),
(11, 10),
(12, 10),
(13, 6),
(14, 10),
(15, 8),
(16, 7);

SELECT nome_musico, nome_banda FROM grupos_musicais G 
JOIN musicos M
ON M.id_musico = G.id_musico
JOIN bandas B
ON B.id_banda = G.id_banda
;

-- Contar quantas bandas cada músico participa:
SELECT nome_musico, count(G.id_banda) AS total_bandas
FROM grupos_musicais G
JOIN musicos M
ON G.id_musico = M.id_musico
GROUP BY M.id_musico, M.nome_musico
ORDER BY total_bandas DESC;
-- Contar quantos músicos há em cada banda:
SELECT 
  B.nome_banda, 
  COUNT(G.id_musico) AS total_musicos
FROM grupos_musicais G
JOIN bandas B ON B.id_banda = G.id_banda
GROUP BY B.id_banda, B.nome_banda
ORDER BY total_musicos DESC;
-- Listar todas as bandas de um músico em uma única linha:
SELECT 
  M.nome_musico, 
  GROUP_CONCAT(B.nome_banda SEPARATOR ', ') AS bandas
FROM grupos_musicais G
JOIN musicos M ON M.id_musico = G.id_musico
JOIN bandas B ON B.id_banda = G.id_banda
GROUP BY M.id_musico, M.nome_musico
ORDER BY M.nome_musico;

'''DESAFIO PRÁTICO
Banco de dados de uma biblioteca 

DESAFIO FINAL
Suponha que você esteja gerenciando um banco de dados para uma biblioteca. O banco de dados contém as seguintes tabelas:
Tabela "Livros" com as seguintes colunas: 
* livro_id (Chave Primária)
* título
* autor_id (Chave Estrangeira relacionando-se à tabela "Autores")
* ano_publicação
* gênero'''
Tabela "Autores" com as seguintes colunas:
*autor_id (Chave Primária)
* nome_autor
Tabela "Empréstimos" com as seguintes colunas:
*emprestimo_id (Chave Primária)
* livro_id (Chave Estrangeira relacionando-se à tabela "Livros")
* data_emprestimo
* data_devolução

Seu desafio é escrever uma consulta SQL que retorna o nome
de cada autor, o título do livro emprestado e a data de
empréstimo. No entanto, você precisa considerar apenas os
autores cujos livros foram emprestados. Além disso, a
consulta deve listar os autores em ordem alfabética e os livros
em ordem de data de empréstimo crescente.'''

CREATE DATABASE IF NOT EXISTS atividade;

use atividade;

CREATE TABLE IF NOT EXISTS Autores (
  autor_id INT PRIMARY KEY AUTO_INCREMENT,
  nome_autor VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Livros (
  livro_id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(150) NOT NULL,
  autor_id INT,
  ano_publicacao INT,
  genero VARCHAR(50),
  FOREIGN KEY (autor_id) REFERENCES Autores(autor_id)
);

CREATE TABLE IF NOT EXISTS Emprestimos (
  emprestimo_id INT PRIMARY KEY AUTO_INCREMENT,
  livro_id INT,
  data_emprestimo DATE,
  data_devolucao DATE,
  FOREIGN KEY (livro_id) REFERENCES Livros(livro_id)
);

INSERT INTO Autores (nome_autor) VALUES
('Clarice Lispector'),
('Machado de Assis'),
('J.K. Rowling'),
('George Orwell'),
('Gabriel García Márquez');

INSERT INTO Livros (titulo, autor_id, ano_publicacao, genero) VALUES
('A Hora da Estrela', 1, 1977, 'Romance'),
('Dom Casmurro', 2, 1899, 'Romance'),
('Harry Potter e a Pedra Filosofal', 3, 1997, 'Fantasia'),
('1984', 4, 1949, 'Distopia'),
('Cem Anos de Solidão', 5, 1967, 'Realismo Mágico'),
('Harry Potter e a Câmara Secreta', 3, 1998, 'Fantasia'),
('Memórias Póstumas de Brás Cubas', 2, 1881, 'Romance'),
('A Paixão Segundo G.H.', 1, 1964, 'Filosófico');

INSERT INTO Emprestimos (livro_id, data_emprestimo, data_devolucao) VALUES
(1, '2024-12-15', '2025-01-10'),
(3, '2025-01-05', '2025-01-20'),
(4, '2025-02-01', NULL),
(2, '2025-03-10', '2025-03-25'),
(6, '2025-03-20', NULL),
(7, '2025-04-01', NULL);

SELECT nome_autor, titulo, data_emprestimo FROM Autores A
INNER JOIN Livros L
ON A.autor_id = L.autor_id
INNER JOIN Emprestimos E
ON E.livro_id = L.livro_id
ORDER BY nome_autor, data_emprestimo;