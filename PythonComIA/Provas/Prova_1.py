'''
[PYIA-A01] Crie uma lista contendo seis frutas de sua escolha. Depois de ter a lista pronta, converta essa lista em uma tupla. Por fim, exiba o conteúdo da tupla resultante para verificar as frutas que foram armazenadas.
'''

lista_frutas = ['laranja', 'banana', 'maça', 'pera', 'uva', 'kiwi']

tupla_frutas = tuple(lista_frutas)
print(f'Tipo Lista: {type(lista_frutas)}, tipo tupla: {type(tupla_frutas)}')

print(tupla_frutas)
