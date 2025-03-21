import operacoes as op

while True:
    print('CALCULADORA')
    print('1 : Somar dois números')
    print('2 : Subtrair dois números')
    print('3 : Multiplicar dois números')
    print('4 : Dividir dois números')
    print('5 : Sair')

    opcao = input('Informe a opção desejada: ')

    if opcao == '1':
        num1 = input('Informe o primeiro número: ')
        num2 = input('Informe o segundo número: ')
        print(f'{num1} + {num2} =',op.soma(num1, num2))
    
    elif opcao == '2':
        num1 = input('Informe o primeiro número: ')
        num2 = input('Informe o segundo número: ')
        print(f'{num1} - {num2} =',op.subtracao(num1, num2))

    elif opcao == '3':
        num1 = input('Informe o primeiro número: ')
        num2 = input('Informe o segundo número: ')
        print(f'{num1} * {num2} =',op.multiplicacao(num1, num2))

    elif opcao == '4':
        num1 = input('Informe o primeiro número: ')
        num2 = input('Informe o segundo número: ')
        print(f'{num1} / {num2} =',op.divisao(num1, num2))

    elif opcao == '5':
        break

    else:
        print('Opção inválida. Tente novamente.')