
'''Tela inicial:
Exiba uma lista de quartos e suas respectivas
disponibilidades.
Inclua botões para realizar reservas, consultar
informações de clientes e gerenciar reservas.'''

import flet as ft
from class_gerenciadorReservas import GerenciadorReservas

gerenciador = GerenciadorReservas()

def main(page:ft.Page):
    
    page.title = "Gerenciador de Reservas"
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

    cabecalho = ft.Text('Consulta de Disponibilidade dos Quartos',text_align="center",size=24, color="blue")

    lista_quartos = gerenciador.lista_quartos()

    def opcoes_quartos():
        opcoes = []
        for quarto in lista_quartos:
            opcoes.append(ft.DropdownOption(quarto))
        return opcoes
    container_opcoes = ft.Dropdown(options=opcoes_quartos(),label = "Quartos",width=300)

    botao_reserva = ft.ElevatedButton(text="Realizar RESERVA")
    botao_consultar_clientes = ft.ElevatedButton(text="Consultar Clientes")
    botao_gerenciar_reservas = ft.ElevatedButton(text="Gerenciar Reservas")

    container_botoes = ft.Row(controls=[botao_reserva, botao_consultar_clientes, botao_gerenciar_reservas],alignment="center")

    page.add(cabecalho,container_opcoes,container_botoes)

ft.app(target=main)
