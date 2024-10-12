numero_advinhar = 8
tentativa = 3

print('Advinhe qual é o número entre 1 e 10. Você terá 3 chances para advinhar.')

while tentativa > 0:

    numero_jogador = int(input('Informe o número: '))
    acertou = numero_jogador == numero_advinhar
    if acertou:
        print('Parabéns !! Você acertou o número !!')
        break
    elif not acertou and tentativa == 1:
        print('Infelizmente não foi dessa vez !')
    tentativa -= 1