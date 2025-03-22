'''[PYIA-A11] Crie uma classe base chamada Animal que tenha um método chamado falar, o qual imprime uma mensagem genérica, como "Este animal faz um som." Em seguida, crie duas subclasses chamadas Cachorro e Gato que herdem de Animal. Dentro de cada uma dessas subclasses, sobrescreva o método falar para que ele imprima uma mensagem específica para cada animal. Por exemplo, na classe Cachorro, o método falar pode imprimir "O cachorro late." e, na classe Gato, pode imprimir "O gato mia."'''

class Animal:
    def falar(self):
        print('Este animal faz um som.')

class Cachorro(Animal):
   
    def falar(self):
        print('O cachorro late.')

class Gato(Animal):
    
    def falar(self):
        print('O gato mia.')

# TESTES 
# animal_qualquer = Animal()
# meu_cachorro = Cachorro()
# meu_gato = Gato()

# animal_qualquer.falar()
# meu_cachorro.falar()
# meu_gato.falar()