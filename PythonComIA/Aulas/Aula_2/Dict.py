# meu_dict = {}
# print(meu_dict)
# meu_dict = dict()
# print(meu_dict)
# meu_dict = dict([('Modulo', 'Python'),('Instituição', 'Infinity')])
# print(meu_dict)
# meu_dict = dict(Modulo = 'Python', Instituicao = 'Infinity')
# print(meu_dict)

# # Usando compreensão de dicionários
# meu_dict = {elemento: f'Valor {elemento}' for elemento in range(6)}
# print(meu_dict)

# # Usando items()
# meu_dict = {'Programação1':'Python' ,'Programação02':'JavaScript' ,'Programação3': 'PHP' }
# print(meu_dict)
# for i in meu_dict.items():
#     print(i)

# for i,j in meu_dict.items():
#     print(f'Chave {i}, Valor {j}')

# print(meu_dict['Programação1'])
# print(meu_dict.get('Programação1'))

# # ATIVIDADE PRÁTICA 8
# # Escreva um programa que EXIBA um dicionário contendo
# # informações de pessoas (nome, idade) e exiba essas informações.
# pessoas = {'Nome': 'Alessandra', 'idade': 50}
# print(pessoas.get('Nome'), pessoas['idade'], sep=' - ')

# ATIVIDADE PRÁTICA 9
# Escreva um programa que percorra as chaves e valores
# de um dicionário separadamente e os exiba.

# meu_dict = {f'chave {i}': f'valor {i}' for i in range(5)}
# print(meu_dict)
# for i,j in meu_dict.items():
#     print(f'Chave: {i} \nValor: {j}')

# ATIVIDADE PRÁTICA 10
# Desenvolva um programa que recebe um dicionário, uma
# chave e um valor como entrada e adiciona a chave e o
# valor ao dicionário, atualizando o valor se a chave já existir.
# meu_dict = input('Informe o dicionario: ')
# chave = input('Informe a chave: ')
# valor = input('Informe o valor: ')

# meu_dict = dict([(chave,valor)])
# print(meu_dict)

# ATIVIDADE PRÁTICA 11
# Escreva um programa que recebe um dicionário e uma
# lista de chaves como entrada e verifica se todas as
# chaves da lista existem no dicionário. A função deve
# retornar True se todas as chaves existirem e False caso 
# contrário.

# meu_dict = {f'{i}':f'v{i}' for i in range(10)}
# print('*'*10,'Dicionário','*'*10)
# meu_dict = {}
# while True:
#     chave_dict = input('Informe a chave ou # para sair: ')
#     if chave_dict != '#':
#         valor_dict = input('Informe o valor: ')
#         meu_dict[chave_dict] = valor_dict
#     else:
#         break

# lista_chaves = []

# print('\n\n','*'*10,'Lista de Chaves para pesquisa','*'*10)

# while True:
#     chave = input('Informe a chave ou # para sair: ')
#     if chave != '#':
#         lista_chaves.append(chave)
#     else:
#         break

# key_exist = True

# for i in lista_chaves:
#     if i not in set(list(meu_dict)):
#         key_exist = False

# print(key_exist)

# ATIVIDADE PRÁTICA 12
# Crie um programa que simule um sistema de votação. O
# programa deve permitir que os eleitores escolham entre
# opções de eleitores e conte os votos para cada opção.
# Use um dicionário para armazenar os resultados da
# votação, onde as chaves são as opções e os valores são o
# número de votos para cada opção. O programa deve
# permitir que os eleitores votem, encerre a votação e exiba
# os resultados finais. Use While True e pare o programa
# somente se o usuário digitar o número 0 e exiba os
# resultados finais.

# total_caracteres_divisao = 50
# titulo = 'Abertura da Urna de Votação'
# tamanho_titulo = len(titulo)
# tamanho_laterais = int((total_caracteres_divisao - tamanho_titulo - 2)/2)
# print('*' * total_caracteres_divisao)
# print('*' * tamanho_laterais,titulo,'*' * tamanho_laterais)
# print('*' * total_caracteres_divisao,end='\n\n')

