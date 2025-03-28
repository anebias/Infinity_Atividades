'''[PYIA-A13] Crie uma classe chamada ContaBancaria que tenha dois atributos privados, _saldo e _titular. O atributo _saldo deve armazenar o saldo da conta, enquanto o atributo _titular deve armazenar o nome do titular da conta. Para interagir com esses atributos, implemente métodos públicos que permitam realizar operações bancárias. Crie um método depositar que permita adicionar um valor ao saldo, um método sacar que permita retirar um valor do saldo (caso haja saldo suficiente), e um método exibir_saldo que exiba o saldo atual da conta. Utilize métodos para encapsular o acesso ao saldo, garantindo que ele só possa ser alterado de maneira controlada pelos métodos de depósito e saque.'''

class ContaBancaria:

    def __init__(self, titular):
        self.__saldo = 0 # Saldo zero ao instanciar uma conta. Saldo só pode ser alterado pelos métodos depositar e sacar
        self.__titular = titular
    
    # Não foi solicitado no exercício, mas coloquei para usar o atributo em algum lugar do código e parar de sinalizar
    @property
    def titular(self):
        return self.__titular

    def depositar(self, valor):
        if valor < 0:
            print(f'Valor inválido para depósito: {valor:.2f}')
            return
        self.__saldo += valor

    def sacar(self, valor):
        if valor < 0:
            print(f'Valor inválido para saque: {valor:.2f}')
            return
        if valor > self.__saldo:
            print('Saldo insuficiente')
            return
        self.__saldo -= valor

    def exibir_saldo(self):
        print (f'Saldo: R$ {self.__saldo:.2f}')

# # TESTES
# conta_teste = ContaBancaria("Alessandra")
# conta_teste.depositar(500)
# conta_teste.depositar(-200)
# conta_teste.sacar(100)
# conta_teste.sacar(-300)
# conta_teste.sacar(600)
# conta_teste.exibir_saldo()
# print(conta_teste.titular) # Acesso permitido pelo decorator @property
# # print(conta_teste.__saldo) Erro ao tentar acessar, pois está encapsulado
# # print(conta_teste.__titular) Erro ao tentar acessar, pois está encapsulado
