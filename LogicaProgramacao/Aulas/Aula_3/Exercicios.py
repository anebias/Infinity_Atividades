# Condicionais:
# 01 - Crie um algoritmo em que o usuário informe dois números (n1 e n2). Após, exiba na tela (terminal) qual deles é o maior.
print('*** Exercício 1 ***')

numero_1 = float(input('Informe o primeiro número: '))
numero_2 = float(input('Informe o segundo número: '))

if numero_1 > numero_2:
    print(f'O número {numero_1} é maior que {numero_2}.')
elif numero_2 > numero_1:
    print(f'O número {numero_2} é maior que {numero_1}.')
else:
    print(f'Os números {numero_1} e {numero_2} são iguais')

# 02 - Crie um algoritmo em que o usuário informe dois números (n1 e n2). Após, exiba na tela (terminal) qual deles é o menor.
print('*** Exercício 2 ***')

numero_1 = float(input('Informe o primeiro número: '))
numero_2 = float(input('Informe o segundo número: '))

if numero_1 < numero_2:
    print(f'O número {numero_1} é menor que {numero_2}.')
elif numero_2 < numero_1:
    print(f'O número {numero_2} é menor que {numero_1}.')
else:
    print(f'Os números {numero_1} e {numero_2} são iguais')

# 03 - Crie um algoritmo em que o usuário informe seu gênero, sua altura e seu pese. Após, calcule e exiba na tela (terminal) o IMC do usuário.
print('*** Exercício 3 ***')

genero = input('Informe o seu gênero. Digite "F" para feminino e "M" para masculino: ')
altura = float(input('Informe a sua altura: '))
peso = float(input('informe o seu peso: '))

imc = peso / (altura ** 2)

print(f'\nGênero: {genero} \nAltura: {altura} \nPeso: {peso} \nO seu IMC é {imc:.2f}')

# 04 - Crie um algoritmo em que o usuário informe um número qualquer. Após, informe se esse número é par ou ímpar.
print('*** Exercício 4 ***')

numero = float(input('Informe um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')

# 05 - Crie um algoritmo em que o usuário informe um número qualquer. Após, informe se esse número é múltiplo de 2.
print('*** Exercício 5 ***')

numero = float(input('Informe um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é múltiplo de 2')
else:
    print(f'O número {numero} não é múltiplo de 2')

# 06 - Crie um algoritmo em que o usuário informe um número qualquer. Após, informe se esse número é múltiplo de 3.
print('*** Exercício 6 ***')

numero = float(input('Informe um número: '))

if numero % 3 == 0:
    print(f'O número {numero} é múltiplo de 3')
else:
    print(f'O número {numero} não é múltiplo de 3')

# 07 - Crie um algoritmo em que o usuário informe um número qualquer. Após, informe se esse número é múltiplo de 5.
print('*** Exercício 7 ***')

numero = float(input('Informe um número: '))

if numero % 5 == 0:
    print(f'O número {numero} é múltiplo de 5')
else:
    print(f'O número {numero} não é múltiplo de 5')

# 0 : Através do exemplo do contador de letras, crie um algoritmo que exiba cada letra de uma palavra digitada pelo usuário;
print('*** ESTRUTURA WHILE ***')
print('*** Exercício 0 ***')

palavra = input('Digite uma palavra: ')
n = 0
while n < len(palavra):
    print(palavra[n])
    n += 1

# 1 - Crie um algoritmo que receba um número e imprima no terminal todos os valores em ordem crescente até o valor do número informado.
print('*** Exercício 1 ***')

numero = int(input('Informe um número inteiro: '))
n = 1
while n <= numero:
    print(n)
    n += 1

# 2 - Crie um algoritmo que receba um número e imprima no terminal todos os valores em ordem decrescente até o valor do número informado.
print('*** Exercício 2 ***')

numero = int(input('Informe um número inteiro: '))
n = numero
while n >= 1:
    print(n)
    n -= 1

# 3 - Crie um algoritmo que ao receber uma palavra conte o número de letras dessa palavra e imprima esse valor no terminal.
print('*** Exercício 3 ***')

palavra = input('Digite uma palavra: ')

print(f'A palavra "{palavra} possui {len(palavra)} letras')

# 4 - Crie um algoritmo que recebe 5 nomes e imprime no terminal os nomes que se iniciem com uma letra à sua escolha:
# Ex: 'Ana', 'Julia', 'Pedro', 'Amanda', 'Bruno' , letra = "A", a saída no terminal dever ser:
# Ana
# Amanda
# Obs: Se atentem para o uso de letras maiúsculas ou minúsculas

print('*** Exercício 4 ***')

nome1 = input('Digite o primeiro nome: ').capitalize()
nome2 = input('Digite o segundo nome: ').capitalize()
nome3 = input('Digite o terceiro nome: ').capitalize()
nome4 = input('Digite o quarto nome: ').capitalize()
nome5 = input('Digite o quinto nome: ').capitalize()
letra = input('Informe a letra inicial do nome: ').upper()

lista_nomes = [nome1, nome2, nome3, nome4, nome5]
n = 0
while n < len(lista_nomes):
    if letra == lista_nomes[n][0]:
        print(lista_nomes[n])
    n += 1

# 5 - Crie um algoritmo aque receba um número de usuário e informe a soma de todos os números anteriores ao valor informado:
# Ex: 3 , o resultado devera ser: 1 + 2 + 3 = 6 , então no terminal deverá ser exibido o número 6.
print('*** Exercício 5 ***')

numero = int(input('Informe um número inteiro: '))

n = soma = 0

while n <= numero:
    soma += n
    n += 1

print(f'A soma dos números de 1 até {numero} é {soma}')

# 6 - Crie um algoritmo que ao receber uma palavra a reescreve de trás para frente.
print('*** Exercício 6 ***')

palavra = input('Digite uma palavra:')

n = len(palavra)

while n > 0:
    print(palavra[n-1],end = "")
    n -= 1

print()

# 7 - Crie um algoritmo que ao receber um número calcule a tabuada deste número até 10 e exiba cada uma das multiplicações no terminal
# Ex: numero = 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30
print('*** Exercício 7 ***')

numero = int(input('Informe um número inteiro para calcular a tabuada: '))

n = 1
while n <=10:
    print(f'{numero} x {n} = {numero * n}')
    n += 1

# 9 - Crie um algoritmo para que o usuário possa selecionar uma das três opções: "pedra", "papel", "tesoura"
# imprima a opção escolhida pelo usuário. Caso o usuário escolha uma opção inválida exiba a mensagem "Escolha inválida, tente novamente"
# O algoritmo só para sua execução quando o usuário escolher entre uma das opções válidas, exibindo qual opção foi escolhida.
print('*** Exercício 9 ***')

opcao = input('Digie "pedra", "papel" ou "tesoura" :').lower()

while opcao != "pedra" and opcao != "papel" and opcao != "tesoura":
    opcao = input('Escolha inválida, tente novamente: ').lower()

print(f'Opção selecionada foi {opcao}')