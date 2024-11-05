'''
Atividade 09:
Verificar Par ou Ímpar:
Crie um programa que peça ao usuário um número e use a
estrutura condicional if para verificar se ele é par ou ímpar.
'''
numero = int(input('Informe um número inteiro: '))

if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')

'''
Atividade 10:
Verificar Nota para Aprovado:
Crie um programa que peça a nota de um aluno e
use if para verificar se ele foi aprovado (nota >= 6).
'''
nota = int(input('Informe a sua nota: '))

if nota >= 6:
    print(f'Você foi aprovado com nota {nota}')
else:
    print(f'Você foi reprovado com nota {nota}')

'''
Atividade 11:
Verificar Par ou Ímpar e Positivo ou Negativo:
Escreva um programa que peça um número e use if para verificar
se ele é par ou ímpar e também se é positivo ou negativo.
'''

numero = int(input('Informe um número inteiro: '))
paridade = ""
sinal = ""

if numero == 0:
    sinal = "nulo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "positivo"

if numero % 2 == 0:
    paridade = "par"
else:
    paridade = "impar"

print(f'O número {numero} é {paridade} e {sinal}')

'''
Atividade 12:
Verificar Classificação de IMC:
Crie um programa que calcule o Índice de Massa Corporal (IMC) e use if para classificar o resultado em "Abaixo do peso", "Peso normal", "Sobrepeso" e "Obesidade".
'''

peso = float(input('Informe o seu peso:'))
altura = float(input('Informe a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    resultado = "Abaixo do peso"
elif imc < 25:
    resultado = "Peso Normal"
elif imc < 30:
    resultado = "Sobrepeso"
else:
    resultado = "Obesidade"

print('Resultado:', resultado)

'''
Atividade 13:
Sistema de Login Simples:
Desenvolva um programa que peça ao usuário um nome de usuário
e uma senha e use if para verificar se são iguais a "admin" e "1234",
respectivamente.
'''

usuario_acesso = 'admin'
senha_acesso = '1234'

usuario = input('Informe o usuário: ')
senha = input('Informe a senha: ')

if usuario == usuario_acesso and senha == senha_acesso:
    print('Usuário e senha corretos')
else:
    print('usuário e/ou senha inválido')


'''
Atividade 14:
Verificar Status de Taxa de Desconto:
Crie um programa que peça ao usuário o preço original de um produto e
a quantidade comprada. Use if para verificar se a quantidade é maior que
10 para aplicar um desconto de 10% sobre o total.
'''

preco = float(input('Informe o preço do produto: '))
quantidade = int(input('Informe a quantidade comprada: '))
taxa_desconto = 0.1

if quantidade > 10:
    valor_compra = (1-taxa_desconto) * preco * quantidade
else:
    valor_compra = preco * quantidade

print(f'O valor da compra foi: R$ {valor_compra: .2f}')