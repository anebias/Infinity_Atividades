# Continue no FOR pula as etapas seguintes e vai para a próxima iteração.

#Exemplo de pular números ímpares
for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i)

#Exemplo de aninhamento de FOR, break e continue com else:

for num in range(2,20):
    for i in range(2,num):
        if num % i ==0:
            break
    else:
        print(f'{num} é um número primo')