# quantidade_candidatos = input('informe o número de candidados: ')

# while not quantidade_candidatos.isnumeric():
#     quantidade_candidatos = input('Inválido. Informe um número: ')

# quantidade_candidatos = int(quantidade_candidatos)
# urna_votacao = {}

# for i in range(quantidade_candidatos):
#     urna_votacao[f'Candidato_{i+1}'] = 0

# candidatos = list(urna_votacao)
# lista_opcoes = ''

# for i in range(quantidade_candidatos):
#     lista_opcoes += str(i+1)

# print('\n','*'*5,'Urna de Votação','*'*5)

# while True:
#     print('Digite o número correspondente ao seu candidato ou 0 (zero) para sair')

#     for i,candidato in enumerate(candidatos):
#         print(f'{i+1} - {candidato}')
#     print('\n0 - Sair')

#     voto = input('Voto: ')

#     if voto in lista_opcoes:
#         urna_votacao[f'Candidato_{voto}'] += 1
#     elif voto == '0':
#         break
#     else:
#         print('Opção inválida !')
    
# titulo = 'Resultado da Votação'
# tamanho_titulo = len(titulo)
# tamanho_laterais = int((total_caracteres_divisao - tamanho_titulo - 2)/2)

# print('*' * total_caracteres_divisao)
# print('*' * tamanho_laterais,titulo,'*' * tamanho_laterais)
# print('*' * total_caracteres_divisao,end='\n\n')

# for chave,valor in urna_votacao.items():
#     print(f'{chave} - {valor} votos')

# ATIVIDADE PRÁTICA 13
# Crie um dicionário que relacione nomes de alunos às suas
# notas em uma disciplina. Calcule a média das notas e exiba-a.

# notas_alunos = {}
# quantidade_alunos = ''
# quantidade_notas = ''

# while not quantidade_alunos.isnumeric():
#     quantidade_alunos = input('Informe a quantidade de alunos para lançamento: ')

# while not quantidade_notas.isnumeric():
#     quantidade_notas = input('Informe a quantidade de notas a ser lançada para cada aluno: ')

# quantidade_alunos = int(quantidade_alunos)
# quantidade_notas = int(quantidade_notas)

# for i in range(quantidade_alunos):
#     notas = []
#     aluno = input('Informe o nome do aluno: ')
#     for j in range(quantidade_notas):
#         nota = ''
#         while not nota.isnumeric():
#             nota = input(f'Informe a {j +1} nota: ')
#         notas.append(nota)
#     notas_alunos[aluno] = notas

# medias_alunos = {}
# for aluno,notas in notas_alunos.items():
#     media = 0
#     soma = 0
#     for nota in notas:
#         soma += float(nota)
#     media = soma / quantidade_notas
#     medias_alunos[aluno] = media

# print(medias_alunos)

# ATIVIDADE PRÁTICA 14
# Crie um programa que receba uma lista de números e
# remova todas as duplicatas usando um conjunto (set). Em
# seguida, exiba a lista original e a lista sem duplicatas.

# lista_original = []
# lista_exclusivos = {}

# numero = ''

# while True:
#     numero = input('Informe um número ou * para sair: ')
#     while not numero.isnumeric() and numero != '*':
#         numero = input('Inválido. Informe um número ou * para sair: ')
#     if numero == '*':
#         print('Saindo...')
#         break
#     else:
#         lista_original.append(numero)
    
# lista_exclusivos = set(lista_original)
# lista_exclusivos = list(lista_exclusivos)

# print('Lista Original\n',lista_original)
# print('Lista sem duplicidade\n',lista_exclusivos)

# ATIVIDADE PRÁTICA 15
# Crie um programa que realize a união de múltiplos
# conjuntos e exiba o conjunto resultante.

# conjunto = set()
# item = novo_conjunto = ''
# while novo_conjunto != '*':
#     novo_conjunto = input('Informe o nome do conjunto ou "*" para sair: ')
#     if novo_conjunto == '*':
#         break
#     else:
#         novo_conjunto = {''}
#         while item != '*':
#             item = input(f'Informe o novo elemento do conjunto {novo_conjunto} ou "*" para finalizar a inclusão: ')
#             if item == '*':
#                 break
#             else:
#                 novo_conjunto.add(item)

