# ATIVIDADE PRÁTICA 1
#  Crie uma função que receba um nome e imprima uma
#  saudação personalizada.

# def saudacao(nome):
#     print(f'Olá {nome}! Seja muito bem vindo!')

# saudacao(input('Informe o seu nome: '))

# ATIVIDADE PRÁTICA 2
#  Crie uma função que receba um horário e imprima "Bom
#  dia!", "Boa tarde!" ou "Boa noite!" conforme o horário

# def cumprimento(horario):
#     '''
#     A função recebe um horário no formato hh:mm e retorna:
#     "Bom dia!", "Boa tarde!" ou "Boa noite" na tela.
#     '''
#     mensagem = ''
    
#     if ":" in horario:
#         posicao_separador = horario.index(':')
#         horario = horario[:posicao_separador]

#     if horario.isnumeric():
#         if len(horario) in [1,2]:
#            hora = int(horario)
#         else:
#             return 'Horário inválido'
#     else:
#         return 'Horário inválido'
    
#     if hora >= 0 and hora < 12:
#         mensagem = 'Bom dia!'
#     elif hora >= 12 and hora < 18:
#         mensagem = 'Boa tarde!'
#     elif hora >= 18 and hora < 24:
#         mensagem = 'Boa noite!'
#     else:
#         return 'Horário inválido'
    
# #     return print(mensagem)

# # cumprimento(input('Informe um horário: '))   

# # ATIVIDADE PRÁTICA 3
# #  Crie uma função que receba dois números e retorne a
# #  soma deles

# def soma(num1,num2):

#     if num1.replace('.','').isnumeric() and num2.replace('.','').isnumeric():
#         return float(num1) + float(num2)
#     else:
#         return 'Valores inválidos'

# print(soma('2.1','3.4'))

# # ATIVIDADE PRÁTICA 4
# #  Crie uma função que receba dois números e retorne a
# #  subtração do primeiro pelo segundo.

# def subtracao(num1,num2):

#     if num1.replace('.','').isnumeric() and num2.replace('.','').isnumeric():
#         return float(num1) - float(num2)
#     else:
#         return 'Valores inválidos'

# print(subtracao('2.1','3.4'))

# # ATIVIDADE PRÁTICA 5
# #  Crie uma função que receba dois números e retorne a
# #  multiplicação deles.

# def multiplicacao(num1,num2):

#     if num1.replace('.','').isnumeric() and num2.replace('.','').isnumeric():
#         return float(num1) * float(num2)
#     else:
#         return 'Valores inválidos'

# print(multiplicacao('2.1','3.4'))

# def divisao(num1,num2):

#     if num2 == '0':
#         return 'Não é possível dividir por zero'
#     elif num1.replace('.','').isnumeric() and num2.replace('.','').isnumeric():
#         return float(num1) / float(num2)
#     else:
#         return 'Valores inválidos'

# print(divisao('2.1','0'))

# # DESAFIO PRÁTICO
# #  Calculadora
# #  Crie uma calculadora com opções de soma, multiplicação,
# #  subtração, divisão e sair.
# #  (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)
# #  Utilize funções de rotina para cada operação e funções de unidade lógica para
# #  realizar os cálculos.
# #  Dica:
# #  Utilize de condicionais e Laços de Repetição para realizar esse exercício

# while True:
#     print('CALCULADORA')
#     print('1 : Somar dois números')
#     print('2 : Subtrair dois números')
#     print('3 : Multiplicar dois números')
#     print('4 : Dividir dois números')
#     print('5 : Sair')

#     opcao = input('Informe a opção desejada: ')

#     if opcao == '1':
#         num1 = input('Informe o primeiro número: ')
#         num2 = input('Informe o segundo número: ')
#         print(f'{num1} + {num2} =',soma(num1, num2))
    
#     elif opcao == '2':
#         num1 = input('Informe o primeiro número: ')
#         num2 = input('Informe o segundo número: ')
#         print(f'{num1} - {num2} =',subtracao(num1, num2))

#     elif opcao == '3':
#         num1 = input('Informe o primeiro número: ')
#         num2 = input('Informe o segundo número: ')
#         print(f'{num1} * {num2} =',multiplicacao(num1, num2))

#     elif opcao == '4':
#         num1 = input('Informe o primeiro número: ')
#         num2 = input('Informe o segundo número: ')
#         print(f'{num1} / {num2} =',divisao(num1, num2))

#     elif opcao == '5':
#         break

#     else:
#         print('Opção inválida. Tente novamente.')