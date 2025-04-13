'''[PYIA-A17] Crie uma tabela chamada Estoque que contenha as seguintes colunas: EstoqueID, ProdutoID, FornecedorID, Quantidade e DataEntrada. A coluna EstoqueID deve ser um identificador único para cada registro no estoque. A coluna ProdutoID deve referenciar o identificador do produto correspondente na tabela de produtos, e a coluna FornecedorID deve referenciar o identificador do fornecedor na tabela de fornecedores, ambas atuando como chaves estrangeiras para estabelecer a relação com outras tabelas. A coluna Quantidade deve indicar a quantidade de produtos recebidos, e a coluna DataEntrada deve armazenar a data em que os produtos entraram no estoque. Para criar esta tabela e garantir as referências corretas, é necessário definir as chaves estrangeiras para ProdutoID e FornecedorID.

Após a criação da tabela, você pode utilizar operações de banco de dados como FULL OUTER JOIN para combinar informações de diferentes tabelas, GROUP BY para agrupar dados com base em uma ou mais colunas, e ALTER TABLE para modificar a estrutura da tabela, como adicionar ou alterar colunas.'''

CREATE TABLE IF NOT EXISTS Produtos(
produto_id INT PRIMARY KEY,
nome_produto VARCHAR(100) NOT NULL,
quantidade INT,
preco FLOAT
);

INSERT INTO Produtos (produto_id, nome_produto, quantidade, preco) VALUES 
(1,"Banana", 120, 6.78),
(2,"Laranja", 200, 5.99),
(3,"Maça", 95, 24.98),
(4,"Ovos", 360, 29.98),
(5, "Filé Mignon", 10, 74.99),
(6, "Frango", 25, 19.90);

CREATE TABLE IF NOT EXISTS fornecedores(
fornecedor_id INT PRIMARY KEY AUTO_INCREMENT,
nome_fornecedor VARCHAR(100)
);

INSERT INTO fornecedores (nome_fornecedor) VALUES ("CEASA MG"), ("Granja de Ovos"), ("Frigorífico Boizão");

CREATE TABLE IF NOT EXISTS estoque (
estoque_id INT PRIMARY KEY AUTO_INCREMENT,
produto_id INT,
fornecedor_id INT,
quantidade INT,
data_entrada DATE,
FOREIGN KEY (produto_id) REFERENCES produtos (produto_id),
FOREIGN KEY (fornecedor_id) REFERENCES fornecedores (fornecedor_id)
);

INSERT INTO estoque (produto_id, fornecedor_id, quantidade, data_entrada) 
VALUES (1,1,240,"2025-01-10"),
(1,1,240,"2025-02-10"),
(2,1,110,"2025-01-20"),
(3,2,20,"2024-12-10"),
(4,3,40,"2025-02-28"),
(5,2,70,"2025-04-01");

# EXIBIR TODOS OS DADOS DAS TABELAS PRODUTOS, FORNECEDORES E ESTOQUE
SELECT * FROM produtos;
SELECT * FROM fornecedores;
SELECT * FROM estoque;

# EXIBIR AS COLUNAS SELECIONADAS DAS DUAS TABELAS RELACIONADAS QUANDO EXISTIR RELACIONAMENTO
SELECT P.nome_produto, P.quantidade AS quantidade_exposta, P.preco, F.nome_fornecedor, E.quantidade AS quantidade_estoque, E.data_entrada FROM estoque E
JOIN produtos P
ON E.produto_id = P.produto_id
JOIN fornecedores F
ON E.fornecedor_id = F.fornecedor_id
;

# ALTERAÇÕES NA TABELA: INCLUSAO COLUNA, RENOMEAR COLUNA, ALTERAR TIPO DA COLUNA, EXCLUIR COLUNA
ALTER TABLE produtos ADD COLUMN peso NUMERIC;
ALTER TABLE produtos RENAME COLUMN peso TO peso_produto;
ALTER TABLE produtos MODIFY COLUMN peso_produto DOUBLE;
ALTER TABLE produtos DROP COLUMN peso_produto;

# EXIBIR TODOS OS REGISTROS DAS TABELAS RELACIONADAS
SELECT P.nome_produto, P.quantidade, P.preco, E.quantidade AS quantidade_estoque, E.data_entrada FROM produtos P FULL OUTER JOIN estoque E
ON P.produto_id = E.produto_id;

# EXIBIR TODOS OS REGISTROS DA TABELA À ESQUERDA (PRODUTOS)
SELECT P.nome_produto, P.quantidade, P.preco, E.quantidade AS quantidade_estoque, E.data_entrada FROM produtos P LEFT JOIN estoque E
ON P.produto_id = E.produto_id;

# EXIBIR TODOS OS REGISTROS DA TABELA À DIREITA (ESTOQUE)
SELECT P.nome_produto, P.quantidade, P.preco, E.quantidade AS quantidade_estoque, E.data_entrada FROM produtos P RIGHT JOIN estoque E
ON P.produto_id = E.produto_id;

# AGRUPAMENTO DE REGISTROS POR FORNECEDOR, CONTANDO QUANTOS PRODUTOS DE CADA FORNECEDOR
SELECT F.nome_fornecedor, count(E.fornecedor_id) AS quantidade_produtos FROM
fornecedores F JOIN estoque E ON F.fornecedor_id = E.fornecedor_id
GROUP BY F.nome_fornecedor
ORDER BY F.nome_fornecedor;