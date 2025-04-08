'''Formulário de reserva:
Permita que o usuário escolha o cliente, o quarto e
as datas desejadas para criar uma nova reserva.'''

import flet as ft

def main(page:ft.Page):
    page.title = "Gestão de Reservas"
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

    cabecalho = ft.Text("GESTÃO DE RESERVAS", size=36, color="indigo")

    # ********** CLIENTES **************
    lista_clientes = ''
    def opcoes_clientes():
        opcoes = []
        for cliente in lista_clientes:
            opcoes.append(ft.DropdownOption(cliente))
        return opcoes
    
    container_opcoes_clientes = ft.Dropdown(options=opcoes_clientes(),label = "Clientes",width=400)
    # ********** QUARTOS **************
    lista_quartos = ''
    def opcoes_quartos():
        opcoes = []
        for quarto in lista_quartos:
            opcoes.append(ft.DropdownOption(quarto))
        return opcoes
    

    container_opcoes_quartos = ft.Dropdown(options=opcoes_quartos(),label = "Quartos",width=400)

    data_reserva_inicio = ft.TextField(label="Data Início Reserva",width=195)
    data_reserva_final = ft.TextField(label="Data Início Reserva",width=195)

    linha_selecao = ft.Row([data_reserva_inicio,data_reserva_final],alignment='center')

    botao_criar_reserva = ft.ElevatedButton(text="Criar reserva", bgcolor='indigo',color='white',width=200)
    botao_modificar_reserva = ft.ElevatedButton(text="Modificar reserva", bgcolor='indigo',color='white',width=200)
    botao_cancelar_reserva = ft.ElevatedButton(text="Cancelar reserva", bgcolor='indigo',color='white',width=200)

    container_botoes = ft.Row(controls=[botao_criar_reserva,botao_modificar_reserva,botao_cancelar_reserva],spacing=10, alignment='center')

    page.add(cabecalho,container_opcoes_clientes,container_opcoes_quartos,linha_selecao, container_botoes)

ft.app(target=main)