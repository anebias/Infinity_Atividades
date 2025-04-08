'''Gerenciamento de clientes:
Inclua uma tela para visualizar, adicionar e editar
informações dos clientes.'''

import flet as ft

def main(page:ft.Page):
    page.title = "Gestão de Clientes"
    page.padding = 40
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme = ft.Theme(color_scheme=ft.ColorScheme(
        primary=ft.colors.INDIGO, #botões primários, barras navegação, elementos destaque
        secondary=ft.colors.BLUE, #botões secundários, pequenos elementos
        background=ft.colors.WHITE, #tela fundo
        surface=ft.colors.INDIGO, #cartões, caixas diálogo, listas
        on_primary=ft.colors.WHITE, #cor sobre os elementos primários
        on_secondary=ft.colors.WHITE, #cor sobre os elementos secundários
        on_background=ft.colors.INDIGO, #cor dos elementos sobre o fundo
        on_surface=ft.colors.WHITE #cor sobre os elementos de superfície
    ))

    cabecalho = ft.Text("GESTÃO DE CLIENTES", size=36, color="indigo")

    nome = ft.TextField(label="Nome")
    telefone = ft.TextField(label="Telefone")
    email = ft.TextField(label="Email")
    __id = '123'

    linha_captura_dados_cliente = ft.Row([nome, telefone, email],alignment='center')

    botao_adicionar_cliente = ft.ElevatedButton(text="Adicionar Cliente", bgcolor='indigo',color='white',width=200)
    botao_editar_cliente = ft.ElevatedButton(text="Editar Cliente", bgcolor='indigo',color='white',width=200)
    botao_consultar_cliente = ft.ElevatedButton(text="Consultar Cliente", bgcolor='indigo',color='white',width=200)

    container_botoes = ft.Row(controls=[botao_adicionar_cliente, botao_editar_cliente, botao_consultar_cliente],spacing=10, alignment='center')

    lista_clientes = ''
    def opcoes_clientes():
        opcoes = []
        for cliente in lista_clientes:
            opcoes.append(ft.DropdownOption(cliente))
        return opcoes
    
    container_opcoes_clientes = ft.Dropdown(options=opcoes_clientes(),label = "Clientes",width=400)

    botao_consultar_dados_cliente = ft.ElevatedButton(text="Consultar Dados do Cliente", bgcolor='indigo',color='white',width=200)

    page.add(cabecalho, container_botoes,linha_captura_dados_cliente,  container_opcoes_clientes, botao_consultar_dados_cliente)

ft.app(target=main)