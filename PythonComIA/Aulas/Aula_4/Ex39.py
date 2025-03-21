# 39 - Desafio: Crie um algoritmo para calcular a velocidade de um veículo
# o calculo da velocidade é: velocidade = distância/tempo 
# os valores devem ser recebidos através de inputs.
# Caso valores não númericos sejam recebidos o deve ser exibida uma mensagem de erro:
# "Os valores inseridos não são números"
# Caso valores corretos sejam informados o algoritmo deve imprimir o valor da velocidade calculada.

distancia = input('Informe a distância percorrida: ')
tempo = input('Informe o tempo: ')

if not distancia.isnumeric() or not tempo.isnumeric():
    print('Os valores recebidos não são numéricos')
elif tempo == '0':
    print('O tempo não pode ser nulo')
else:
    velocidade = float(distancia)/float(tempo)
    print(f'A velocidade do veículo é {velocidade:.2f} km/h')