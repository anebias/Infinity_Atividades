'''[PYIA-A16] Crie uma tabela chamada Produtos que contenha quatro colunas: ProdutoID, NomeProduto, Quantidade e Preco. A coluna ProdutoID deve ser um identificador único para cada produto, a coluna NomeProduto deve armazenar o nome do produto, a coluna Quantidade deve indicar a quantidade disponível do produto, e a coluna Preco deve representar o preço do produto. Após criar a tabela, insira três registros diferentes, cada um representando um produto distinto, incluindo valores específicos para ProdutoID, NomeProduto, Quantidade e Preco.'''

CREATE TABLE IF NOT EXISTS Produtos(
produto_id INT PRIMARY KEY,
nome_produto VARCHAR(100) NOT NULL,
quantidade INT,
preco FLOAT
);

INSERT INTO Produtos (produto_id, nome_produto, quantidade, preco) VALUES 
(1,"Banana", 120, 6.78),
(2,"Laranja", 200, 5.99),
(3,"Maça", 95, 24.98);