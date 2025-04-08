'''Tela de visualização de reservas:
Apresente uma lista de reservas existentes com a
opção de cancelar reservas específicas.'''

import flet as ft

def main(page:ft.Page):
    page.title = "Gestão de Reservas Realizadas"
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

    cabecalho = ft.Text("GESTÃO DE RESERVAS REALIZADAS", size=36, color="indigo")

    lista_reservas = ''
    def opcoes_reservas():
        opcoes = []
        for reserva in lista_reservas:
            opcoes.append(ft.DropdownOption(reserva))
        return opcoes
    
    container_opcoes_reservas = ft.Dropdown(options=opcoes_reservas(),label = "Reservas",width=400)

    botao_modificar_reserva = ft.ElevatedButton(text="Modificar reserva", bgcolor='indigo',color='white',width=200)
    botao_cancelar_reserva = ft.ElevatedButton(text="Cancelar reserva", bgcolor='indigo',color='white',width=200)

    container_botoes = ft.Row(controls=[botao_modificar_reserva,botao_cancelar_reserva],spacing=10, alignment='center')

    page.add(cabecalho,container_opcoes_reservas,container_botoes)

ft.app(target=main)