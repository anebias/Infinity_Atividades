'''[PYIA-A15] Crie uma tabela chamada Clientes com as colunas ID, Nome, Idade e Cidade. Defina a coluna ID como a chave primária e autoincrementável.'''

CREATE TABLE Clientes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100),
  idade INT,
  cidade VARCHAR (100)
);

# EXEMPLO DE INSERÇÃO DE DADOS NA TABELA
INSERT INTO Clientes (nome, idade, cidade) VALUES
('Ana', 18, 'Belo Horizonte'),
('Diego', 20, 'Salvador'),
('Catarina', 19, 'Recife');