# PROJETO POO E FLET

'''Tela inicial:
Exiba uma lista de quartos e suas respectivas
disponibilidades.
Inclua botões para realizar reservas, consultar
informações de clientes e gerenciar reservas.'''



'''Formulário de reserva:
Permita que o usuário escolha o cliente, o quarto e
as datas desejadas para criar uma nova reserva.'''

'''Gerenciamento de clientes:
Inclua uma tela para visualizar, adicionar e editar
informações dos clientes.'''

'''Tela de visualização de reservas:
Apresente uma lista de reservas existentes com a
opção de cancelar reservas específicas.'''

'''DESAFIO EXTRA
Uso de Conceitos Avançados de POO
Implemente herança, polimorfismo e encapsulamento para organizar e otimizar o código do projeto.

Siga as orientações abaixo:
    Herança:
    Crie uma classe base genérica chamada Pessoa, que contenha atributos comuns como nome, telefone e email.
    Faça a classe Cliente herdar de Pessoa, reutilizando esses atributos básicos e adicionando propriedades
    específicas, como um ID único para cada cliente.

    Polimorfismo:
    Implemente métodos que utilizem polimorfismo, como o método exibir_informacoes(). Esse método deve ser definido na classe base Pessoa e sobrescrito na classe Cliente para incluir informações adicionais específicas,
    como o ID do cliente.

    Encapsulamento:
    Garanta que atributos sensíveis, como dados de contato dos clientes e o status de disponibilidade dos quartos, estejam protegidos com modificadores de acesso privados (__atributo).
    Crie métodos públicos (getters e setters) para acessar ou modificar esses atributos de maneira controlada, validando dados quando necessário.'''

class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
    @property
    def nome(self):
        return self.__nome
    
    def set_nome(self,novo_nome):
        self.__nome = novo_nome
        
    def get_telefone(self):
        return self.__telefone
    
    def set_telefone(self,novo_telefone):
        self.__telefone = novo_telefone

    def get_email(self):
        return self.__email
    
    def set_email(self,novo_email):
        self.__email = novo_email

    def exibir_informacoes(self):
        return f'Nome: {self.nome}\nEmail: {self.__email}\nTelefone: {self.__telefone}'

class Cliente(Pessoa):
    def __init__(self, nome, telefone, email):
        super().__init__(nome, telefone, email)
        self.__id = None # biblioteca que gera identificador?

    def exibir_informacoes(self):
        return f'Cliente ID: {self.__id}\nNome: {self.nome}\nEmail: {self.__email}\nTelefone: {self.__telefone}'

class Quarto:
    def __init__(self,numero_quarto, tipo_quarto, preco_diaria):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = tipo_quarto
        self.preco_diaria = preco_diaria
        self.__status_disponibilidade = "livre"

    def set_status_disponibilidade(self,status):
        self.__status_disponibilidade = status

    def get_status_disponibilidade(self):
        return self.__status_disponibilidade

class Reserva:
    def __init__(self, dono_reserva, quarto_reservado, data_checkin, data_checkout):
        self.dono_reserva = dono_reserva #cliente
        self.quarto_reservado = quarto_reservado #quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status_reserva = None

class GerenciadorReservas():

    def verificar_disponibilidade_quarto(self, quarto):
        return quarto.get_status_disponibilidade()

    def criar_reserva(self, hospede, quarto, data_checkin, data_checkout):
        reserva = Reserva(hospede,quarto,data_checkin,data_checkout)
        quarto.set_status_disponibilidade("ocupado")
        print(f"Reserva criada com sucesso!\nHóspede: {hospede.nome} | Quarto {quarto.numero_quarto} | Status {quarto.get_status_disponibilidade()}")

    def modificar_reserva(self):
        pass

    def cancelar_reserva(self):
        pass

    def listar_reservas(self):
        pass

    def consultar_cliente(self, cliente):
        pass

# TESTES
hospede_1 = Cliente("Ana","3198877-1645","ana@gmail.com")
hospede_2 = Cliente("Jose","6198555-1254","jose@outlook.com")
hospede_3 = Cliente("Viviane","5198526-1475","vivi@hotmail.com")

quarto_1 = Quarto(401,"single",269.00)
quarto_2 = Quarto(402,"double",469.00)
quarto_3 = Quarto(403,"suite",669.00)

reserva_1 = Reserva(hospede_1,quarto_1,"2025-02-28","2025-03-04")
reserva_2 = Reserva(hospede_2,quarto_2,"2025-03-03","2025-03-13")
reserva_3 = Reserva(hospede_3,quarto_3,"2025-03-28","2025-04-04")

print("Hóspede 1:",hospede_1.nome)
print("Hóspede 2:",hospede_2.nome)
print("Hóspede 3:",hospede_3.nome)
gerenciador = GerenciadorReservas()
print("Status disponibilidade quarto 1:",gerenciador.verificar_disponibilidade_quarto(quarto_1))
print("Status disponibilidade quarto 2:",gerenciador.verificar_disponibilidade_quarto(quarto_2))
print("Status disponibilidade quarto 3:",gerenciador.verificar_disponibilidade_quarto(quarto_3))
gerenciador.criar_reserva(hospede_1,quarto_1,"2025-02-28","2025-03-04")
gerenciador.criar_reserva(hospede_2,quarto_2,"2025-03-03","2025-03-13")
gerenciador.criar_reserva(hospede_3,quarto_3,"2025-03-28","2025-04-04")
gerenciador.verificar_disponibilidade_quarto(quarto_1)
gerenciador.verificar_disponibilidade_quarto(quarto_2)
gerenciador.verificar_disponibilidade_quarto(quarto_3)
print("Status disponibilidade quarto 1:",gerenciador.verificar_disponibilidade_quarto(quarto_1))
print("Status disponibilidade quarto 2:",gerenciador.verificar_disponibilidade_quarto(quarto_2))
print("Status disponibilidade quarto 3:",gerenciador.verificar_disponibilidade_quarto(quarto_3))
gerenciador.cancelar_reserva(hospede_1)


# gerenciador.criar_reserva(hospede_1,quarto_1)
# gerenciador.criar_reserva(hospede_2,quarto_2)
# gerenciador.criar_reserva(hospede_3,quarto_3)