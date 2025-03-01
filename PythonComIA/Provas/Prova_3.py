'''[PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.'''

print('*'*10,'LISTA DE COMPRAS','*'*10)
print('Orientações: ')
print('Será solicitado o "nome" e o "valor" dos 5 produtos da compra. O nome do produto não pode ter espaços em branco; se for palavra composta utilizar "_" para separação. Exemplo: "copo_descartavel". O valor deverá ser separado por "." e não utilizar ",".')

lista_compras = dict()


for i in range(5):
    nome_produto = input('Informe o nome do produto: ').capitalize()
    while len(nome_produto) < 1 or " " in nome_produto:
        nome_produto = input('Nome inválido. Informe o nome do produto: ').capitalize()

    valor_produto = input('Informe o valor do produto: ')
    while not valor_produto.replace('.','').isnumeric() or valor_produto in ' '*999:
        valor_produto = input('Valor inválido. Informe um valor válido: ')

    lista_compras[f'{nome_produto}'] = float(valor_produto)

valor_total_compra = 0

for item in lista_compras.items():
    valor_total_compra += item[1]

print(f'\nO valor total da compra é de R$ {valor_total_compra:.2f}')

#######################
# O exercício não solicitou para imprimir a lista de compras, mas aproveitei para exercitar.
# EXTRA DO EXERCÍCIO:

print('\n','*'*10,'LISTA DE COMPRAS','*'*10)
for chave, valor in lista_compras.items():
    print(f'Item: {chave} - R$ {valor:.2f}')

print(f'\nO valor total da compra é de R$ {valor_total_compra:.2f}')
#######################