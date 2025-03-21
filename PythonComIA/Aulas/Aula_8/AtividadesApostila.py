# REVISÃO GERAL
# lista.append(elemento): 
# Adiciona um elemento ao final da lista.

# lista.extend(iterável): 
# Adiciona os  elementos de um iterável (por exemplo, outra lista) ao final da lista.

#  lista.insert(posição, elemento): 
# Insere um elemento em uma posição específica na lista.

# lista.remove(elemento): 
# Remove a primeira ocorrência de um elemento específico da lista.

#  lista.pop(índice): 
# Remove e retorna o elemento na posição especificada. Se nenhum índice
#  for fornecido, remove e retorna o último elemento.

# lista.sort(): 
# Ordena a lista em ordem crescente (altera a lista original).

# lista.reverse(): 
# Inverte a ordem dos elementos na lista

# ATIVIDADE PRÁTICA 1
#  Dada uma lista de números, crie uma nova lista contendo
#  apenas os números pares.

# import random
# lista_numeros = []
# for i in range(20):
#     lista_numeros.append(random.randint(-100,100))

# lista_pares = [x for x in lista_numeros if x % 2 == 0 ]

# print(lista_numeros)
# print(lista_pares)

# ATIVIDADE PRÁTICA 2
#  Crie um dicionário com informações de produtos,
#  incluindo nome, preço e quantidade em estoque.
#  Implemente funções para adicionar, remover e atualizar
#  produtos no dicionário.

estoque_produto = dict()

estoque_produto = {'2':{'nome':'PRODUTO 2', 'preco': 19.99, 'estoque': 10},
                   '5':{'nome':'PRODUTO 5', 'preco': 9.99, 'estoque': 97}}

def adicionar_produto():
    cadastrado = False
    produto = input('Informe o nome do produto: ').upper()

    while produto in ' '*999:
        print('Nome inválido. Tente novamente.')
        produto = input('Informe o nome do produto: ').upper()

    for valor in list(estoque_produto.values()):
        if valor['nome'] == produto:
            print('Produto já cadastrado')
            cadastrado = True

    if not cadastrado:
        valor = input(f'Informe o valor do produto {produto}: ')
        while valor in ' '*999:
            print('Valor inválido. Tente novamente.')
            valor = input(f'Informe o valor do produto {produto}: ')

        ultima_chave = list(estoque_produto.keys())[-1]
        estoque_produto[f'{int(ultima_chave) + 1}'] = {'nome': produto, 'valor': valor, 'estoque': 0}

        print(f'O produto {produto} foi cadastrado com valor R$ {float(valor):.2f}')

def remover_produto():
    pass

def listar_produtos_cadastrados():
    print('ID - Nome Produto')
    for chave, valor in estoque_produto.items():
        print(f'{chave} - {valor['nome']}')

def atualizar_produto():
    pass

listar_produtos_cadastrados()
# adicionar_produto()

# ATIVIDADE PRÁTICA 3
#  Crie um conjunto com nomes de cores. Implemente uma
#  função que retorne as cores que têm mais de quatro
#  letras.


# ATIVIDADE PRÁTICA 4
#  Crie uma função que receba uma lista de strings e
#  retorne uma nova lista contendo apenas as strings
#  palíndromos.


# Funções Agregadoras
#  sum()
#  Calcula a soma de todos os elementos
#  em um objeto iterável, como uma lista.

#  max() e min()
#  Retorna o valor máximo eo
#  mínimo em um objeto iterável.

#  any() e all() 
#  valor
#  any() retorna True se pelo menos um
#  elemento de uma coleção for verdadeiro,
#  enquanto all() retorna True se todos os
#  elementos forem verdadeiros.

#  len()
#  Retorna o número de elementos em um
#  objeto iterável, como uma lista, tupla ou
#  string.

#  sorted()
#  Classifica os elementos de uma lista em
#  ordem crescente (ou decrescente, se
#  especificado). Não modifica a lista original,
#  mas retorna uma nova lista ordenada

#  join()
#  Esta é uma função de strings que é
#  frequentemente usada para concatenar
#  elementos de uma lista em uma única
#  string, usando um delimitador específico

#  ATIVIDADE PRÁTICA 5
#  Dado um dicionário que representa as vendas de
#  produtos, encontre o produto mais vendido (ou os
#  produtos mais vendidos, se houver um empate).



#  ATIVIDADE PRÁTICA 6
#  Receba uma lista de números e use funções agregadoras
#  para contar quantos valores são ímpares e quantos são
#  pares.

#  ATIVIDADE PRÁTICA 7
#  Você possui dados de vendas trimestrais de uma
#  empresa em uma lista. Cada trimestre é representado
#  como uma lista de números, onde cada número
#  representa o valor de vendas de um mês (janeiro a
#  março, abril a junho, julho a setembro e outubro a
#  dezembro).
#  Você deve realizar as seguintes tarefas:
#  Calcule a média de vendas por trimestre.

#  ATIVIDADE PRÁTICA 7
#  Encontre o trimestre com a maior soma de vendas.
#  Encontre o trimestre com a menor soma de vendas.
#  Calcule o total de vendas no ano inteiro. - Construa seus dados fictícios

#  DESAFIO PRÁTICO
#  Analise de Produção anual
#  Você tem um conjunto de dados que contém informações sobre a
#  produção anual de diferentes culturas em diversas fazendas ao
#  longo de vários anos. O objetivo é realizar
#  uma análise simples desses dados usando apenas as funções
#  agregadoras. 
#  Tarefas: Encontre o ano em que a produção total foi máxima e o
#  ano em que foi mínima. Identifique a cultura que teve a maior
#  produção total e a cultura com a menor produção total ao longo
#  dos anos. Encontre a fazenda que obteve a produção máxima em
#  um determinado ano e a fazenda com a produção mínima no
#  mesmo ano.- Construa seus próprios dados fictícios.
