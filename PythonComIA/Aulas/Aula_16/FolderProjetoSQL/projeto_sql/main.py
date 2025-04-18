
from db import criar_tabelas
from services.escolas import criar_escola, listar_escolas
from services.alunos import criar_aluno, listar_alunos, listar_aluno_por_id, listar_alunos_por_nome, alterar_aluno_por_id

def menu():
    print("\n==== MENU ====")
    print("1 - Cadastrar Escola")
    print("2 - Cadastrar Aluno")
    print("3 - Listar Escolas")
    print("4 - Listar Alunos")
    print("5 - Listar Aluno por id")
    print("6 - Procurar Aluno por nome")
    print("7 - Alterar Aluno por id")
    print("0 - Sair")

def cadastrar_escola():
    print("\n-- Cadastro de Escola --")
    nome = input("Nome: ")
    tipo = input("Tipo (Pública ou Privada): ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")

    criar_escola(nome, tipo, telefone, email, endereco, cidade, estado, cep)
    print("✅ Escola cadastrada com sucesso!")

def cadastrar_aluno():
    print("\n-- Cadastro de Aluno --")
    nome = input("Nome: ")
    data_nasc = input("Data de nascimento (YYYY-MM-DD): ")
    id_escola = input("ID da escola (ou deixe em branco se não tiver): ")
    id_escola = int(id_escola) if id_escola.strip() else None
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")

    criar_aluno(nome, data_nasc, id_escola, telefone, email, endereco, cidade, estado, cep)
    print("✅ Aluno cadastrado com sucesso!")

def listar_todas_escolas():
    print("\n-- Lista de Escolas --")
    escolas = listar_escolas()
    for escola in escolas:
        print(escola)

def listar_todos_alunos():
    print("\n-- Lista de Alunos --")
    alunos = listar_alunos()
    for aluno in alunos:
        print(aluno)

def listar_aluno_id():
    id = input("Informe o id: ")
    id = int(id) if id.strip() else None
    if id:
        print("\n-- Aluno --")
        aluno = listar_aluno_por_id(id)
        print(aluno)

# Incluir tratamento do tipo de dado a ser alterado
# def alterar_aluno():
#     print('Informe os dados abaixo:')
#     id = input('"id" do aluno: ')
#     id = int(id) if id.strip() else None
#     nome = input("Nome: ")
#     data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
#     id_escola = input("ID da escola (ou deixe em branco se não tiver): ")
#     id_escola = int(id_escola) if id_escola.strip() else None
#     telefone = input("Telefone: ")
#     email = input("Email: ")
#     endereco = input("Endereço: ")
#     cidade = input("Cidade: ")
#     estado = input("Estado: ")
#     cep = input("CEP: ")

#     alterar_aluno_por_id(id, nome, data_nascimento, id_escola=None, telefone=None, email=None, endereco=None, cidade=None, estado=None, cep=None)

#     print("✅ Aluno alterado com sucesso!")

def main():
    criar_tabelas()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_escola()
        elif opcao == "2":
            cadastrar_aluno()
        elif opcao == "3":
            listar_todas_escolas()
        elif opcao == "4":
            listar_todos_alunos()
        elif opcao == "5":
            listar_aluno_id()
        elif opcao == "6":
            pass #listar_aluno()
        # elif opcao == "7":
        #     alterar_aluno()
        elif opcao == "0":
            print("👋 Encerrando o programa.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()