def soma(num1,num2):

    if num1.replace('.','').isnumeric() and num2.replace('.','').isnumeric():
        return float(num1) + float(num2)
    else:
        return 'Valores inválidos'

def subtracao(num1,num2):

    if num1.replace('.','').isnumeric() and num2.replace('.','').isnumeric():
        return float(num1) - float(num2)
    else:
        return 'Valores inválidos'

def multiplicacao(num1,num2):

    if num1.replace('.','').isnumeric() and num2.replace('.','').isnumeric():
        return float(num1) * float(num2)
    else:
        return 'Valores inválidos'

def divisao(num1,num2):

    if num2 == '0':
        return 'Não é possível dividir por zero'
    elif num1.replace('.','').isnumeric() and num2.replace('.','').isnumeric():
        return float(num1) / float(num2)
    else:
        return 'Valores inválidos'