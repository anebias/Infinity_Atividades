'''[PYIA-A02] Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.'''

informacoes_contato = dict()

nome = input('Informe o seu nome: ')
while len(nome) < 3 or nome in ' '*999: #Mínimo 3 letras, como Ana
    nome = input('Inválido. Informe o seu nome: ')

telefone = input('Informe o seu telefone: ')
while len(telefone) < 8 or telefone in ' '*999: # Mínimo 8 dígitos
    telefone = input('Inválido. Informe o seu telefone: ')

email = input('Informe o seu e-mail: ')
while len(email) < 7 or email in ' '*999: # 'a@b.com - cumprimento mínimo de e-mail'
    email = input('Inválido. Informe o seu e-mail: ')

informacoes_contato['nome'] = nome
informacoes_contato['telefone'] = telefone
informacoes_contato['email'] = email

print(informacoes_contato)

