'''
[LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número.

Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.
'''

# O exercício não deixa claro se tem algum intervalo para definir o número da advinhação. Considerei o intervalo de números entre 1 e 10, inclusive.

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