'''
[LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

Ao final, exiba a média geral da turma.
'''

print('*** Média das notas dos alunos da turma ***\n')
quantidade_alunos = 0
media_geral = soma_geral = 0

while quantidade_alunos <= 0:
    quantidade_alunos = int(input('Informe o número de alunos da turma: '))

for i in range(quantidade_alunos):
    media_notas = 0
    nota_1 = nota_2 = nota_3 = -1
    aluno = input('\nInforme o nome do aluno: ')
    while nota_1 < 0:
        nota_1 = float(input('Informe a 1ª nota do aluno: '))
    while nota_2 < 0:
        nota_2 = float(input('Informe a 2ª nota do aluno: '))
    while nota_3 < 0:
        nota_3 = float(input('Informe a 3ª nota do aluno: '))

    media_notas = (nota_1 + nota_2 + nota_3) / 3

    soma_geral += media_notas

    if media_notas >= 7:
        print(f'O aluno {aluno}, obteve as notas {nota_1}, {nota_2}, {nota_3} e foi aprovado com nota média {media_notas: .2f}')
    else:
        print(f'O aluno {aluno}, obteve as notas {nota_1}, {nota_2}, {nota_3} e foi reprovado com nota média {media_notas:.2f}')

print(f'\nA média geral da turma é: {(soma_geral / quantidade_alunos):.2f}')