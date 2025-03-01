# # Faça a definição de uma lista contendo os números de 1
# # até 5. Finalmente, utilize o print() para exibir os valores
# # da lista.

# lista = [1,2,3,4,5]
# print(lista)

# # Faça a definição de uma lista contendo as vogais.
# # Finalmente, utilize o print() para exibir os valores da lista.
# lista_vogais = ['a','e','i','o','u']
# print(lista_vogais)

# # Defina uma lista com 5 itens que tenha, pelo menos, 3
# # classes diferentes. Utilize o print() para exibir o
# # terceiro elemento dessa lista.

# lista_mista = [1,'Ana',3.7,[1,2]]
# print(lista_mista[2])

# Manipulação de listas:
# append - adiciona
# insert - insere o elemento na posição informada
# remove - remove o elemento pelo seu valor
# pop - remove o elemento pelo seu índice

#TUPLAS
# Crie uma tupla para representar as informações de três
# palestrantes, cada uma contendo o nome, o tema da
# palestra e a instituição à qual estão vinculados.
# Exiba na tela as informações do terceiro palestrante,
# incluindo nome, tema da palestra e instituição.

# palestrantes = ('Palestrante 1, tema 1, instituição 1',
#                 'Palestrante 2, tema 2, instituição 2',
#                 'Palestrante 3, tema 3, instituição 3')

# print(palestrantes[2])

# DESAFIO PRÁTICO
# Suponha que você está gerenciando uma competição esportiva e tem
# uma lista de tuplas representando os resultados das equipes em
# diferentes modalidades. Cada tupla contém o nome da equipe, seguido
# por uma lista de pontuações obtidas em cada rodada da competição.
# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a classificação final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a
# mais baixa.

resultados = [
    ('equipe A',[2,7.4,8]),
    ('equipe B',[9,4.7,10]),
    ('equipe C', [8, 3,10]),
    ('equipe D', [7.6,5,9]),
]
medias = []
classificacao = []

for item in resultados:
    media = 0
    soma = 0
    for i in item[1]:
        soma += i
    media = soma / len(item[1])
    medias.append(media)
    classificacao.append((item[0],media))
print(medias)
print(classificacao)

# Resposta CHATGPT:
# sort()
# É um método de lista que ordena os elementos no lugar, ou seja, altera diretamente a lista original.
# Ordena por padrão em ordem crescente.
# Pode ser configurado para ordenação personalizada
# Com parâmetro reverse: numeros.sort(reverse=True)
# Com função de chave (key): palavras = ["maçã", "banana", "kiwi", "abacaxi"]
# palavras.sort(key=len)  # Ordena por tamanho das palavras
# print(palavras)  # Saída: ['kiwi', 'maçã', 'banana', 'abacaxi']
# print(numeros)  # Saída: [9, 5, 4, 3, 1, 1]
# sorted()
# É uma função embutida que retorna uma nova lista ordenada sem modificar a lista original.
# Tem os mesmos parâmetros que sort()

medias_ordenadas = sorted(medias,reverse=True)
print(medias_ordenadas)

ordenacao_equipes = []

for i in medias_ordenadas:
    for j in range(len(medias)):
        if i == medias[j]:
            ordenacao_equipes.append(j)

print("*** CLASSIFICAÇÃO ***",end="\n")

for i in ordenacao_equipes:
    print(f'{classificacao[i][0]} - média {classificacao[i][1]:.2f}')