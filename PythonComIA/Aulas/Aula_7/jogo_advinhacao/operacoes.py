import numero

def maior_menor(num_chute):
    if num_chute < numero.numero:
        print(f'O número {num_chute} está baixo !')
    else:
        print(f'O número {num_chute} está alto !')

def verificar_numero(num_chute):
    if numero.numero == num_chute:
        print(f'Parabéns !! Você acertou ! O número é {numero.numero} ')
        return True
    else:
        print('...', end=" ")
        maior_menor(num_chute)
        return False

def chutar():
    numero_jogador = input('Chute: ')
    numero_jogador = int(numero_jogador)
    if not verificar_numero(numero_jogador):
        chutar()

