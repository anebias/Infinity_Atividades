'''
Objetivo: Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês, calcule o salário total e exiba o resultado (Considere que você trabalha 20 dias no mês).

Instruções:
1 - Solicitar o Salário Mensal:
Use a função input() para pedir ao usuário que insira quanto
ele ganha por mês. Converta a entrada do usuário de string
para um número (float) para permitir cálculos.

2 - Solicitar o Número de Horas Trabalhadas na Semana:
Use a função input() para pedir ao usuário que insira o número
de horas trabalhadas na semana. Converta a entrada do
usuário de string para um número (float) para permitir
cálculos.

3 - Calcular o Total de Horas Trabalhadas no Mês:
Multiplique o número de horas trabalhadas na semana por 4
para obter o total de horas trabalhadas no mês.

4 - Calcular o Salário por Hora:
Divida o salário mensal pelo total de horas
trabalhadas no mês para obter o salário por
hora.

5 - Mostrar o Salário por Hora Calculado
para o Usuário:
Use a função print() para exibir o salário por
hora calculado.
'''

salario_mensal = float(input('Informe o valor do salário mensal: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas na semana: '))
dias_trabalhados = 20

total_horas_mes = 4 * horas_trabalhadas

salario_por_hora = salario_mensal / total_horas_mes

print(f'O valor do salário {salario_mensal:.2f} calculado por hora é de R$ {salario_por_hora:.2f} a hora trabalhada.')