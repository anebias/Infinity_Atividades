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
