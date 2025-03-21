# 38 - Crie um algoritmo que ao ser executado recebe uma frase, 
# e verifica se uma letra escolhida por você está presente na frase
# caso a frase contenha a letra escolhida deve ser exibida a mensagem "A letra <letra> está presente na frase"
# caso contrário deve ser exibida a frase "A letra <letra> não está contida na frase"

frase = input('Digite uma frase: ').lower()
letra_escolhida = input('Escolha uma letra: ').lower()

if letra_escolhida in frase:
    print(f'A letra {letra_escolhida.upper()} está presente na frase')
else:
    print(f'A letra {letra_escolhida.upper()} não está na frase')


