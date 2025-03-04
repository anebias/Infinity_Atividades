# [PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.

def media(num1, num2, num3):

    if num1.replace('.','').replace('-','').isnumeric() and num2.replace('.','').replace('-','').isnumeric() and num3.replace('.','').replace('-','').isnumeric():
        return (float(num1) + float(num2) + float(num3)) / 3
    else:
        return 'valores inválidos'

# TESTES:
print('teste 1: ',media('3','4.7','5'))
print('teste 2: ',media('1','0','-5.4'))
print('teste 3: ',media('1','0',''))
print('teste 4: ',media('1','0',' '))
print('teste 5: ',media('1','0','.'))
print('teste 6: ',media('1','0','a'))