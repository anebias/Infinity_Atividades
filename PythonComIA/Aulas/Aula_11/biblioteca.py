																																																							
class Livro:
    def __init__(self, titulo, autor, ano, categoria, editora, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.editora = editora
        self.ISBN = ISBN
        self.emprestado = False	

    def __str__(self):
        return self.titulo
    
    def get_dict(self):
        return {
            'titulo': self.titulo,
            'autor':  self.autor,
            'ano': self.ano,
            'categoria': self.categoria,
            'editora': self.editora
        }

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
        self.emprestimos = []

    def get_emprestimos(self):
        emprestados = []
        for livros in self.emprestimos:
            emprestados.append(livros.get_dict())
        return emprestados

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
        for usuario in self.usuarios:
            print(usuario)
    
    def cadastrar_livros(self, livro:Livro):
        self.catalogo.append(livro)
        print('Livro cadastrado com sucesso!') 

    def emprestar_livro(self, livro, pessoa):
        if livro.emprestado:
            print('Este livro já está emprestado')
        elif livro not in self.catalogo:
            print('Livro não registrado')
        elif pessoa not in self.usuarios:
            print('Usuário não cadastado')
        else:
            livro.emprestado = True
            pessoa.emprestimos.append(livro)
            print(f'Livro emprestado com sucesso! Para usuario {pessoa.nome}')

    def devolver_livro(self, livro, pessoa):
        if livro.emprestado:
            livro.emprestado = False
            print('Livros emprestados com o usuário:')
            print(pessoa.emprestimos.get_emprestimos())
            pessoa.emprestimos.remove(livro)

            print('Livro devolvido com sucesso')

print('*'*10,'CADASTRE A BIBLIOTECA','*'*10)
# dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
# nome = input('Nome da biblioteca: ')
# endereco = input('Endereço da biblioteca: ')
# horario = dict()

# for dia in dias_semana:
#     horario_abertura = input(f'Informe o horário de abertura para {dia}: ')
#     horario_encerramento = input(f'Informe o horário de encerramento para {dia}: ')
#     horario[dia] = (horario_abertura, horario_encerramento)
# biblioteca = Biblioteca(nome,endereco,horario)
# biblioteca.horario_de_funcionameno(horario)

biblioteca = Biblioteca('Biblioteca Central','Rua A, 147','09:00 às 18:00')

def menu():
    print(f'\nNome: {biblioteca.nome}')

    print('Escolha sua opção:')
    print('1 - Cadastrar usuário')
    print('2 - Ver usuários cadastrados')
    print('3 - Cadastrar livro')
    print('4 - Ver livros cadastrados')
    print('5 - Emprestar livro') ##
    print('6 - Devolver livro')  ##
    print('7 - Sair do sistema')

    opcao = input('Digite sua opcao: ')

    if opcao[0] == '1':
        print('Informe os seguintes dados...')
        nome = input('Nome: ').capitalize()
        sobrenome = input('Sobrenome: ').capitalize()
        matricula = input('Matrícula: ')
        endereco = input('Endereço: ')
        cpf = input('CPF: ')
        data_nascimento = input('Data de Nascimento: ')
        funcao = input('Função: ')
        # VALIDAÇÕES: NOME, SOBRENOME, CPF, DATA NASCIMENTO,...(SIMBOLOS, QDE CARACTERES, ...)
        if nome in ' '*999 or sobrenome in ' '*999 or matricula in ' '*999 or endereco in ' '*999 or cpf in ' '*999 or data_nascimento in ' '*999 or funcao in ' '*999:
            print('Valores inválidos. Informe todos os dados para cadastro.')
        else:
            biblioteca.cadastrar_usuarios(Pessoa(nome,sobrenome,matricula,endereco,cpf,data_nascimento,funcao))
            print(f'Novo usuário {nome} cadastrado com sucesso')
    elif opcao[0] == '2':
        pass
    elif opcao[0] == '3':
        pass
    elif opcao[0] == '4':
        pass
    elif opcao[0] == '5':
        pass
    elif opcao[0] == '6':
        pass
    
    
    if opcao[0] != '7':
        menu()

    print('*'*5,'Sistema encerrado','*'*5)

menu()

# TESTES TESTES TESTES
# joao_farias = Biblioteca('João Farias', 'Rua das Flores', '10')
# gabriel = Pessoa('Gabriel', 'Santos', '14A', 'Rua X', '123', '19/04/1994', 'usuário')
# livro = Livro('X', 'Y', 1994, 'M', 'A', '13143113')
# livro2 = Livro('Volume 2', 'Yx', 1994, 'M', 'A', '13143113')
# livro3 = Livro('Volume 3', 'AbzYx', 1799, 'M', 'A', '13143113')

# # joao_farias.cadastrar_usuarios(gabriel)
# joao_farias.cadastrar_livros(livro)
# joao_farias.cadastrar_livros(livro2)
# joao_farias.emprestar_livro(livro3, gabriel)
# joao_farias.emprestar_livro(livro, gabriel)
# joao_farias.emprestar_livro(livro, gabriel)
# gabriel.emprestimos.append(livro)
# gabriel.emprestimos.append(livro2)
# # print('Livros que o Gabriel pegou!')
# # print(gabriel.get_emprestimos())
# # print('-'*30)

# lista = ['banana', 'uva', 'laranja']
# lista.remove('banana')
