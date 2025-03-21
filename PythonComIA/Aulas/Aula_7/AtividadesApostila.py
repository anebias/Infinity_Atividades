# Um módulo é um arquivo Python
#  contendo funções, classes e variáveis.
#  Você pode criar seus próprios módulos
#  escrevendo código Python em um
#  arquivo com extensão .py.
#  Para usar um módulo em outro
#  programa, você importa-o usando a
#  instrução import.

# Criamos uma função chamada saudacao que possui o parâmetro nome,  no arquivo meu_modulo.py

# No arquivo meu_arquivo importamos o meu_modulo. Criamos uma variável mensagem que armazena a chamada do arquivo meu_modulo e busca a função saudacao que espera um argumento como resposta.

# import meu_modulo

# mensagem = meu_modulo.saudacao('Alessandra')
# print(mensagem)

# import modulo
# Uma advertência, importar um módulo desta
#  maneira traz pra gente TODAS AS FUNÇÕES daquele
#  módulo, ou seja, se neste módulo existirem 100
#  funções, essa maneira de import traz todas as 100
#  funções

#  from modulo import função
#  Realizando o import desta maneira
#  temos o cuidado de importar apenas
#  a função que queremos, evitando
#  importar todas as funções daquele
#  módulo.

# from modulo import (func1, func2)
#  Quando queremos ou precisamos
#  importar mais de uma função, devemos
#  importar todas as funções dentro de uma
#  tupla, seguindo o padrão de estilização de
#  código do Python - PEP 8.

# from modulo import *
#  Nesta maneira importamos tudo o
#  que existe no módulo, basicamente
#  como a primeira maneira

# from pacote.modulo import função
#  Dessa maneira podemos importar uma função
#  de um módulo que está em um pacote externo,
#  ou seja, quando o módulo e o arquivo onde o
#  módulo será importado não estão na mesma
#  pasta

#  import modulo as apelido
#  Em algum momento podemos lidar com nomes
#  de módulos grandes, para não termos que digitar
#  nomes grandes todas as vezes que vamos utilizar
#  alguma função daquele módulo, damos um
#  apelido (alias) para este módulo, através da
#  palavra as

# ATIVIDADE PRÁTICA 1
#  Crie um programa que será uma calculadora.
#  Nesta calculadora você deverá ter um módulo para as
#  operações matemáticas, o arquivo principal deverá
#  conter apenas um menu de escolha para o usuário
#  (soma, subtração, multiplicação e divisão). 

# Resolvido na pasta CALCULADORA

# ATIVIDADE PRÁTICA 2
#  Crie um módulo chamado manipulacao_strings que
#  contenha funções para realizar operações com strings,
#  como inverter uma string, contar o número de palavras
#  em uma string e verificar se uma string é um
#  palíndromo (lê-se igual de trás para frente). Crie 
# um programa principal que importe o módulo e use
#  essas funções com strings fornecidas pelo usuário

# Resolvido na pasta MANIPULACAO_STRINGS

# BIBLIOTECAS:

#  ATIVIDADE PRÁTICA 3
#  Crie um programa que permite ao usuário calcular a
#  área e operímetro de formas geométricas simples,
#  como quadrados, retângulos e círculos. Use funções
#  matemáticas do módulo math para realizar os cálculos.

# import math

# def area_quadrado(lado):
#     return math.pow(lado,2)

# def area_retangulo(lado, altura):
#     return lado * altura

# def area_circulo(raio):
#     return math.pi * math.pow(raio,2)

# def perimetro_quadrado(lado):
#     return lado * 4

# def perimetro_retangulo(lado, altura):
#     return 2*lado + 2*altura

# def perimetro_circulo(raio):
#     return 2 * math.pi * raio


# ATIVIDADE PRÁTICA 4
#  Desenvolva um jogo de adivinhação em que o programa
#  escolhe um número aleatório e desafia o jogador a
#  adivinhá-lo. Forneça dicas ao jogador, indicando se o
#  número é maior ou menor do que a adivinhação atual.

# Resolvido na pasta JOGO_ADVINHACAO

# ATIVIDADE PRÁTICA 5
#  Desenvolva um programa que permita ao usuário
#  converter entre diferentes unidades de medida, como
#  metros para pés, quilogramas para libras, ou Celsius
#  para Fahrenheit. Use módulos que contenham funções
#  de conversão.


# DESAFIO PRÁTICO
#  Gerenciador de Livros de Biblioteca - passo 1
#  Crie um programa que permita aos usuários:
#  Adicionar novos livros à biblioteca, com informações como título,
#  autor e número de cópias disponíveis.
#  Listar todos os livros disponíveis na biblioteca.
#  Permitir aos usuários fazer empréstimos de livros, reduzindo o
#  número de cópias disponíveis quando um livro é emprestado.


# DESAFIO PRÁTICO
#  Gerenciador de Livros de Biblioteca - passo 2
#  Permitir aos usuários devolver livros, aumentando o número de
#  cópias disponíveis quando um livro é devolvido.
#  Verificar a disponibilidade de um livro específico na biblioteca.
#  Mostrar a lista de livros emprestados a um usuário específico.
