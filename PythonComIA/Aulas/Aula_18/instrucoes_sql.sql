CREATE TABLE IF NOT EXISTS produtos(
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        quantidade_disponivel INTEGER,
        preco REAL
);

CREATE TABLE IF NOT EXISTS vendas(
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto_vendido INTEGER NOT NULL,
        quantidade_vendida INTEGER CHECK(quantidade_vendida > 0),
        data_venda DATE CHECK(data_venda LIKE '____-__-__') NOT NULL,
        FOREIGN KEY (id_produto_vendido) REFERENCES produtos(id_produto) ON DELETE CASCADE
);

INSERT INTO produtos (nome, descricao, quantidade_disponivel, preco) VALUES (?,?,?,?);

INSERT INTO vendas (id_produto,quantidade_vendida,data_venda) VALUES(?,?,?);

SELECT * FROM produtos WHERE id_produto = ?;

SELECT * FROM vendas WHERE id_venda = ?;

SELECT * FROM produtos;

UPDATE produtos SET quantidade_vendida = ? WHERE id_produto = ?;

DELETE FROM produtos WHERE id_produto = ?;