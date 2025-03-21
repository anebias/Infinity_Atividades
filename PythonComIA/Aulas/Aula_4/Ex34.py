
# 34 - Crie um algoritmo que ao ser executado recebe dois valores númericos
# e imprime qual é o maior dos dois valores.

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))
maior = numero1

if numero1 > numero2:
    maior = numero1
elif numero2 > numero1:
    maior = numero2
else:
    print(f'Os números {numero1} e número {numero2} são iguais')
    

print(f'O número {maior} é o maior dos dois números informados')