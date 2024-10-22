print('\n\n*** Atividade 8 ****')
frase = input('Digite uma frase qualquer: ')
palavra = input('Informe uma palavra para pesquisa na frase: ')

if palavra in frase:
    print(f'A palavra "{palavra}" pesquisada está presente na frase "{frase}"')
else:
    print(f'A palavra "{palavra}" pesquisada não está presente na frase "{frase}"')