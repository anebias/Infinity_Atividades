#*Pleno*
# While Loop - Média de Números: Escreva um programa que pede ao usuário para inserir números inteiros, e ao digitar zero, calcula e imprime a média dos números inseridos usando o loop while.
soma = numero = int(input('Informe um número inteiro: '))
contador = 1

while numero != 0:
    numero = int(input('Informe um número inteiro: '))
    soma += numero
    contador += 1

print(f'A média dos {contador - 1} números informados é {soma / (contador - 1):.2f}')

# For Loop - Verificação de Palíndromo: Faça um programa que utiliza o loop for para verificar se uma palavra fornecida pelo usuário é um palíndromo.
palavra = input('Informe uma palavra: ')
palavra_invertida = ""
quantidade_letras = len(palavra)

for i in range(quantidade_letras -1,-1,-1):
    palavra_invertida += palavra[i]

print(palavra_invertida)

# While Loop - FizzBuzz: Faça um programa que utiliza o loop while para mostrar na tela uma contagem de 1 a 100. Durante a contagem, caso o numero seja divisível por 3 você mostrará "Fizz" no lugar, caso o numero seja divisível por 5 você mostrará "Buzz" no lugar, caso ele seja divisível por 3 e por 5 você mostrará "FizzBuzz" no lugar.
i = 1
while i <= 100:
    print(i)
    if i % 3 == 0  and i % 5 == 0:
        print('FizBuzz')
    elif i% 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    i += 1

# For Loop - Contagem de Consoantes: Faça um programa que utiliza o loop for para contar o número de consoantes em uma frase fornecida pelo usuário.

frase = input('Digite uma frase: ')
quantidade_caracteres = len(frase)
contador = 0

for i in range(quantidade_caracteres):
    if frase[i] != 'a' and frase[i] != 'e' and frase[i] != 'i' and frase[i] != 'o' and frase[i] != 'u' and frase[i] != ' ':
        contador += 1

print(f'A frase {frase} tem {contador} consoantes')

# While Loop - Números Primos: Implemente um programa que solicita ao usuário um número e verifica se ele é um número primo usando o loop while.

numero = int(input('Informe um número: '))



# For Loop - Números de Armstrong: Implemente um programa que utiliza o loop for para imprimir todos os números de Armstrong de 1 a 1000.


# While Loop - Contagem de Vogais: Faça um programa que utiliza o loop while para contar o número de vogais em uma frase fornecida pelo usuário.


# For Loop - Números Primos no Intervalo: Crie um programa que utiliza o loop for para imprimir todos os números primos no intervalo de 1 a 100.
