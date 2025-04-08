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
        return f'Nome: {self.nome}\nEmail: {self.get_email()}\nTelefone: {self.get_telefone()}'

class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, id):
        super().__init__(nome, telefone, email)
        self.__id = id 

    def get_id(self):
        return self.__id
    
    def exibir_informacoes(self):
        return f'Cliente ID: {self.get_id()} | Nome: {self.nome} | Email: {self.get_email()} | Telefone: {self.get_telefone()}'

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
    def __init__(self, dono_reserva, quarto_reservado, data_checkin, data_checkout,status_reserva=None):
        self.dono_reserva = dono_reserva #instância de Cliente
        self.quarto_reservado = quarto_reservado #instância de Quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status_reserva = status_reserva

class GerenciadorReservas():

    def __init__(self):
        self.lista_clientes = []
        self.lista_quartos = []
        self.lista_reservas = []

    def cadastrar_cliente(self, nome, telefone, email):
        id = len(self.lista_clientes)
        cliente = Cliente(nome, telefone, email, id)
        self.lista_clientes.append(cliente)
        return cliente

    def cadastrar_quarto(self,numero_quarto, tipo_quarto, preco_diaria):
        quarto = Quarto(numero_quarto, tipo_quarto, preco_diaria)
        self.lista_quartos.append(quarto)
        return quarto

    def criar_reserva(self, hospede, quarto, data_checkin, data_checkout):
        reserva = Reserva(hospede,quarto,data_checkin,data_checkout,status_reserva="ativa")
        quarto.set_status_disponibilidade("ocupado")
        self.lista_reservas.append(reserva)
        print(f"Reserva criada com sucesso!\nHóspede: {hospede.nome} | Quarto {quarto.numero_quarto} | Disp. Quarto {quarto.get_status_disponibilidade()} | Status Reserva {reserva.status_reserva} | CheckIn {reserva.data_checkin} | CheckOut {reserva.data_checkout}")
        return reserva

    def verificar_disponibilidade_quarto(self, quarto):
        return quarto.get_status_disponibilidade()
    
    def modificar_reserva(self, reserva, novo_quarto, novo_checkin, novo_checkout):
        for _reserva in self.lista_reservas:
            if _reserva == reserva:
                _reserva.quarto_reservado.set_status_disponibilidade('livre')
                _reserva.quarto_reservado = novo_quarto
                _reserva.data_checkin = novo_checkin
                _reserva.data_checkout = novo_checkout

                print(f"Reserva alterada com sucesso!\nHóspede: {_reserva.dono_reserva.nome} | Quarto {_reserva.quarto_reservado.numero_quarto} | Disp. Quarto {_reserva.quarto_reservado.get_status_disponibilidade()} | Status Reserva {_reserva.status_reserva} | CheckIn {_reserva.data_checkin} | CheckOut {_reserva.data_checkout}")
                
            return _reserva

    def cancelar_reserva(self,reserva):
        for _reserva in self.lista_reservas:
            if _reserva == reserva:
                self.listar_reservas()
                _reserva.quarto_reservado.set_status_disponibilidade('livre')
                _reserva.status_reserva = "cancelada"

                print(f"Reserva cancelada com sucesso!\nHóspede: {_reserva.dono_reserva.nome} | Quarto {_reserva.quarto_reservado.numero_quarto} | Disp. Quarto {_reserva.quarto_reservado.get_status_disponibilidade()} | Status Reserva {_reserva.status_reserva} | CheckIn {_reserva.data_checkin} | CheckOut {_reserva.data_checkout}")

                self.listar_reservas()

                return _reserva

    def listar_reservas(self):
        print ('**** LISTA RESERVAS ATIVAS ****')
        reservas_ativas = False
        for reserva in self.lista_reservas:

            if reserva.status_reserva == "ativa":
                print(f'Quarto {reserva.quarto_reservado.numero_quarto} | Nome hóspede: {reserva.dono_reserva.nome} | Data Check In: {reserva.data_checkin}')
                reservas_ativas = True
        if not reservas_ativas:
            print("Não existem reservas ativas")            
        
    def consultar_cliente(self, cliente):
        
        for _cliente in self.lista_clientes:
            if _cliente == cliente:
                return cliente.exibir_informacoes()

        return 'Cliente não encontrado'
        
# TESTES
gerenciador = GerenciadorReservas()

hospede_1 = gerenciador.cadastrar_cliente("Ana","3198877-1645","ana@gmail.com")
hospede_2 = gerenciador.cadastrar_cliente("Jose","6198555-1254","jose@outlook.com")
hospede_3 = gerenciador.cadastrar_cliente("Viviane","5198526-1475","vivi@hotmail.com")

quarto_1 = gerenciador.cadastrar_quarto(401,"single",269.00)
quarto_2 = gerenciador.cadastrar_quarto(402,"double",469.00)
quarto_3 = gerenciador.cadastrar_quarto(403,"suite",669.00)

reserva_1 = gerenciador.criar_reserva(hospede_1,quarto_1,"2025-02-28","2025-03-04")
reserva_2 = gerenciador.criar_reserva(hospede_2,quarto_2,"2025-03-03","2025-03-13")
reserva_3 = gerenciador.criar_reserva(hospede_3,quarto_3,"2025-03-28","2025-04-04")

print(gerenciador.verificar_disponibilidade_quarto(quarto_1))
print(gerenciador.verificar_disponibilidade_quarto(quarto_2))
print(gerenciador.verificar_disponibilidade_quarto(quarto_3))

gerenciador.listar_reservas()

gerenciador.modificar_reserva(reserva_1,quarto_2,"2025-01-01","2025-01-15")
gerenciador.modificar_reserva(reserva_2,quarto_1,"2025-10-01","2025-10-15")
gerenciador.modificar_reserva(reserva_3,quarto_3,"2025-10-01","2025-10-11")

gerenciador.listar_reservas()

print(gerenciador.verificar_disponibilidade_quarto(quarto_1))
print(gerenciador.verificar_disponibilidade_quarto(quarto_2))
print(gerenciador.verificar_disponibilidade_quarto(quarto_3))

gerenciador.cancelar_reserva(reserva_1)
gerenciador.cancelar_reserva(reserva_2)
gerenciador.cancelar_reserva(reserva_3)

gerenciador.listar_reservas()

print(gerenciador.consultar_cliente(hospede_1))
print(gerenciador.consultar_cliente(hospede_2))
print(gerenciador.consultar_cliente(hospede_3))