'''ATIVIDADE PRÁTICA 1
Crie uma hierarquia de classes representando formas
geométricas. Comece com uma classe base chamada
"Forma e, em seguida, crie classes derivadas como
"Círculo e Retângulo que herdem da classe base.
Adicione métodos para calcular área e perímetro em
cada classe derivada.'''



'''ATIVIDADE PRÁTICA 2
Crie uma hierarquia de classes que represente veículos.
Comece com uma classe base "Veículo e, em seguida,
crie classes derivadas como Carro e Bicicleta." Adicione
métodos para definir atributos, como cor e modelo,
e permita a chamada de métodos em cadeia para
configurar esses atributos.'''


'''ATIVIDADE PRÁTICA 3
Crie uma classe chamada "Calculadora" com um método
somar que pode somar dois números inteiros ou duas
strings. Use o polimorfismo para implementar a
sobrecarga do método somar para que ele funcione
com diferentes tipos de entrada (números inteiros e
strings). Crie exemplos de uso para demonstrar como a
mesma função pode se comportar de maneira diferente
com base nos tipos de entrada.'''


'''ATIVIDADE PRÁTICA 4
Crie uma interface chamada "Veículo" com métodos
"acelerar" e "frear." Em seguida, crie classes concretas
como "Carro" e "Bicicleta" que implementem a interface
"Veículo" e forneçam suas próprias implementações dos
métodos "acelerar" e "frear." Demonstre como o
polimorfismo pode ser usado para tratar diferentes tipos
de veículos de maneira uniforme, chamando os métodos
da interface.'''


'''ATIVIDADE PRÁTICA 5
Crie uma classe base chamada "Animal" com um método
"emitirSom." Em seguida, crie classes derivadas como
"Cachorro," "Gato" e "Pássaro" que herdem de "Animal"
e sobrescrevam o método "emitirSom" para cada tipo de animal.
Crie uma lista de animais e percorra-a, chamando o método
"emitirSom" para cada animal. Demonstre como o polimorfismo
permite que diferentes tipos de animais emitam seus sons de
maneira uniforme.'''


'''DESAFIO PRÁTICO
sistema de gerenciamento de contas bancárias
em Python Crie um sistema de gerenciamento de contas bancárias
em Python usando herança e polimorfismo. O sistema
deve incluir as seguintes classes:'''


'''DESAFIO PRÁTICO
Classe Conta:
-A classe base "Conta" deve ter atributos para o número da conta, 
o titular da conta e o saldo.
-Ela deve incluir métodos para depósitos, saques e exibição do saldo
atual.'''


'''DESAFIO PRÁTICO
Classe ContaCorrente:
-A classe "ContaCorrente" herda de "Conta"
e inclui atributos específicos, como taxa de manutenção e
limite de cheque especial.
-Deve sobrescrever o método de saque para
considerar o limite de cheque especial, se
necessário.'''


'''DESAFIO PRÁTICO
Classe ContaPoupanca:
-A classe "ContaPoupanca" também herda de "Conta"
e inclui atributos específicos, como taxa de juros.
-Ela deve ter um método para calcular e adicionar juros ao
saldo.
-Crie um método chamado resumo que pode ser chamado
em qualquer objeto de conta (ContaCorrente ou
ContaPoupanca).'''


'''DESAFIO PRÁTICO
Esse método resumo irá exibir um resumo das
informações da conta, incluindo o tipo de conta
(corrente ou poupança), o número da conta, o
titular da conta e o saldo atual.
Teste de Funcionalidade:
Crie um programa principal que demonstre o uso dessas
classes. Crie instâncias de contas correntes e poupanças,
realize depósitos, saques, adicione juros e chame o
método resumo para cada conta.'''

