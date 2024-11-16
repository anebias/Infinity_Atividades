# Definição dos parâmetros de validação
usuario_valido = 'usermain'
senha_valida = 'senha1234'

print('Menu de acesso \nVocê tem 3 tentativas')

usuario = input('Informe o seu usuário: ')
senha = input('Informe a sua senha: ')

tentativas = 3

while tentativas <=3 and tentativas > 0:
    tentativas -= 1
    validado = usuario == usuario_valido and senha == senha_valida

    if validado:
        print ('Seja bem vindo !')
        break
    else:
        print(f'Usuário ou senha inválidos. Você tem {tentativas} tentativas.')
        usuario = input('Informe o seu usuário: ')
        senha = input('Informe a sua senha: ')
        
if not validado:   
    for i in range(3):
        print('Acesso bloqueado')