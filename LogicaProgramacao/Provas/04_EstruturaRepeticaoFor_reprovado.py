'''
[LPIA-A04] Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).

Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

Ao final, exiba a soma dos números pares encontrados.
'''

# O exercício não deixa claro se é para considerar apenas números positivos, então não coloquei restrição sobre esse critério.

numero_1 = int(input('Informe o número inicial do intervalo:'))
numero_2 = numero_1 - 1
soma = 0

print('estou aqui')
while numero_2 < numero_1:
    numero_2 = int(input('Informe o número final do intervalo:'))

for numero in range(numero_1,numero_2 + 1):
    if numero_2 - numero_1 > 1:
        if numero % 2 == 0:
            soma = soma + numero
            mensagem = f'soma: {soma}'
    else:
        mensagem = 'Não existem números pares no intervalo informado'
        break

print(mensagem)
