class Menu():
    print('*'*20,'M E N U   -  HAMBURGUERIA','*'*20)
    print('\nEscolha uma opção: ')
    
    Lista_opcoes = ['Incluir hamburgueria','Incluir pedido','Entregar pedido', 'Consultar pedido',
                    'Alterar pedido',
                    'Cancelar pedido', 'Listar pedidos em espera', 
                    'Listar pedidos entregues no dia',
                    'Cadastrar hamburguer','Cadastrar bebida', 'Cadastrar cliente',
                    'Cadastrar Usuário','Consultar Cliente',
                    'Consultar usuário','Alterar Cliente','Alterar Usuário',
                    'Consultar Fidelização Cliente','Alterar Produto','Alterar Pedido']
    
    # Abrir opção de consultar cliente e usuário
    # Cliente: por telefone, por nome
    # Usuário: por CPF, por telefone, por nome
    # Alterar cliente e usuário: telefone, endereço
    # Alterar produto: valor, nome, hamburguer: descricao; bebida: volume, tipo recipiente
    # Consultar pedido: numero, cliente, valor total
    # Alterar pedido: tipo de entrega, adicionar item, excluir item

    for i, item in enumerate(Lista_opcoes):
        print(f'{i+1} - {Lista_opcoes[i]}')

    print('*'*65)