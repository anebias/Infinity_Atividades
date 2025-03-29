'''[PYIA-A09] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento. A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.'''

import flet as ft

def main(page:ft.Page):
    
    lista_tarefas = ft.Column(controls=[])

    titulo = ft.Text('Lista de Tarefas', size=40, color="pink600", weight=ft.FontWeight.BOLD )

    subtitulo = ft.Text('Lista de Tarefas Cadastradas', size=30, color="black",weight=ft.FontWeight.BOLD)

    def cadastrar_tarefa(e):
        nova_tarefa = ft.Text(tarefa_digitada.value, size=24)
        lista_tarefas.controls.append(nova_tarefa)
        lista_tarefas.update()
        tarefa_digitada.value = ""
        tarefa_digitada.update()

    tarefa_digitada = ft.TextField(label="Informe o nome da tarefa a ser cadastrada")
    botao = ft.ElevatedButton('Cadastrar tarefa',on_click=cadastrar_tarefa)

    leiaute = ft.Column(controls=[titulo,tarefa_digitada,botao,subtitulo,lista_tarefas])

    page.add(leiaute)

ft.app(target=main)
