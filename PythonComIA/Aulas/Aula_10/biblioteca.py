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

# Localidade do livro na biblioteca
class Estante:
    def __init__(self, numero, fileira, andar, categoria):
        self.numero = numero
        self.fileira = fileira
        self.andar = andar
        self.categoria = categoria
        self.livros = []
    
    def listar_livros_na_estante(self):
        lista = []
        for livro in self.livros:
            lista.append(livro)
        print(livro)

class Pessoa:
    def __init__(self, nome, sobrenome, matricula, endereco, cpf, data_de_nascimento=''):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.endereco = endereco
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.status = True
    
class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, matricula, endereco, cpf, funcao):
        super().__init__(nome, sobrenome, matricula, endereco, cpf)
        self.funcao = funcao
    
    def __str__(self):
        return self.nome
    
    def cadastrar_livros(self, livro:Livro, estante: Estante, biblioteca):
        estante.livros.append(livro)
        biblioteca.catalogo.append(livro)


class Biblioteca:
    def __init__(self, nome, endereco, horario):
        self.nome = nome
        self.endereco = endereco
        self.horario = horario
        self.catalogo = []
        self.usuarios = []
        self.funcionarios = []

    def __str__(self):
        return (f'Biblioteca: {self.nome}, endereço: {self.endereco}')

    def cadastrar_funcionarios(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
    
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)

    def cadastrar_usuarios(self, usuario: Pessoa):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)   

    def horario_de_funcionameno(self):
        for dia, hora in self.horario.items():
            print(f'{dia} - {hora[0]} às {hora[1]}')

def menu():
    print('Escolha uma opção: ')
    print('1 - Cadastrar nova biblioteca')
    print('2 - Cadastrar estante')
    print('3 - Cadastrar funcionário')
    print('4 - Cadastrar usuário')
    print('5 - Cadastrar livro')
    print('6 - Emprestar livro')
    print('7 - Devolver livro')

    opcao = input(": " )

    if opcao[0] == '1':
        dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
        nome = input('Nome da biblioteca: ')
        endereco = input('Endereço da biblioteca: ')
        horario = dict()

        for dia in dias_semana:
            horario_abertura = input(f'Informe o horário de abertura para {dia}: ')
            horario_encerramento = input(f'Informe o horário de encerramento para {dia}: ')
            horario[dia] = (horario_abertura, horario_encerramento)
        biblioteca = Biblioteca(nome,endereco,horario)
        biblioteca.horario_de_funcionameno()

menu()