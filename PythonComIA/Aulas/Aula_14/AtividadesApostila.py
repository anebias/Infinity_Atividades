# PROJETO POO E FLET

class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
    
    def __str__(self):
        return f'Nome: {self.__nome}\nEmail: {self.__email}\nTelefone: {self.__telefone}'

class Cliente(Pessoa):
    def __init__(self):
        self.__id = None # biblioteca que gera identificador?

    def __str__(self):
        return f'Cliente ID: {self.__id}\nNome: {self.__nome}\nEmail: {self.__email}\nTelefone: {self.__telefone}'

class Quarto:
    def __init__(self,numero_quarto, tipo_quarto, preco_diaria, status_disponibilidade):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = tipo_quarto
        self.preco_diaria = preco_diaria
        self.status_disponibilidade = status_disponibilidade

class Reserva:
    def __init__(self, dono_reserva, quarto_reservado, data_checkin, data_checkout, status_reserva):
        self.dono_reserva = dono_reserva
        self.quarto_reservado = quarto_reservado
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status_reserva = status_reserva

class GerenciadorReservas:
    pass

    def verificar_disponibilidade_quarto(self, quarto):
        pass

    def criar_reserva(self):
        pass

    def modificar_reserva(self):
        pass

    def cancelar_reserva(self):
        pass

    def listar_reservas(self):
        pass

    def consultar_cliente(self):
        pass

        