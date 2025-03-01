class Livro:
    def __init__(self, titulo, autor, ano, categoria, editora, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.editora = editora
        self.isbn = isbn
        self.emprestado = False

    def __str__(self):
        return self.titulo, self.emprestado
     
class Pessoa:
    def __init__(self, nome, sobrenome, matricula, endereco, cpf, data_de_nascimento, funcao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.endereco = endereco
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.status = True
        self.funcao = funcao

    def __str__(self):
        return f'Nome: {self.nome} {self.sobrenome}, Matrícula: {self.matricula}'

class Biblioteca:
    def __init__(self, nome, endereco, horario):
        self.nome = nome
        self.endereco = endereco
        self.horario = horario
        self.catalogo = []
        self.usuarios = []
        self.funcionarios = []

    def cadastrar_usuarios(self, usuario: Pessoa):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for i, usuario in enumerate(self.usuarios):
            print(f'{i+1} - {usuario}')
    
    def cadastrar_livros(self, livro:Livro):
        self.catalogo.append(livro)
        print(f'Livro cadastrado com sucesso! {livro.titulo}')

    def listar_livros(self):
        for i, livro in enumerate(self.catalogo):
            print(f'{i+1} - {livro[0]}')

    def emprestar_livro(self, livro):
        if not livro.emprestado and livro in self.catalogo:
            livro.emprestado = True
            print('Livro emprestado com sucesso!')
        else:
            print('Livro indisponível ou emprestado')

    def devolver_livro(self, livro):
        if livro.emprestado:
            livro.emprestado = False
            print('Livro devolvido com sucesso')

horario = {
    'Segunda': ('10:00', '17:00'),
    'Terça': ('10:00', '17:00'),
    'Quarta': ('10:00', '17:00'),
    'Quinta': ('10:00', '17:00'),
    'Sexta': ('10:00', '17:00'),
    'Sábado': ('10:00', '17:00'),
}

biblioteca = Biblioteca("Biblioteca Central", "Praça Liberdade", horario)

def menu():
    while True:
        print('Escolha sua opção:')
        print('1 - Cadastrar usuário')
        print('2 - Cadastrar livro')
        print('3 - Emprestar livro')
        print('4 - Devolver livro')
        print('5 - Sair do sistema')

        opcao = input('\nDigite sua opcao: ')

        if opcao[0] == '1':
            nome = input('Informe o nome: ')
            sobrenome = input('Informe o sobrenome: ')
            matricula = input('Informe a matrícula: ')
            endereco = input('Informe o endereço: ')
            cpf = input('Informe o CPF: ')
            data_de_nascimento = input('Informe a data de nascimento: ')
            funcao = input('Informe a função: ')
            usuario = Pessoa(nome, sobrenome, matricula, endereco, cpf, data_de_nascimento, funcao)
            biblioteca.cadastrar_usuarios(usuario)
            biblioteca.listar_usuarios()

        elif opcao[0] == '2':
            titulo = input('Informe o título: ')
            autor = input('Informe o autor: ')
            ano = input('Informe o ano: ')
            categoria = input('Informe a categoria: ')
            editora = input('Informe a editora: ')
            isbn = input('Informe o ISBN: ')
            livro = Livro(titulo, autor, ano, categoria, editora, isbn)
            biblioteca.cadastrar_livros(livro)
            print('\nLivros Cadastrados:')
            biblioteca.listar_livros()
            print()

        elif opcao[0] == '3':
            biblioteca.listar_livros()
            # indice_livro = ""
            # while not livro.isdigit():
            #     indice_livro = input('Informe o livro: ')

            indice_livro = input('Informe o livro: ')

            if (int(indice_livro) > len(biblioteca.catalogo)) or not indice_livro.isdigit():
                print('Inválido. Livro não disponivel no catalogo')
                continue
            else:
                biblioteca.emprestar_livro(biblioteca.catalogo[int(indice_livro) - 1])

            #     print('Este livro não está disponivel para empréstimo')
            # else:
            #     biblioteca.catalogo[livro - 1] = True
            
            biblioteca.listar_livros()

        elif opcao[0] == '4':
            pass
        elif opcao[0] == '5':
            print('Logoff realizado com sucesso !')
            break
        else:
            print('Opção inválida! tente novamente')
            menu()
menu()