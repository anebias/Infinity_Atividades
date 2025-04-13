'''Tela de visualização de reservas:
Apresente uma lista de reservas existentes com a
opção de cancelar reservas específicas.'''

import flet as ft
from class_gerenciadorReservas import GerenciadorReservas
from testes import testes

gerenciador = GerenciadorReservas()
testes(gerenciador)

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
        on_primary=ft.colors.BLACK, #cor sobre os elementos primários
        on_secondary=ft.colors.BLACK, #cor sobre os elementos secundários
        on_background=ft.colors.INDIGO, #cor dos elementos sobre o fundo
        on_surface=ft.colors.BLACK #cor sobre os elementos de superfície
    ))

    cabecalho = ft.Text("GESTÃO DE RESERVAS REALIZADAS", size=36, color="indigo")

    # FUNÇÕES DA PÁGINA
    lista_reservas = gerenciador.listar_reservas()

    def opcoes_reservas():
        opcoes = []
        for reserva in lista_reservas:
            opcoes.append(ft.DropdownOption(reserva))
        return opcoes
    
    lista_quartos = gerenciador.listar_quartos_disponibilidades()
    def opcoes_quartos():
        opcoes = []
        for quarto in lista_quartos:
            opcoes.append(ft.DropdownOption(quarto))
        return opcoes
    
    def visualizar_container(e):
        linha_modificacao.visible = True
        botao_modificar_reserva.visible = False
        botao_cancelar_reserva.visible=False
        container_opcoes_reservas.disabled = True
        page.update()

    container_opcoes_reservas = ft.Dropdown(options=opcoes_reservas(),label = "Reservas",width=600)

    botao_modificar_reserva = ft.ElevatedButton(text="Modificar reserva", bgcolor='indigo',color='white',width=200, on_click=visualizar_container)
    botao_cancelar_reserva = ft.ElevatedButton(text="Cancelar reserva", bgcolor='indigo',color='white',width=200)

    container_botoes = ft.Row(controls=[botao_modificar_reserva,botao_cancelar_reserva],spacing=10, alignment='center')

    # ESSE CONTAINER DEVERÁ FICAR VISÍVEL SOMENTE SE SELECIONAR MODIFICAR RESERVA
    # ********** QUARTOS **************
    container_opcoes_quartos = ft.Dropdown(options=opcoes_quartos(),label = "Quartos",width=400)

    data_reserva_inicio = ft.TextField(label="Data Início Reserva",width=195)
    data_reserva_final = ft.TextField(label="Data Início Reserva",width=195)

    linha_selecao = ft.Row([data_reserva_inicio,data_reserva_final],alignment='center')

    botao_confirmar_alteracao_reserva = ft.Row(controls= [ft.ElevatedButton(text="Confirmar Alteração", bgcolor='indigo',color='white',width=200)],alignment='center')

    container_modificacao = ft.Column(controls=[container_opcoes_quartos,linha_selecao,botao_confirmar_alteracao_reserva],alignment='center')

    linha_modificacao = ft.Row(controls=[container_modificacao],alignment='center', visible=False)

    page.add(cabecalho,container_opcoes_reservas,container_botoes,linha_modificacao)

ft.app(target=main)