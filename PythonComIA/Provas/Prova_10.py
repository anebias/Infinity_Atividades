'''[PYIA-A10] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um formulário de contato. O formulário deve incluir três campos: um campo de texto para o nome, um campo de texto para o email e um campo de texto para a mensagem. Após o usuário preencher esses campos, deve haver um botão de envio. Quando o usuário clicar no botão de envio, os dados devem ser processados e uma mensagem de confirmação deve ser exibida na tela, indicando que o formulário foi enviado com sucesso.'''

import flet as ft

def main(page: ft.Page):
    page.title = "Prova 10 - FLET"

    def enviar(e):
        mensagem.value = "Enviado com sucesso"
        mensagem.update()
        nome.value = ""
        nome.update()
        email.value = ""
        email.update()

    nome = ft.TextField(label='Nome')
    email = ft.TextField(label='Email')
    mensagem = ft.Text(size=24, color='pink',weight='bold')

    botao = ft.ElevatedButton('Enviar',on_click=enviar, bgcolor='pink', color='white')

    page.add(nome,email, botao, mensagem)

ft.app(target=main)