lista_tarefas = dict()

def incluir_tarefa():
    nome = input('Informe o nome: ')
    descricao = input('Informe a descricao: ')
    prioridade = input('Informe a prioridade: ')
    categoria = input('Informe a categoria: ')

    if nome in ' '*999 or descricao in ' '*999 or prioridade in ' '*999 or categoria in ' '*999:
        print ('Parâmetros inválidos')
        incluir_tarefa()
    else:
        lista_chaves = list(lista_tarefas)
        if len(lista_chaves) != 0:
            ultima_chave = int(lista_chaves[-1])
        else:
            ultima_chave = 0

        if len(lista_chaves) == 0:
            lista_tarefas['1'] = {'nome': nome, 'descricao': descricao, 'prioridade': prioridade, 'categoria':categoria, 'status': 'ativa'}
        else:
            lista_tarefas[f'{ultima_chave + 1}'] = {'nome': nome, 'descricao': descricao, 'prioridade': prioridade, 'categoria':categoria, 'status': 'ativa'}
        print('Tafera incluída com sucesso')

def listar_tarefas():

    if len(lista_tarefas) == 0:
        print('\nNão existem tarefas cadastradas')
    else:
        print('\n','*'*10,'LISTA DE TAREFAS','*'*10)
        for chave, valor in lista_tarefas.items():
            print(f'ID: {chave}')
            print(f'Nome: {valor['nome']}')
            print(f'Descrição: {valor['descricao']}')
            print(f'Prioridade: {valor['prioridade']}')
            print(f'Categoria: {valor['categoria']}')
            print(f'Status: {valor['status']}')
            print('*'*10)

def concluir_tarefa():
    listar_tarefas()
    if len(lista_tarefas) != 0:
        tarefa_para_concluir = input('Informe o ID da tarefa concluída: ')

        if tarefa_para_concluir not in list(lista_tarefas):
            print('\nOpção inválida. Tente novamente')
            concluir_tarefa()
        else:
            lista_tarefas[f'{tarefa_para_concluir}']['status'] = 'concluída'
            print(f'Tarefa {tarefa_para_concluir} concluída')

def listar_prioridades():
    conjunto = set()
    for _, valor in lista_tarefas.items():
        conjunto.add(valor['prioridade'])
    return list(conjunto)

def listar_categorias():
    conjunto = set()
    for _, valor in lista_tarefas.items():
        conjunto.add(valor['categoria'])
    return list(conjunto)

def listar_por_prioridade():
    prioridades = listar_prioridades()
    if len(lista_tarefas) == 0:
        print('\nNão existem tarefas cadastradas')
    else:
        for prioridade in prioridades:
            print(f'\nPRIORIDADE: {prioridade.upper()}')
            for chave,valor in lista_tarefas.items():
                if valor['prioridade'] == prioridade:
                    print(f'ID: {chave}')
                    print(f'Nome: {valor['nome']}')
                    print(f'Descrição: {valor['descricao']}')
                    print(f'Prioridade: {valor['prioridade']}')
                    print(f'Categoria: {valor['categoria']}')
                    print(f'Status: {valor['status']}')
            print('*'*20)

def listar_por_categoria():
    categorias = listar_categorias()
    if len(lista_tarefas) == 0:
        print('\nNão existem tarefas cadastradas')
    else:
        for categoria in categorias:
            print(f'\nCATEGORIA: {categoria.upper()}')
            for chave,valor in lista_tarefas.items():
                if valor['categoria'] == categoria:
                    print(f'ID: {chave}')
                    print(f'Nome: {valor['nome']}')
                    print(f'Descrição: {valor['descricao']}')
                    print(f'Prioridade: {valor['prioridade']}')
                    print(f'Categoria: {valor['categoria']}')
            print('*'*20)

def listar_por_status():
    lista_status = ['ativa','concluída']
    if len(lista_tarefas) == 0:
        print('\nNão existem tarefas cadastradas')
    else:
        for status in lista_status:
            print(f'\nSTATUS: {status.upper()}')
            for chave,valor in lista_tarefas.items():
                if valor['status'] == status:
                    print(f'ID: {chave}')
                    print(f'Nome: {valor['nome']}')
                    print(f'Descrição: {valor['descricao']}')
                    print(f'Prioridade: {valor['prioridade']}')
                    print(f'Categoria: {valor['categoria']}')
            print('*'*20)

while True:
    print('\n','*'*10,'MENU - LISTA DE TAREFAS (TO DO)','*'*10)
    print('1. Inserir tarefa')
    print('2. Marcar tarefa concluída')
    print('3. Listar Tarefas - Ordem ID')
    print('4. Listar Tarefas - Por Categoria')
    print('5. Listar Tarefas - Por Prioridade')
    print('6. Listar Tarefas - Por Status')
    print('7. Sair')
    print()

    opcao = input('Informe a opção desejada: ')

    if opcao == '1':
        incluir_tarefa()
    elif opcao == '2':
        concluir_tarefa()
    elif opcao == '3':
        listar_tarefas()
    elif opcao == '4':
        listar_por_categoria()
    elif opcao == '5':
        listar_por_prioridade()
    elif opcao == '6':
        listar_por_status()
    elif opcao == '7':
        break
    else:
        print('Opção Inválida. Tente Novamente')