inteiro = '2' #isdecimal, isdigit, isnumeric
decimal = '2.4'
negativo = '-1'

novo = decimal.replace('.','')
print(novo.isnumeric())
print(float(decimal))
print(negativo.isdecimal())

print(decimal.isdigit())
print(negativo.isdigit())

print(decimal.isnumeric())
print(negativo.isnumeric())