# print(novo_conjunto)

# DESAFIO PRÁTICO
# Sistema de Cadastro de Alunos - passo 1
# Cadastro de Alunos: O programa deve permitir ao usuário
# cadastrar alunos. Cada aluno terá as seguintes
# informações: nome, idade e notas em três disciplinas:
# Matemática, Ciências e História. Os dados de cada aluno
# devem ser armazenados em um dicionário com as
# seguintes chaves: 'nome','idade','notas'. As notas devem
# ser armazenadas em uma tupla.

print('*'*10,'CADASTRO DE ALUNOS E NOTAS', '*'*10)
print('Instruções:')
print('Para cada aluno será necessário informar:\n1. Nome\n2. Idade \n3. Três notas: Matemática, Ciências e História, nesta ordem\n')

disciplinas = ['Matemática', 'Ciências', 'História']
cadastro_alunos = dict()
contador = 0

while True:

    nome = input('Informe o nome do aluno ou "*" para sair: ').capitalize()

    if nome == '*':
        break
    else:
        while (len(nome) < 3 or nome in ' '*999):
            nome = input('Nome inválido. Digite novamente: ').capitalize()

        idade = input(f'Informe a idade do aluno {nome}: ')

        while (not idade.isdigit() or idade in ' '*999):
            idade = input('Idade inválida. Digite novamente: ')

        notas_aluno = []
        for disciplina in disciplinas:
            nota = input(f'Informe a nota de {disciplina} do aluno {nome}: ')
            while not nota.replace('.','').isnumeric() or nota in ' '*999:
                nota = input('Nota inválida. Digite novamente: ')
            notas_aluno.append(float(nota))

        cadastro_alunos[f'{contador}'] = {'nome': nome, 'idade': idade, 'notas': tuple( notas_aluno)}
        contador += 1

print(cadastro_alunos)

# DESAFIO PRÁTICO
# Sistema de Cadastro de Alunos - passo 2
# Visualização de Alunos: O programa deve permitir ao usuário
# visualizar todos os alunos cadastrados, exibindo suas informações
# de forma organizada.
# Média de Notas: O programa deve calcular a média das
# notas de cada aluno e exibi-la.
# Aluno com Melhor Média: O programa deve identificar e
# exibir o aluno com a melhor média de notas.

print('*'*10,'ALUNOS CADASTRADOS','*'*10)

contador = 0
lista_medias = []

for chave, valor in cadastro_alunos.items():
    contador += 1
    print(f'Nome do Aluno: {cadastro_alunos[chave]['nome']}')
    print(f'Idade: {cadastro_alunos[chave]['idade']}')
    soma = media = 0
    
    print('Notas do aluno:', end=' ')
    for i, nota in enumerate(cadastro_alunos[chave]['notas']):
        if i != len(cadastro_alunos[chave]['notas']):
            print(f'{disciplinas[i]}: {nota}', end=', ')
        else:
            print(f'{disciplinas[i]}: {nota}')
        soma += nota
    media = soma / 3
    lista_medias.append(media)

    print(f'Média do Aluno: {media:.2f}')
    print('*'*30)

# Buscar aluno com melhor desempenho
melhor_desempenho = lista_medias[0]
aluno_melhor_desempenho = 0

for j in range(len(lista_medias)-1):
    if lista_medias[aluno_melhor_desempenho] < lista_medias[j+1]:
        melhor_desempenho = lista_medias[j+1]
        aluno_melhor_desempenho = j + 1

nome_aluno_melhor_desempenho = cadastro_alunos.get(f'{aluno_melhor_desempenho}')['nome']
print('Aluno com melhor desempenho: ',nome_aluno_melhor_desempenho)
print('*'*30)

# from datetime import datetime
# antes = datetime.now()
# depois = datetime.now()
# diferenca = depois - antes
# print(diferenca)
