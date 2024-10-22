'''
Atividade 01:
Comparação de Idades:
Peça ao usuário duas idades e use operadores de comparação para
verificar se a primeira idade é maior, menor ou igual à segunda.
'''
print('\n\n*** Atividade 1 ****')

idade_1 = int(input('Informe a primeira idade: '))
idade_2 = int(input('Informe a segunda idade: '))

if idade_1 > idade_2:
    print('A primeira idade é maior que a segunda')
elif idade_1 < idade_2:
    print('A primeira idade é menor que a segunda')
else:
    print('As duas idades são iguais')

'''
Atividade 02:
Verificar Igualdade de Strings:
Peça ao usuário duas palavras e use operadores
de comparação para verificar se elas são iguais.
'''
print('\n\n*** Atividade 2 ****')

palavra_1 = input('Digite uma palavra: ')
palavra_2 = input('Digite outra palavra: ')

if palavra_1 == palavra_2:
    print('As palavras digitadas são iguais')
else:
    print(f'As palavras digitadas {palavra_1} e {palavra_2} são diferentes')

'''
Atividade 03:
Verificação de Maioridade e Habilitação:
Crie um programa que peça a idade do usuário e se ele possui habilitação
(sim ou não). Use operadores lógicos para verificar se ele é maior de idade
(>= 18) e possui habilitação.
'''
print('\n\n*** Atividade 3 ****')

idade = int(input('Informe a sua idade: '))

if idade >= 18:
    habilitacao = input('Você possui habilitação (sim ou não): ')
    if habilitacao == 'sim':
        print('Você é maior de idade e possui habilitação')
    else:
        print('Você é maior de idade e mas não possui habilitação')
else:
    print('Você não tem idade para ter habilitação')

'''
Atividade 04:
Verificação de Notas Aprovadas:
Escreva um programa que peça duas notas de um aluno. Use operadores
lógicos para verificar se as duas notas são maiores ou iguais a 6.
'''
print('\n\n*** Atividade 4 ****')

nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))

if nota_1 >= 6 and nota_2 >= 6:
    print('As duas notas são maiores que 6')
elif nota_1 >= 6 and nota_2 < 6:
    print('A primeira nota é maior que 6, mas a segunda nota é menor que 6')
elif nota_1 < 6 and nota_2 >= 6:
    print('A segunda nota é maior que 6, mas a primeira nota é menor que 6')
else:
    print('As duas notas são menores que 6')

'''
Atividade 05:
Desconto em Preço:
Peça ao usuário para inserir o preço de um produto e, em seguida,
use o operador de atribuição -= para aplicar um desconto de 5%.
'''
print('\n\n*** Atividade 5 ****')
preco = float(input('Informe o preço do produto: '))
preco -= preco * 0.05
print(f'O preço do produto com desconto é R${preco:.2f}')

'''
Atividade 06:
Dobro do Valor:
Solicite ao usuário um número e use o operador de
atribuição *= para dobrar o valor e exibir o resultado.
'''
print('\n\n*** Atividade 6 ****')
numero = float(input('Informe um número: '))
numero *= 2

print(f'O dobro do número informado é {numero}')

'''
Atividade 07:
Verificação de Caracteres em uma String:
Crie um programa que peça ao usuário uma frase e um caractere.
Use o operador de associação in para verificar se o caractere está
presente na frase.
'''
print('\n\n*** Atividade 7 ****')
frase = input('Digite uma frase qualquer: ')
caractere = input('Informe um caracter para pesquisa na frase: ')

if caractere in frase:
    print(f'O caractere "{caractere}" pesquisado está presente na frase "{frase}"')
else:
    print(f'O caractere "{caractere}" pesquisado não está presente na frase "{frase}"')

'''
Atividade 08:
Verificação de Palavras em uma Frase:
Peça ao usuário para inserir uma frase e uma palavra.
Use in para verificar se a palavra está na frase.
'''
print('\n\n*** Atividade 8 ****')
frase = input('Digite uma frase qualquer: ')
palavra = input('Informe uma palavra para pesquisa na frase: ')

if palavra in frase:
    print(f'A palavra "{palavra}" pesquisada está presente na frase "{frase}"')
else:
    print(f'A palavra "{palavra}" pesquisada não está presente na frase "{frase}"')
