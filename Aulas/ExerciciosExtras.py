''' https://dontpad.com/dfs7071910 '''
# 1  - Crie um algoritmo em que o usuário informe uma frase qualquer e exiba a frase na tela (terminal) quando executado.
print('\n\n*** Exercício 1 ****')

frase = input('Digite uma frase qualquer: ')
print(frase)

# 2  - Crie um algoritmo em que o usuário informe o nome completo e exiba o nome completo na tela (terminal) quando executado.
print('\n\n*** Exercício 2 ****')
nome_completo = input('Informe o seu nome completo: ')
print(nome_completo)

# 3  - Crie um algoritmo em que o usuário informe a idade e exiba a idade na tela (terminal) quando executado.
print('\n\n*** Exercício 3 ****')
idade = int(input('Informe a sua idade: '))
print(idade)

# 4  - Crie um algoritmo em que o usuário informe dois números inteiros (n1 e n2) e exiba os números na tela (terminal) quando executado.
print('\n\n*** Exercício 4 ****')
numero_1 = int(input('Informe um número inteiro: '))
numero_2 = int(input('Informe outro número inteiro: '))

print(f'Primeiro número: {numero_1}, segundo número: {numero_2}')

# 5  - Crie um algoritmo em que o usuário informe dois números inteiros (n1 e n2) e exiba a soma dos números na tela (terminal) quando executado.
print('\n\n*** Exercício 5 ****')
numero_1 = int(input('Informe um número inteiro: '))
numero_2 = int(input('Informe outro número inteiro: '))
soma = numero_1 + numero_2
print(f'A soma dos números {numero_1} e {numero_2} é {soma}')

# 6  - Crie um algoritmo em que o usuário informe dois números inteiros (x1 e x2) e exiba a diferença dos números na tela (terminal) quando executado.
print('\n\n*** Exercício 6 ****')
numero_1 = int(input('Informe um número inteiro: '))
numero_2 = int(input('Informe outro número inteiro: '))
subtracao = numero_1 - numero_2
print(f'A diferença dos números {numero_1} e {numero_2} é {subtracao}')

# 7  - Crie um algoritmo em que o usuário informe dois números inteiros (a1 e a2) e exiba o produto dos números na tela (terminal) quando executado.
print('\n\n*** Exercício 7 ****')
numero_1 = int(input('Informe um número inteiro: '))
numero_2 = int(input('Informe outro número inteiro: '))
produto = numero_1 * numero_2
print(f'O produto dos números {numero_1} e {numero_2} é {produto}')

# 8  - Crie um algoritmo em que o usuário informe dois números inteiros (x e y) e exiba o quociente dos números na tela (terminal) quando executado.
print('\n\n*** Exercício 8 ****')
numero_1 = int(input('Informe um número inteiro: '))
numero_2 = int(input('Informe outro número inteiro: '))
quociente = numero_1 / numero_2
print(f'O quociente do número {numero_1} pelo número {numero_2} é {quociente}')

# 9  - Crie um algoritmo em que o usuário informe quatro notas (n1, n2, n3 e n4). Após, calcule a média aritmética e exiba a média na tela (terminal) quando executado.
print('\n\n*** Exercício 9 ****')
nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))
nota_3 = float(input('Informe a terceira nota: '))
nota_4 = float(input('Informe a quarta nota: '))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'A média das notas {nota_1}, {nota_2}, {nota_3} e {nota_4} é {media:.2f}')


'''
Desafio: Crie um algorimo que peça ao usuário o email e a senha. Caso o usuário e a senha estejam corretos imprima no terminal:
"Acesso garantido", caso contrário imprima "Acesso negado"; Pre-defina a senha e e-mail corretos e compare com as entradas obtidas através do input.
'''
print('\n\n*** Desafio ****')
print('\n\n*** Cadastro de Usuário ****')
email_acesso = input('Cadastre o seu e-mail: ')
senha_acesso = input('Cadastre a sua senha: ')

print('\n\n*** Acesso ao sistema ****')
email = input('Informe o seu e-mail: ')
senha = input('Informe a sua senha: ')

if email == email_acesso and senha == senha_acesso:
    print('Acesso garantido')
else:
    print('Acesso negado')

'''
Desafio: Crie um algoritmo que rece
# o nome, idade, a fruta favorita e se o usuário é ou não aluno da Infinity School.
# Imprima os valores no seguindo o exemplo:
# Se as informações forem: "João", 34, "banana", as informações devem aparecer dessa forma no terminal:
# Nome: João
# Idade: 34
# Fruta favorita: banana
# Aluno Infinty: Sim  
'''
print('\n\n*** Desafio ****')
nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))
fruta = input('Informe a sua fruta favorita: ')
aluno = input('Você é aluno da Infinity School? (sim, não)')

print(f'\nNome: {nome} \nIdade: {idade} \nFruta favorita: {fruta} \nAluno Infinity: {aluno}')