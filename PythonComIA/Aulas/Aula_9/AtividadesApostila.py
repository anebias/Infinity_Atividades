# EXEMPLO DA APOSTILA

# import flet as ft

# def main(page: ft.Page):
#     page.title = "Minha aplicação FLET"

#     layout = ft.Column(
#         controls=[ft.Text("Janela Principal", size=20, weight=ft.FontWeight.BOLD),
#                   ft.ElevatedButton("Botão 1"),
#                   ft.ElevatedButton("Botão 2"),
#                   ft.ElevatedButton("Botão 3")]
#     )
#     page.add(layout)

# ft.app(target=main)

'''ATIVIDADE PRÁTICA 1
Criar um Formulário de Cadastro
Propor aos participantes que criem um formulário de cadastro utilizando Flet.
Incluir campos como nome, sobrenome, email, etc.
Encorajar a aplicação de diferentes widgets e layouts para organizar o formulário.'''

# import flet as ft

# def main(page: ft.Page):
    
#     contador = ft.Text(value="Botão clicado 0 vezes") 

#     def evento_botao(e):
#         evento_botao.clicks += 1
#         contador.value = f'Botão clicado {evento_botao.clicks} vezes'
#         texto.value = f'Nome: {nome.value} | email {email.value} | telefone: {telefone.value}'
#         contador.update()
#         texto.update()

#     evento_botao.clicks = 0

#     page.title = "Cadastro"

#     botao = ft.ElevatedButton("Incluir",on_click=evento_botao)
#     texto = ft.Text()

#     nome = ft.TextField(label="Nome Completo")
#     email = ft.TextField(label="E-mail")
#     telefone = ft.TextField(label="Telefone")

#     layout = ft.Column(controls=[nome,email,telefone, botao, contador, texto])
#     page.add(layout)

# ft.app(target=main)

'''ATIVIDADE PRÁTICA 2
Criar um Aplicativo de Lista de Tarefas
Propor aos participantes que criem um aplicativo de lista de tarefas simples utilizando Flet.
Incluir funcionalidades como adicionar, remover e marcar tarefas como concluídas.
Incentivar a utilização de eventos e interações do usuário.'''


'''ATIVIDADE PRÁTICA 3
Crie um Aplicativo de Calculadora Simples
O aplicativo deve ser capaz de realizar operações básicas de matemática, como adição, subtração, multiplicação e divisão.
Implemente uma interface limpa e intuitiva, com botões para os números e operações, além de uma área para exibir o resultado das operações.'''


'''ATIVIDADE PRÁTICA 4
Desenvolvendo um Bloco de Notas Básico
Crie um bloco de notas básico usando Flet.
O bloco de notas deve permitir aos usuários digitar, editar e salvar texto.
A interface deve ser clara e direta, com menus ou botões para acessar as
funcionalidades principais, como abrir, salvar e editar o texto.
Opcional:Implemente funcionalidades adicionais simples, como opções
de formatação de texto (negrito, itálico, etc.) ou contagem de palavras.'''


