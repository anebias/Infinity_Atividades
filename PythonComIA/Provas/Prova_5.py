# [PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. Esta função deve comparar os três números e identificar qual deles é o maior. Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.

def maior(num1 , num2, num3):
    
    if (num1.replace('.','').replace('-','').isnumeric() and num1 not in ' ') and (num2.replace('.','').replace('-','').isnumeric() and num2 not in ' ') and (num3.replace('.','').replace('-','').isnumeric() and num3 not in ' '):

        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
        
        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num1 and num2 >= num3:
            return num2
        else:
            return num3
        
    else:
        return 'valores não numéricos'

# TESTES
print(maior('2','2','2'))
print(maior('2','1','2'))
print(maior('1','2','2'))
print(maior('2','2','1'))

# print(maior('1','2.99','3'))
# print(maior('1','3','2.99'))
# print(maior('2.99','1','3'))
# print(maior('2.99999','3','1'))
# print(maior('3','1','2.999'))
# print(maior('3','2.999','1'))
# print(maior('','2.999','1'))
# print(maior(' ','2.999','1'))
# print(maior('a','2.999','1'))
# print(maior('.','2.9999','1'))



