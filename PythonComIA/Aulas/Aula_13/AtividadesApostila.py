# # POLIMORFISMO 
# class Animal:
#     def fazerSom(self):
#         pass

# class Cachorro(Animal):
#     def fazerSom(self):
#         return "Woof"
    
# class Gato(Animal):
#     def fazerSom(self):
#         return "Meow"

# class Pato(Animal):
#     def fazerSom(self):
#         return "Quack"
    
# def fazerAnimalFalar(animal):
#     return animal.fazerSom()

# rex = Cachorro()
# whiskers = Gato()
# donald = Pato()

# animais = [rex,whiskers,donald]

# for animal in animais:
#     print(animal.__class__.__name__,"faz",fazerAnimalFalar(animal))

'''ATIVIDADE PRÁTICA 1
Desenvolva um aplicativo de gerenciamento de tarefas
em python. Crie duas classes, Tarefa e Projeto, com uma
associação unidirecional. Permita que as tarefas sejam
associadas a projetos e que você possa listar as tarefas
de um projeto em particular.'''

# **** ANALISAR ****
# class Projeto:
#     def __init__(self, nome):
#         self.nome = nome
#         self.lista_tarefas = []
    
#     def adicionar_tarefa(self, tarefa):
#         self.lista_tarefas.append(tarefa)

#     def listar_tarefas(self):
#         if not self.lista_tarefas:
#             print('Nenhuma tarefa adicionada')
#             return
#         print(f'Projeto: {self.nome}')
#         for i, tarefa in enumerate(self.lista_tarefas,start=1):
#             print(f'Tarefa nº {i}',f'\n{tarefa}')
#             print("*"*20)

# class Tarefa():
#     def __init__(self, titulo, descricao, status="pendente"):
#         self.titulo = titulo
#         self.descricao = descricao
#         self.status = status

#     def __str__(self):
#         return f'Título: {self.titulo} \nDescrição: {self.descricao}\nStatus: {self.status}'

# meu_projeto = Projeto('meu projeto')
# tarefa1 = Tarefa("incluir tabela","incluir a tabela pessoas no BD","pendente")
# tarefa2 = Tarefa("script GET","escrever a rota GET","pendente")

# meu_projeto.adicionar_tarefa(tarefa1)
# meu_projeto.adicionar_tarefa(tarefa2)

# meu_projeto.listar_tarefas()
# print(tarefa1)


# GETERS E SETERS

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.__nome = nome # Atributo privado
#         self.__idade = idade # Atributo privado
    
#     def get_nome(self):
#         return self.__nome
    
#     def set_nome(self, novo_nome):
#         if novo_nome:
#             self.__nome = novo_nome

#     def get_idade(self):
#         return self.__idade
    
#     def set_idade(self, nova_idade):
#         if nova_idade > 0:
#             self.__idade = nova_idade

# pessoa = Pessoa("Alice",15)
# nome = pessoa.get_nome()
# print(nome)
# novo_nome = "Maria Alice"
# pessoa.set_nome(novo_nome)
# print(pessoa.get_nome())

# DECORATOR @PROPERTY
# O decorador @property em Python é usado para criar um método que permite acessar
# um atributo de uma classe como se fosse um atributo público, tornando-o de leitura
# apenas (não permite modificação direta). Isso é útil para implementar um getter,
# permitindo que você defina uma interface de acesso controlada aos atributos
# privados de uma classe.
# É importante observar que, com o decorador @property, o atributo _nome pode ser
# lido, mas não pode ser modificado diretamente. Para permitir a modificação
# controlada, você pode definir um método com o decorador @nome.setter.

# class Pessoa:
#     def __init__(self, nome):
#         self.__nome = nome # Atributo privado
    
#     @property
#     def nome(self):
#         return self.__nome # Getter que acessa o atributo
    
#     @nome.setter
#     def nome(self, novo_nome):
#         if novo_nome:
#             self.__nome = novo_nome

# pessoa = Pessoa("Alice")
# print(pessoa.nome)
# pessoa.nome = "Maria Alice"
# print(pessoa.nome)

'''ATIVIDADE PRÁTICA 2
Desenvolva uma aplicação de loja online em. Crie as
classes Cliente e Pedido com uma associação
bidirecional. Os clientes podem fazer pedidos, e os
pedidos devem estar associados aos clientes que os
fizeram. Implemente a capacidade de listar todos os
pedidos de um cliente específico.'''

# class Cliente:
#     def __init__(self, nome, documento, telefone, endereco):
#         self.nome = nome
#         self.documento = documento
#         self.telefone = telefone
#         self.endereco = endereco
#         self.pedidos = []

#     def adicionar_pedidos(self, pedido):
#         self.pedidos.append(pedido)

#     # Sugestão GPT na avaliação de melhoria do código enviado
#     def fazer_pedido(self, data_pedido, numero_pedido, valor_pedido):
#         pedido = Pedido(data_pedido, numero_pedido, valor_pedido)
#         pedido.cliente = self

