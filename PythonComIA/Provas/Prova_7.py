'''[PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total.'''

from random import randint
def lancar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    # teste realizado com exibição no terminal
    # print(f'Lançamento de dados: \ndado 1: {dado1}, \ndado 2: {dado2}')
    return dado1 + dado2

# A função retorna a soma e a chamada da função.
# O exercício não orienta imprimir a soma, mas retornar.
# imprime o valor do lançamento dos dados no terminal.
print(lancar_dados())