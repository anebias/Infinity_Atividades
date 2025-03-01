# # SETS
# meu_set = {'a',1,'meu'}
# print(meu_set)

# # Usando compreensão de conjuntos
# meu_set = {letra for letra in 'Qualquer Palavra ou frase' if letra not in ['a','e','i','o','u']}
# print(meu_set)

# # Método construtor
# meu_set = set(['a',1,'meu'])
# print(meu_set)

# ATIVIDADE PRÁTICA 1
# Crie um conjunto vazio chamado frutas e adicione as
# seguintes frutas a ele: "maçã","banana","uva","laranja" e "morango".
# Em seguida, imprima o conjunto.

# Método construtor para SET. 
# Se colocar {} será criado objeto DICT
frutas = set([])
frutas.add('maça')
frutas.add('banana')
frutas.add('uva')
frutas.add('laranja')
frutas.add('morango')
print(frutas)

# ATIVIDADE PRÁTICA 2
# Verifique se a fruta "banana está presente no conjunto
# frutas e imprima o resultado.

print('banana' in frutas)

# ATIVIDADE PRÁTICA 3
# Crie um conjunto chamado frutas_vermelhas e adicione
# as seguintes frutas a ele:"morango","cereja" e "framboesa". 
# Em seguida, imprima o conjunto.

frutas_vermelhas = set([])
frutas_vermelhas.add('morango')
frutas_vermelhas.add('cereja')
frutas_vermelhas.add('framboesa')

print(frutas_vermelhas)

# ATIVIDADE PRÁTICA 4
# Remova a fruta "cereja" do conjunto frutas_vermelhas e
# imprima o conjunto atualizado.

frutas_vermelhas.remove('cereja')
frutas_vermelhas.add('cereja')
frutas_vermelhas.discard('cereja')
print(frutas_vermelhas)

# ATIVIDADE PRÁTICA 5
# Crie dois conjuntos, A e B, e realize a união dos dois
# conjuntos.

frutas = {'uva', 'maça', 'banana', 'morango', 'laranja'}
frutas_vermelhas = {'framboesa', 'morango', 'cereja'}
todas_frutas = frutas.union(frutas_vermelhas)
print(todas_frutas)

# ATIVIDADE PRÁTICA 6
# Crie um programa que recebe dois conjuntos e exibe a
# interseção deles.


# ATIVIDADE PRÁTICA 7
# Escreva um programa que receba duas listas e calcule
# a união dos elementos únicos dessas listas, usando conjuntos.