#     def listar_pedidos(self):
#         if not self.pedidos:
#             print (f"{self.nome} ainda não tem pedidos")
#             return
        
#         for pedido in self.pedidos:
#             print(f'{pedido.cliente.nome} | {pedido.numero_pedido}: {pedido.data_pedido} | R${pedido.valor_pedido:.2f}')

# class Pedido:
#     def __init__(self, data_pedido, numero_pedido, valor_pedido):
#         self.data_pedido = data_pedido
#         self.numero_pedido = numero_pedido
#         self.valor_pedido = valor_pedido
#         self.__cliente = None
    
#     @property
#     def cliente(self):
#         return self.__cliente
    
#     @cliente.setter
#     def cliente(self,cliente_pedido):
#         self.__cliente = cliente_pedido
#         cliente_pedido.adicionar_pedidos(self)

#     def __str__(self):
#         return f'Pedido: {self.numero_pedido}, Cliente: {self.cliente.nome}'
    
#     # Sugestão GPT na avaliação de melhoria do código enviado
#     def __repr__(self):
#         return f"Pedido({self.numero_pedido}, {self.data_pedido}, R$ {self.valor_pedido:.2f})"

# TESTE COMO ESTAVA SEM SUGESTÃO DE MELHORIA DO GPT
# cliente = Cliente("Vanessa","12345","31-99988-8877","Rua A, nº 123, bairro ZZ, Cidade/UF")
# pedido1 = Pedido("27/03/2025", 987654,14007.85)
# pedido2 = Pedido("10/04/2025", 995147,400.97)
# pedido3 = Pedido("01/07/2024", 654321,1006.00)
# pedido1.cliente = cliente
# pedido2.cliente = cliente
# pedido3.cliente = cliente

# cliente2 = Cliente("André","12987","31-98855-4433","Rua B, nº 78 apto 101, bairro XX, Cidade/UF")
# pedido1 = Pedido("01/09/2024", 654124,98.57)
# pedido2 = Pedido("08/03/2024", 547851,59.99)
# pedido3 = Pedido("16/08/2023", 325784,9874.50)
# pedido1.cliente = cliente2
# pedido2.cliente = cliente2
# pedido3.cliente = cliente2

# cliente.listar_pedidos()
# cliente2.listar_pedidos()

# TESTE COM IMPLEMENTAÇÃO DE MELHORIA DO GPT, COM ATRIBUIÇÃO DE 
# VINCULAÇÃO DO CLIENTE AO PEDIDO À CLASSE "cliente.fazer_pedido"
# print('*'*10,'TESTE MELHORADO','*'*10)
# cliente = Cliente("Vanessa","12345","31-99988-8877","Rua A, nº 123, bairro ZZ, Cidade/UF")
# cliente.fazer_pedido("27/03/2025", 987654,14007.85)
# cliente.fazer_pedido("10/04/2025", 995147,400.97)
# cliente.fazer_pedido("01/07/2024", 654321,1006.00)

# cliente2 = Cliente("André","12987","31-98855-4433","Rua B, nº 78 apto 101, bairro XX, Cidade/UF")
# cliente2.fazer_pedido("01/09/2024", 654124,98.57)
# cliente2.fazer_pedido("08/03/2024", 547851,59.99)
# cliente2.fazer_pedido("16/08/2023", 325784,9874.50)

# cliente.listar_pedidos()
# cliente2.listar_pedidos()

'''ATIVIDADE PRÁTICA 3
Crie uma classe Aluno em Python com atributos privados,
como nome, idade e matrícula. Implemente métodos
públicos para acessar e modificar esses atributos. Em
seguida, crie uma instância da classe e demonstre como
usar os métodos de acesso.'''

# class Aluno:
#     def __init__(self, nome, idade, matricula):
#         self.__nome = nome
#         self.__idade = idade
#         self.__matricula = matricula

#     @property
#     def nome(self):
#         return self.__nome

#     def get_nome(self):
#         return self.__nome
    
#     def set_nome(self,nome):
#         self.__nome = nome

#     def get_idade(self):
#         return self.__idade
    
#     def set_idade(self,idade):
#         self.__idade = idade

#     def get_matricula(self):
#         return self.__matricula
    
#     def set_matricula(self,matricula):
#         self.__matricula = matricula    

#     def __str__(self):
#         # Uso de decorator @property para acessar nome ao invés de __nome
#         # Como matrícula não tem decorator, não consegue acessar sem __
#         return f'Aluno: {self.nome} | Matrícula: {self.__matricula}'

# aluno = Aluno('Alice',15,14785)
# print(aluno.get_nome())
# print(aluno) # Aqui está sendo usado o métdo __str__ para exibição
# aluno.set_nome('Maria Alice')
# print(aluno.get_nome())
# print(aluno) # Aqui está sendo usado o métdo __str__ para exibição
# # Mesma lógica para idade e matrícula

'''ATIVIDADE PRÁTICA 4
Desenvolva uma classe Produto em python que contenha
atributos privados, como nome, preço e quantidade em
estoque. Forneça métodos públicos para acessar e
modificar esses atributos e garantir que o preço e a
quantidade não sejam definidos como valores negativos.'''

