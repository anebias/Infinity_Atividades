import celsius_fahrenheit
import metros_pes
import quilogramas_libras

def menu():
    print('*'*20,'CONVERSÃO DE MEDIDAS','*'*20)
    print('1 - Metros para Pés')
    print('2 - Quilogramas para Libras')
    print('3 - Celsius para Fahrenheit')
    print('4 - Sair')

    opcao = input('\nInforme a sua opção: ')

    if opcao == '1':
        pass
    elif opcao == '2':
        pass
    elif opcao == '3':
        celsius_fahrenheit.converter_celsius()
    elif opcao != '4':
        print("opcao inválida!")
        menu()

menu()