'''ATIVIDADE PRÁTICA 1
Crie um classe chamada cachorro com os atributos:
nome, raça, idade'''

# class Cachorro:
#     def __init__(self, nome, raca, idade):
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade

# meu_cachorro = Cachorro("Betão","vira-lata",15)
# print(meu_cachorro)

'''ATIVIDADE PRÁTICA 2
Crie um classe chamada pessoa com os atributos: nome,
idade, peso, gênero'''

# class Pessoa:
#     def __init__(self, nome, idade, peso, genero):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.genero = genero

'''ATIVIDADE PRÁTICA 3
Crie uma classe Empresa que permita gerenciar
funcionários. Os funcionários devem ter informações
como nome, cargo e salário. A empresa deve ser capaz
de adicionar, remover e listar funcionários.'''

# class Funcionarios:
#     def __init__(self,nome, cargo, salario):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario = salario

'''ATIVIDADE PRÁTICA 4
Crie uma classe Calculadora que tenha métodos
para realizar operações matemáticas básicas 
(+ , - , *, / ).'''

# class Calculadora:
#     def __init__(self):
#         pass

#     def soma(self,*args):
#         resultado = 0
#         for num in args:
#             resultado += num
#         return resultado

#     def subtracao(self, num1, num2):
#         return num1 - num2

#     def multiplicacao(self, *args):
#         resultado = 0
#         for num in args:
#             resultado *= num
#         return resultado

#     def divisao(self, num1, num2):
#         if num2 == 0:
#             return "erro"
#         return num1 / num2

# calculadora = Calculadora()
# calculadora.soma(1.4,2.3)
# print(calculadora.soma(1.4,2.3,7))
# print(calculadora.subtracao(1.4,2.3))
# print(calculadora.multiplicacao(1.4,2.3,5))
# print(calculadora.divisao(1.4,2.3))
# print(calculadora.divisao(1.4,0))

'''ATIVIDADE PRÁTICA 5
Crie uma classe chamada Fatura , a classe Fatura deve incluir os seguintes atributos o nome do item; o preço unitário do item; quantidade de item a ser faturado; valor total da fatura; Sua classe deve ter um construtor que inicialize todos os atributos menos o valor total da fatura. Forneça um método chamado gerar_fatura que calcula o valor da fatura (isto é, multiplicar a
quantidade pelo preço por item).'''

class Fatura:
    def __init__(self,nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total_fatura = self.gerar_fatura()

    def gerar_fatura(self):
        return self.preco_unitario * self.quantidade

# fatura = Fatura("marco",2.58,10)
# print(fatura.valor_total_fatura)

'''DESAFIO PRÁTICO
Aplicativo de hotelaria
Crie uma classe Hotel que permita gerenciar
funcionários, reservas e quartos de hotel. Os
funcionários devem ter informações como nome,
função e salário. O hotel deve ser capaz de
receber reservas, atribuí-las a quartos e
calcular a conta final.'''