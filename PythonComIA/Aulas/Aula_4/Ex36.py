# 36 - Crie um algoritmo que ao ser executado recebe uma palavra, verifica se a palavra se inicia com uma vogal
# e exibe a mensagem "Começa em vogal" caso a palavra se inice em vogal
# ou exibe a mensagem "Começa em consoante" caso a palavra não se inicie em vogal

palavra = input('Informe uma palavra: ')

if palavra[0].lower() in ['a','e','i','o','u']:
    print('Começa em vogal')
else:
    print('Começa em consoante')