# class Produto:
#     def __init__(self, nome, preco: float, quantidade_estoque: int):
#         if preco < 0 or quantidade_estoque < 0:
#             return "Valores inválidos! 'Preço' e/ou 'Quantidade Estoque' não podem ser negativos"
#         self.__nome = nome
#         self.__preco = preco
#         self.__quantidade_estoque = quantidade_estoque

#     def get_nome(self):
#         return self.__nome
    
#     def set_nome(self,nome):
#         self.__nome = nome

#     def get_preco(self):
#         return self.__preco
    
#     def set_preco(self,preco):
#         if preco < 0:
#             print('O valor do produto não pode ser negativo !')
#             return
        
#         self.__preco = preco

#     def get_quantidade_estoque(self):
#         return self.__quantidade_estoque
    
#     def set_quantidade_estoque(self,quantidade_estoque):
#         if quantidade_estoque < 0:
#             print('A quantidade em estoque não pode ser negativa')
#             return
        
#         self.__quantidade_estoque = quantidade_estoque

# produto = Produto('caneta',5.60,2)
# print(produto.get_nome())
# print(produto.get_preco())
# print(produto.get_quantidade_estoque())
# produto.set_nome('caneta esferográfica')
# produto.set_preco(6.15)
# produto.set_quantidade_estoque(1)
# print(produto.get_nome())
# print(produto.get_preco())
# print(produto.get_quantidade_estoque())
# produto.set_nome('caneta esferográfica')
# produto.set_preco(-6.15)
# produto.set_quantidade_estoque(-1)
# print(produto.get_nome())
# print(produto.get_preco())
# print(produto.get_quantidade_estoque())

'''ATIVIDADE PRÁTICA 5
Desenvolva uma classe ContaBancaria em Python com atributos
privados, como saldo e número da conta. Forneça métodos
públicos para depositar dinheiro, sacar dinheiro e verificar o
saldo. Garanta que o saldo não seja definido como negativo e
que as transações sejam registradas.'''

# from random import randint

# class ContaBancaria:
#     def __init__(self):
#         self.__numero_conta = randint(1,100000)
#         self.__saldo = 0
#         self.__transacoes =[]

#     def consultar_numero_conta(self):
#         return f"Número da conta: {self.__numero_conta}"

#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
#             self.__transacoes.append(('+', valor))
#         print( f'Conta: {self.__numero_conta} | Valor Depósito: R$ {valor:.2f}')
    
#     def sacar(self,valor):
#         if valor > self.__saldo:
#             print(f'Saldo insuficiente | Saldo disponível: R$ {self.__saldo:.2f}')
#             return
        
#         if valor > 0 :
#             self.__saldo -= valor
#             self.__transacoes.append(('-', valor))
#             print( f'Conta: {self.__numero_conta} | Valor Saque: R$ {valor:.2f} | Valor Saldo Disponível: R$ {self.__saldo:.2f}')

#     def consultar_saldo(self):
#         return f'Saldo: R$ {self.__saldo:.2f}'
    
#     def imprimir_extrato(self):
#         if not self.__transacoes:
#             print(f'Conta {self.__numero_conta} | Sem movimentação')
#             return
#         print(f'Extrato da conta {self.__numero_conta}:')
#         for transacao in self.__transacoes:
#             print(f'{transacao[0]} {transacao[1]:.2f}')
#         print(f'Fim das movimentações | Saldo Disponível {self.__saldo}')
    
# conta = ContaBancaria()
# conta.depositar(500)
# conta.depositar(5.65)
# conta.sacar(236.54)
# conta.depositar(102.64)
# conta.sacar(23.87)
# conta.sacar(198.70)
# print(conta.consultar_saldo())
# conta.imprimir_extrato()

'''DESAFIO PRÁTICO
sistema de biblioteca
Imagine um sistema de biblioteca em Python que
gerencia livros e usuários. As classes envolvidas são Livro,
Usuario, Biblioteca e Emprestimo.
A classe Livro deve ter atributos privados, como título e
autor, e métodos públicos para obter esses atributos.
A classe Usuario deve ter atributos privados, como nome
e ID, e métodos públicos para obter e modificar esses
atributos.'''


'''DESAFIO PRÁTICO
A classe Biblioteca deve conter uma lista de livros disponíveis
e métodos para adicionar e remover livros.
A classe Empréstimo deve representar um empréstimo de um livro por um
usuário e deve estar associada a um Livro e a um Usuário.
O exercício é criar essas classes, estabelecer a associação
entre elas (um usuário pode pegar emprestado um livro da
biblioteca), aplicar encapsulamento para proteger os
atributos privados e implementar métodos para:'''


'''DESAFIO PRÁTICO
Adicionar e remover livros da biblioteca.
Registrar um empréstimo de livro por um usuário,
verificando se o livro está disponível.
Exibir informações sobre os empréstimo, como qual livro
foi emprestado para qual usuário.'''