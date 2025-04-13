from class_pessoas import Cliente
from class_quartos import Quarto
from class_reservas import Reserva

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

    def listar_reservas_ativas(self):
        print ('**** LISTA RESERVAS ATIVAS ****')
        reservas_ativas = False
        for reserva in self.lista_reservas:

            if reserva.status_reserva == "ativa":
                print(f'Quarto {reserva.quarto_reservado.numero_quarto} | Nome hóspede: {reserva.dono_reserva.nome} | Data Check In: {reserva.data_checkin}')
                reservas_ativas = True
        if not reservas_ativas:
            print("Não existem reservas ativas")            
        
    def listar_reservas(self):

        lista_reservas_cadastradas = []

        for reserva in self.lista_reservas:

            if reserva.status_reserva == "ativa":
                lista_reservas_cadastradas.append(f'Quarto {reserva.quarto_reservado.numero_quarto} | Nome hóspede: {reserva.dono_reserva.nome} | Data Check In: {reserva.data_checkin}')
        
        return lista_reservas_cadastradas

    def consultar_cliente(self, cliente):
        
        for _cliente in self.lista_clientes:
            if _cliente == cliente:
                return cliente.exibir_informacoes()

        return 'Cliente não encontrado'
    
    def listar_quartos_disponibilidades(self):
        
        lista_quartos_disponibilidades = []

        if self.lista_quartos:
            for quarto in self.lista_quartos:
                disponibilidade = self.verificar_disponibilidade_quarto(quarto)
                lista_quartos_disponibilidades.append(f'{quarto.numero_quarto} | {disponibilidade}')
        return lista_quartos_disponibilidades


    def listar_clientes(self):
        lista_clientes_cadastrados = []

        if self.lista_clientes:
            for cliente in self.lista_clientes:
                lista_clientes_cadastrados.append(cliente.nome)
        return lista_clientes_cadastrados

