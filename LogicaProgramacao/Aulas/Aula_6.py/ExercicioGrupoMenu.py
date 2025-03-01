senha = '1234'
menu_ativo = False

contador = 0

lista_tarefas = []
lista_tarefas_concluidas = []

while contador < 3: 
    senha_lida = input('Digite sua senha: ')

    if senha_lida == senha:
        print('Bem vindo!')
        menu_ativo = True
        break
    elif contador != 2:
        print('Senha inválida.')
    else:
        print('Acesso bloqueado!')    
    contador += 1

continuar = False

while menu_ativo and continuar == False:
    print('Menu')
    print('1 - Cadastrar Tarefas')
    print('2 - Ver Tarefas')
    print('3 - Marcar como Concluída')
    print('4 - Sair')

    opcao = input('Escolha uma opcao: ')
    continuar = True

    while continuar:
        if opcao == '1':
            lista_tarefas.append(input('Digite a tarefa: '))
            print('Tarefa Cadastrada')
            continuar_opcao = input('Deseja continuar (S/N): ')
            if continuar_opcao == 'S' or continuar_opcao == 's':
                continuar = True
            else:       
                continuar = False

        elif opcao == '2':
            print('Exibindo lista de tarefas: ')
            for tarefa in lista_tarefas:
                print(tarefa)
                continuar = False

        elif opcao == '3':

            for i, tarefa in enumerate(lista_tarefas):
                print(f'Item {i + 1}: {tarefa}')

            tarefa_concluir = int(input('Qual tarefa deseja concluir: '))

            lista_tarefas_concluidas.append(lista_tarefas[tarefa_concluir - 1])

            lista_tarefas.remove(lista_tarefas[tarefa_concluir - 1])

            print('Tarefa Concluída')
            for tarefa in lista_tarefas_concluidas:
                print(tarefa)
                
            continuar_opcao = input('Deseja continuar (S/N): ')

            if continuar_opcao == 'S' or continuar_opcao == 's':
                continuar = True
            else:       
                continuar = False

        elif opcao == '4':
            print('Saindo do sistema')
            menu_ativo = False
            continuar = False
        else: 
            print('Opção inválida!')
            continuar = False
   
