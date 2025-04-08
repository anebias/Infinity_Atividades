class Reserva:
    def __init__(self, dono_reserva, quarto_reservado, data_checkin, data_checkout,status_reserva=None):
        self.dono_reserva = dono_reserva #instância de Cliente
        self.quarto_reservado = quarto_reservado #instância de Quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status_reserva = status_reserva
