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