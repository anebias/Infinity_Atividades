'''ATIVIDADE PRÁTICA 1
Suponha que você tenha uma tabela "clientes" e uma tabela "pedidos". Escreva uma consulta SQL que retorne o nome do cliente e o número do pedido para todos os clientes, incluindo aqueles que não fizeram nenhum pedido. Utilizando as mesmas tabelas de "clientes" e "pedidos", escreva uma consulta SQL que retorne o nome do cliente e o número do pedido para todos os pedidos, incluindo os pedidos que não estão associados a nenhum cliente.'''


'''ATIVIDADE PRÁTICA 2
Suponha que você tenha uma tabela "vendedores" e uma tabela "vendas". Escreva uma consulta SQL que retorne o nome do vendedor e o valor da venda para todas as vendas e todos os vendedores, incluindo os vendedores que não fizeram nenhuma venda e as vendas não associadas a nenhum vendedor.'''


'''ATIVIDADE PRÁTICA 3
Suponha que você tenha tabelas "Pessoas" e "Documentos de Identidade" com um relacionamento um-para-um. Escreva uma consulta para recuperar o nome de cada pessoa e o número do documento de identidade, se estiverem disponíveis.'''


'''ATIVIDADE PRÁTICA 4
Suponha que você tenha tabelas "Autores" e "Livros" com um relacionamento um-para-muitos. Escreva uma consulta que retorne o nome de cada autor e os títulos dos livros que eles escreveram.'''


'''ATIVIDADE PRÁTICA 5
Dado um cenário com tabelas "Músicos" e "Bandas" com um relacionamento muitos-para-muitos, escreva uma consulta que liste o nome de cada músico e as bandas em que eles tocam.'''

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