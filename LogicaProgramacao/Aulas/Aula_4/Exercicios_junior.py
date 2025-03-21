# For Loop - Contagem Progressiva: Crie um programa que utiliza o loop for para imprimir uma contagem de 10 a 30.
for i in range(10,31):
    print(i)

# While Loop - Contagem Regressiva: Faça um programa que utiliza o loop while para imprimir uma contagem regressiva de 10 a 1.
numero = 10
while numero > 0:
    print(numero)
    numero -= 1

# For Loop - Soma Pares: Crie um programa que utiliza o loop for para calcular a soma dos números pares de 1 a 50.
soma = 0
for i in range(1,51):
    if i % 2 == 0:
        soma += i
print(f'A soma dos números é {soma}')

# While Loop - Fatorial: Implemente um programa que calcula o fatorial de um número usando o loop while.
numero = int(input('Informe um número: '))
fatorial = 1

while numero > 0:
    fatorial *= numero
    numero -= 1

print(fatorial)

# For Loop - Quadrados: Utilize o loop for para imprimir os quadrados dos números de 1 a 20.
for i in range(1,21):
    print(i ** 2)

# While Loop - Soma Ímpares: Implemente um programa que utiliza o loop while para calcular a soma dos números ímpares de 1 a 50.
numero = 50
soma = 0

while numero > 0:
    if numero % 2 == 1:
        soma += numero

print(f'A soma dos ímpares entre 1 e 50 é {soma}')

# For Loop - Tabuada: Crie um programa que utiliza o loop for para exibir a tabuada de multiplicação de um número fornecido pelo usuário.
numero = int(input('Informe um número: '))
for i in range (1,11):
    print (f' {i} x {numero}  = {numero * i}')

# While Loop - Faça um programa que irá pedir nome e altura de pessoas, após cada inserção deve perguntar se o usuário quer continuar ('S' para sim e 'N' para não). Ao final, mostre o nome da pessoa mais alta.    
seguir = 's'
altura_maxima = 0
nome_altura_maxima = ""

while seguir == 's':
    nome = input('Informe o nome: ')
    altura = float(input('Informe a altura: '))
    seguir = input('Informe "s" para seguir e "n" para sair: ')
    if altura > altura_maxima:
        altura_maxima = altura
        nome_altura_maxima = nome

print(f'{nome_altura_maxima} tem a maior altura e é igual a {altura_maxima}')


