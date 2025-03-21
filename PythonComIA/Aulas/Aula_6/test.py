from random import choice

def regras():
    print ('*'*5,'Bem Vindo ao Jogo Pedra, Papel e Tesoura','*'*5,end='\n\n')
    print ('*'*5,'Regras','*'*5)
    print ('Escolha uma das opções abaixo na sua jogada:', end='\n')
    print('1.Pedra \n2.Papel \n3.Tesoura \n')
    print ('*'*5,'Vencedores','*'*5)
    print ('Pedra x Papel = Papel \nPedra x Tesoura = Pedra \nPapel x Tesoura = Tesoura',end='\n\n')


def escolha_jogador(nome):
    print(f'{nome}, escolha uma opção: ')
    print('1.Pedra \n2.Papel \n3.Tesoura \n')

    escolha_user = input('Pedra, papel ou tesoura: ').lower()

    if escolha_user not in {'1','2','3','pedra','papel','tesoura'}:
        print('\nopção inválida!\n')
        escolha_jogador(nome)
    elif escolha_user in {'1','pedra'}:
        return 1
    elif escolha_user in {'2','papel'}:
        return 2
    else:
        return 3


def escolha_computador():
    return choice([1,2,3])


def disputa(escolha_user,escolha_pc):
    if escolha_user == escolha_pc:
        return 'vocês empataram'
    elif (escolha_user == 1 and escolha_pc == 3) or (escolha_user == 2 and escolha_pc == 1) or (escolha_user == 3 and escolha_pc == 2):
        return 'você ganhou a máquina !'
    else:
        return 'a máquina venceu !'
    

def jogada():
    partidas = 0
    partidas_vencedoras = 0
    partidas_empatadas = 0
    regras()
    nome = input('Informe o seu nome: ').capitalize()
    while True:
        partidas +=1
        res_jogador = escolha_jogador(nome)
        res_computador = escolha_computador()
        print(f'{nome} escolheu {res_jogador} e máquina escolheu {res_computador}\n')
        resultado = disputa(res_jogador,res_computador)

        if resultado == 'você ganhou a máquina !':
            partidas_vencedoras +=1
        elif resultado == 'vocês empataram':
            partidas_empatadas +=1

        print(f'Resultado da competição: {nome}, {resultado}\n')

        if not nova_partida:
            break

    print(f'Resultado da competição de {nome} versus máquina: \n - {nome} venceu: {partidas_vencedoras}\n - Máquina venceu: {partidas-partidas_empatadas-partidas_vencedoras}\n - Empates: {partidas_empatadas}\n - Total: {partidas}')

def nova_partida():
        continuar = input('Deseja continuar (S)? ').lower()
        if continuar[0] != 's':
            print('\n','*'*5 ,'Jogo encerrado !','*'*5)
        else:
            jogada()

def tipo_partida():
    print('\nESCOLHA DO TIPO DE PARTIDA')
    print('*'*5,'Tipos de Partida','*'*5,'\n1. Melhor de 3 \n2. Melhor de 5 \n3. Decidir quando parar \n')
    tipo = input('Escolha o tipo da Partida (1, 2 ou 3): ')
    
    if tipo[0] not in {'1','2','3'}:
        print('opção inválida! Informe o número correspondente à sua escolha!')
        tipo_partida()
    
    return tipo[0]

def abertura_jogo():
    regras()    
    tipo_partida()

    if tipo_partida == 1:
        continue
    elif tipo_partida == 2:
        continue
    else:
        jogada()

    print ('*'*5,'Início','*'*5)

tipo_partida()  
# jogada()