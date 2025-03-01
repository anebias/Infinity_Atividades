from random import choice

def regras():
    print ('\n','*'*5,'Seguem as Regras das partidas','*'*5)
    print ('Quando for solicitado, escolha uma das opções abaixo:', end='\n')
    print('1.Pedra \n2.Papel \n3.Tesoura \n')
    print ('*'*5,'Segue a regra para definição do vencedor de cada partida:','*'*5)
    print ('Pedra x Papel = Papel \nPedra x Tesoura = Pedra \nPapel x Tesoura = Tesoura',end='\n\n')
    print ('*'*5,'VAMOS COMEÇAR...','*'*5)

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

def disputa(nome, escolha_user,escolha_pc):
    if escolha_user == escolha_pc:
        resultado = 'empate'
    elif (escolha_user == 1 and escolha_pc == 3) or (escolha_user == 2 and escolha_pc == 1) or (escolha_user == 3 and escolha_pc == 2):
        resultado = 'jogador'
    else:
        resultado = 'maquina'
    print(f'{nome} escolheu {escolha_user} e máquina escolheu {escolha_pc}\n')
    print(f'Resultado da partida: {resultado}\n')
    return resultado

def tipo_partida():
    print('\nESCOLHA DO TIPO DE PARTIDA')
    print('*'*5,'Tipos de Partida','*'*5,'\n1. Melhor de 3 \n2. Melhor de 5 \n3. Decidir quando parar \n')
    tipo = input('Escolha o tipo da Partida (1, 2 ou 3): ')
    
    if tipo[0] not in {'1','2','3'}:
        print('opção inválida! Informe o número correspondente à sua escolha!')
        tipo_partida()
    
    return tipo[0]

def nova_partida():
        continuar = input('Deseja continuar (S)? ').lower()
        if continuar[0] != 's':
            print('\n','*'*5 ,'Jogo encerrado !','*'*5)
            return False
        else:
            return True
        
def abertura_jogo():
    partidas = 0
    partidas_vencedoras = 0
    partidas_empatadas = 0

    print('\n','*'*5, 'Seja bem vindo ao JOGO PEDRA, PAPEL E TESOURA !','*'*5,'\n')
    nome = input('Para começar, me fale como gostaria de ser chamado: ').capitalize()
    regras()
    tipo = tipo_partida()

    if tipo == '1':
        for i in range(3):
            partidas,partidas_vencedoras,partidas_empatadas = placar(partidas,partidas_vencedoras,partidas_empatadas,disputa(nome,escolha_jogador(nome),escolha_computador()))
    elif tipo == '2':
        for i in range(5):
            partidas,partidas_vencedoras,partidas_empatadas = placar(partidas,partidas_vencedoras,partidas_empatadas,disputa(nome,escolha_jogador(nome),escolha_computador()))
    else:
        while nova_partida():            
            partidas,partidas_vencedoras,partidas_empatadas = placar(partidas,partidas_vencedoras,partidas_empatadas,disputa(nome,escolha_jogador(nome),escolha_computador()))
    
    ranking(nome,partidas,partidas_vencedoras,partidas_empatadas)

def placar(partidas,partidas_vencedoras,partidas_empatadas,resultado_jogada):
    partidas +=1
    if resultado_jogada == 'jogador':
        partidas_vencedoras +=1
    elif resultado_jogada == 'empate':
        partidas_empatadas +=1
    return partidas, partidas_vencedoras, partidas_empatadas    

def ranking(nome,partidas,partidas_vencedoras,partidas_empatadas):
    print(f'Resultado da competição de {nome} versus máquina: \n - {nome} venceu: {partidas_vencedoras}\n - Máquina venceu: {partidas-partidas_empatadas-partidas_vencedoras}\n - Empates: {partidas_empatadas}\n - Total: {partidas}')

abertura_jogo()