print('*** Exercício 9 ***')

opcao = input('Digie "pedra", "papel" ou "tesoura" :').lower()

while opcao != "pedra" and opcao != "papel" and opcao != "tesoura":
    opcao = input('Escolha inválida, tente novamente: ').lower()

print(f'Opção selecionada foi {opcao}')