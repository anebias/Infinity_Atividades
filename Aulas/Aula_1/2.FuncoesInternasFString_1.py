'''
Objetivo: Criar um Programa que Peça as 4 Notas
Bimestrais e Mostre a Média

Instruções:

1 - Solicitar as Notas do Usuário:
Use a função input() para pedir ao usuário que insira
cada uma das quatro notas bimestrais. Converta a
entrada do usuário de string para um número (float)
para permitir cálculos.

2 - Calcular a Média das Notas:
Some as quatro notas e divida o resultado
por quatro para obter a média.

3 - Mostrar a Média Calculada para o Usuário:
Use a função print() para exibir a média das notas
calculada.
'''

nota_1 = float(input('Informe a 1ª nota: '))
nota_2 = float(input('Informe a 2ª nota: '))
nota_3 = float(input('Informe a 3ª nota: '))
nota_4 = float(input('Informe a 4ª nota: '))

media_notas = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'A média das notas {nota_1:.2f}, {nota_2:.2f}, {nota_3:.2f} e {nota_4:.2f} foi {media_notas:.2f}.')