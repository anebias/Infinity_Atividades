# Ambientes Virtuais
# Substitua "myenv" pelo nome que você deseja dar ao seu ambiente virtual
# CRIAR AMBIENTE: python -m venv myenv
# ATIVAR: 
# No Windows: myenv/scripts/activate
# No macOS e Linux: source myenv/bin/activate
# INSTALAR BIBLIOTECAS: pip install nome_da_biblioteca
# LISTAR BIBLIOTECAS: pip list
# DESATIVAR AO FINAL: 
# No Windows: myenv/scripts/deactivate
# No macOS e Linux: source myenv/bin/deactivate

# Desenvolver um programa de linha de comando que permite
#  aos usuários gerenciar suas tarefas diárias, atribuindo-lhes
#  prioridades e categorias. O projeto será organizado em várias
#  partes e usará funções, listas, tuplas, dicionários, conjuntos e
#  um ambiente virtual. Passos do projeto:
#  Configuração do Ambiente Virtual:
#  Crie um ambiente virtual usando o módulo venv

#  Definição de Dados:
#  Defina estruturas de dados para representar tarefas. Cada tarefa pode incluir
#  informações como nome, descrição, prioridade e categoria. Você pode usar
#  dicionários para representar as tarefas.

#  Funções:
#  Crie funções para adicionar tarefas, listar tarefas, marcar tarefas
#  como concluídas, exibir tarefas por prioridade ou categoria, e outras
#  funcionalidades que desejar.
#  Menu de Comandos:
#  Crie um menu de comandos de linha de comando que permita ao
#  usuário interagir com o programa.

lista_tarefas = dict()

# TESTES
lista_tarefas = {'1': {'nome': 'tarefa 1', 'descricao': 'descricao tarefa 1', 'prioridade': 'alta', 'categoria':'compras', 'status': 'ativa'}, 
                 '2': {'nome': 'escola', 'descricao': 'descricao tarefa 2', 'prioridade': 'baixa', 'categoria':'categoria tafefa 2', 'status': 'ativa'},
                 '3': {'nome': 'compras', 'descricao': 'descricao tarefa 2', 'prioridade': 'media', 'categoria':'categoria tafefa 3', 'status': 'ativa'}, '4': {'nome': 'tarefa 4', 'descricao': 'descricao tarefa 2', 'prioridade': 'extrema', 'categoria':'escola', 'status': 'ativa'},
                 '5': {'nome': 'tarefa 5', 'descricao': 'descricao tarefa 2', 'prioridade': 'alta', 'categoria':'pagar', 'status': 'ativa'}
                 }

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

