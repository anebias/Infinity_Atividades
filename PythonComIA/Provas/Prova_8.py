'''[PYIA-A08] Importe o módulo 'os' e use a função 'listdir' para listar todos os arquivos e pastas presentes no diretório onde o script Python está sendo executado. A função 'listdir' retornará uma lista contendo os nomes dos arquivos e pastas. Após obter essa lista, exiba cada item da lista individualmente na saída do console.'''

from os import listdir

lista_arquivos = listdir()

print('*'*10,'Lista de Arquivos no diretório raiz: ','*'*10)

for item in lista_arquivos:
    print(item)

print('*'*8,'Fim Lista de Arquivos no diretório raiz: ','*'*8)
