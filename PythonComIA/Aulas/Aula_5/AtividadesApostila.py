# * args - armazena em tupla
# ** kwargs - armazena em dicionario

# # exemplo:
# def somar_numeros(*args):
#     resultado = 0
#     for num in args:
#         resultado += num
#     return resultado

# def mostrar_info(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f'{chave}: {valor}')

# mostrar_info(nome='João', idade=30, cidade='Belo Horizonte')

# def minha_funcao(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for chave, valor in kwargs.items():
#         print(f'{chave}: {valor}')

# minha_funcao("Curriculo","Desenvolvedor",nome = "Alessandra", idade = 50)

# ## Funções Lambda
# # sintaxe: lambda parâmetros: comando

# # Exemplo:
# quadrado = lambda x : x**2
# print(quadrado(5))

# par = lambda x: x % 2 == 0
# print(par(10), par(11))

# name_uppercase = lambda n : n.upper()
# print(name_uppercase('alessandra'))

# par_impar = lambda x : "par" if x % 2 == 0 else "impar"
# print(par_impar(2),par_impar(3))

# valida_usuarios = lambda user : "Erro: usuario precica ser definido " if user in ' ' else ("usuário não pode ter menos de 4 dígitos" if len(user) < 4 else "usuario definido com sucesso")

# print(valida_usuarios(''))
# print(valida_usuarios(' '))
# print(valida_usuarios('ale'))
# print(valida_usuarios('aless'))
# print(valida_usuarios('.'))

#  A função map() recebe uma função e uma sequência (como uma lista) como
#  argumentos e aplica a função a cada elemento da sequência. Ela retorna um objeto map
#  que pode ser convertido em uma lista, se necessário. A função map() é útil quando você
#  deseja aplicar uma determinada operação a todos os elementos de uma sequência.
#  Exemplo usando map() com uma função lambda

numeros = [1,2,3,4,5,6,7,8,9]
quadrados = list(map(lambda x : x ** 2, numeros))
print(quadrados)

# A função reduce() está disponível no módulo functools e recebe 
# uma função e uma sequência como argumentos. Ela aplica a função cumulativamente
#  aos elementos da sequência, de modo que cada aplicação sucessiva usa o resultado da
#  aplicação anterior. Ela retorna um único valor como resultado final

from functools import reduce
numeros = [1,2,3,4,5,6,7,8,9]
soma = reduce(lambda x, y : x + y, numeros)
print(soma)

# ATIVIDADE PRÁTICA 1
#  Crie um programa que solicita ao usuário que insira três
#  notas e, em seguida, calcule a média dessas notas
#  usando uma função. A função deve receber as três
#  notas como argumentos e retornar a média. Por fim, o
#  programa deve imprimir a média calculada



# ATIVIDADE PRÁTICA 2
#  Crie um programa que define uma função
#  calcular_area_retangulo que recebe dois argumentos,
#  comprimento e largura de um retângulo, e retorna a
#  área desse retângulo. Em seguida, o programa deve
#  solicitar ao usuário que insira o comprimento e a
#  largura e imprimir a área calculada



# ATIVIDADE PRÁTICA 3
#  Crie uma função chamada concatenar_strings que
#  aceita um número variável de strings como argumentos
#  posicionais (usando *args). A função deve concatenar
#  todas as strings em uma única string e retorná-la.


# ATIVIDADE PRÁTICA 4
#  Crie uma função que aceita uma lista de números e use
#  a função map para retornar uma nova lista contendo o
#  dobro de cada número na lista de entrada.


# ATIVIDADE PRÁTICA 5
#  Crie uma função que aceita uma lista de números e use
#  a função filter para retornar uma nova lista contendo
#  apenas os números pares da lista de entrada


# ATIVIDADE PRÁTICA 6
#  Crie uma função que aceita uma lista de strings e use a
#  função reduce (importada de functools) para encontrar
#  a maior string na lista.


# ATIVIDADE PRÁTICA 7
#  Crie uma função chamada criar_lista_de_compras que
#  aceita um número variável de itens de compras como
#  argumentos posicionais (usando *args). A função deve
#  criar e retornar uma lista de compras que contenha
#  todos os itens fornecidos


# ATIVIDADE PRÁTICA 8
#  Crie uma função que aceite dois números e uma
#  operação (por exemplo, adição, subtração,
#  multiplicação, divisão) como argumentos e use funções
#  lambda para realizar a operação especificada. A função
#  deve retornar o resultado da operação.


# DESAFIO PRÁTICO
#  Processador de Texto - passo 1
#  Crie um processador de texto simples que realiza várias operações
#  em um texto de entrada, como contar palavras, contar letras,
#  inverter o texto e substituir palavras-chave.
#  Requisitos:
#  Crie uma função chamada processador_texto que aceite uma
#  string de texto como argumento


# DESAFIO PRÁTICO
#  Processador de Texto - passo 2
#  A função deve aceitar uma série de operações como argumentos
#  de palavra-chave, usando **kwargs. As operações podem incluir
#  "contar_palavras", "contar_letras", "inverter_texto" e
#  "substituir_palavra".
#  Use funções lambda para realizar as operações de acordo com
#  as palavras-chave especificadas nos argumentos de palavra
# chave


# DESAFIO PRÁTICO
#  Processador de Texto - passo 3
#  Se a operação "substituir_palavra" for especificada, a função
#  deve aceitar uma palavra-chave adicional, como
#  "substituir_palavra" e "nova_palavra", para realizar a
#  substituição em todo o texto.
#  A função deve retornar o texto resultante após todas as
#  operações