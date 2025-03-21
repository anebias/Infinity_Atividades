# 37 - Crie um algoritmo que ao ser executado recebe a velocidade de dois veículos  em km/h
# e exibe no terminal qual dos veículos está se deslocando mais rápido.
# Se algum dos veículos estiver a mais de 80km/hora deve ser exibida a mensagem: "<veiculo> está acima da velocidade permitida"
# Se algum dos veículos estiver parado deve exibir a mensagem: "<veiculo> não está em movimento"

veiculo1 = float(input('Informe a velocidade do primeiro veículo: '))
veiculo2 = float(input('Informe a velocidade do segundo veículo: '))

mais_veloz = 0

if veiculo1 > veiculo2:
    mais_veloz = veiculo1
else:
    mais_veloz = veiculo2

if veiculo1 > 80:
    frase1 = "1 está acima da velocidade permitida"
elif veiculo1 == 0:
    frase1 = "1 não está em movimento"
else:
    frase1 = ""

if veiculo2 > 80:
    frase2 = "1 está acima da velocidade permitida"
elif veiculo2 == 0:
    frase2 = "1 não está em movimento"
else:
    frase2 = ""



