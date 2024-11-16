# Definição dos parâmetros de validação
usuario_valido = 'usermain'
senha_valida = 'senha1234'

print('*** Menu de acesso *** \n*** Você tem 3 tentativas ***')

usuario = input('Informe o seu usuário: ')
senha = input('Informe a sua senha: ')

tentativa = 1

while tentativa <=3:
    validado = usuario == usuario_valido and senha == senha_valida

    if validado:
        print ('Seja bem vindo !')
        break
    elif tentativa < 3:
        print(f'Usuário ou senha inválidos. Você tem {3 - tentativa} tentativas.')
        usuario = input('Informe o seu usuário: ')
        senha = input('Informe a sua senha: ')
        tentativa += 1
    else:
        for i in range(3):
            print('Acesso bloqueado')
        break