# inverter uma string, contar o número de palavras
#  em uma string e verificar se uma string é um
#  palíndromo (lê-se igual de trás para frente)

def inverter_string(string):
    string_invertida = ''
    for i in range(len(string) - 1,-1,-1):
        string_invertida += string[i]
    return string_invertida

def contar_caracteres(string):
    return len(string)

def ispalindromo(string):
    return string == inverter_string(string)
