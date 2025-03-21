import manipulacao_strings as ms

while True:
    print('\nMANIPULADOR DE PALAVRAS')
    print('1 : Inverter PALAVRA')
    print('2 : Contar caracteres da PALAVRA')
    print('3 : Verificar se PALAVRA é PALÍNDROMO')
    print('4 : Sair')

    opcao = input('Informe a opção desejada: ')

    if opcao == '1':
        palavra = input('Informe a palavra: ')
        if palavra not in ' '*999:
            print(f'a palavra {palavra} invertida é {ms.inverter_string(palavra)}')
        else:
            print('Não é aceito palavra "vazia"')
    
    elif opcao == '2':
        palavra = input('Informe a palavra: ')
        if palavra not in ' '*999:
            print(f'a palavra {palavra} possui {ms.contar_caracteres(palavra)} caracteres')
        else:
            print('Não é aceito palavra "vazia"')
            
    elif opcao == '3':
        palavra = input('Informe a palavra: ')
        if palavra not in ' '*999:
            print(f'a palavra {palavra} {"é" if ms.ispalindromo(palavra) else "não é"} um palíndromo')
        else:
            print('Não é aceito palavra "vazia"')

    elif opcao == '4':
        break

    else:
        print('Opção inválida. Tente novamente.')