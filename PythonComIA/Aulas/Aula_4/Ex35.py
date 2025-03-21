# 35 - Crie um algoritmo que recebe três números e compare cada desses números e imprima: 
# Para o menor número a mensagem: "<numero1> é o menor entre os números fornecidos"
# Para o número intermediário: "<numero2> está entre <numero2> e <numero3>"
# Para o maior número: "<numero3> é o maior entre os números"

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))
numero3 = float(input('Informe o terceiro número: '))

menor = 0
meio = 0
maior = 0

# Definir o menor:
if numero1 < numero2 and numero1 < numero3:
    menor = numero1

elif numero2 < numero1 and numero2 < numero3:
    menor = numero2

else:
    menor = numero3

print(f'{menor} é o menor entre os números fornecidos')

# Definir o maior:
if numero1 > numero2 and numero1 > numero3:
    maior = numero1

elif numero2 > numero1 and numero2 > numero3:
    maior = numero2

else:
    maior= numero3

print(f'{maior} é o maior entre os números fornecidos')

# Definir o meio:
if numero1 != menor and numero1 != maior:
    meio = numero1
elif numero2 != menor and numero2 != maior:
    meio = numero2
else:
    meio = numero3

print(f'{meio} está entre {menor} e {maior}')

