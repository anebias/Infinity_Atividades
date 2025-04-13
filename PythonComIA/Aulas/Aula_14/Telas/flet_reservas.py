'''Formulário de reserva:
Permita que o usuário escolha o cliente, o quarto e
as datas desejadas para criar uma nova reserva.'''

import flet as ft
from class_gerenciadorReservas import GerenciadorReservas
from testes import testes

gerenciador = GerenciadorReservas()
testes(gerenciador)

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
        on_primary=ft.colors.BLACK, #cor sobre os elementos primários
        on_secondary=ft.colors.BLACK, #cor sobre os elementos secundários
        on_background=ft.colors.INDIGO, #cor dos elementos sobre o fundo
        on_surface=ft.colors.BLACK #cor sobre os elementos de superfície
    ))

    cabecalho = ft.Text("GESTÃO DE RESERVAS", size=36, color="indigo")

    # ********** CLIENTES **************
    lista_clientes = gerenciador.listar_clientes()
    def opcoes_clientes():
        opcoes = []
        for cliente in lista_clientes:
            opcoes.append(ft.DropdownOption(cliente))
        return opcoes

    # ********** QUARTOS **************
    lista_quartos = gerenciador.listar_quartos_disponibilidades()
    def opcoes_quartos():
        opcoes = []
        for quarto in lista_quartos:
            opcoes.append(ft.DropdownOption(quarto))
        return opcoes
 
    def lista_das_reservas():
        lista_reservas_cadastradas = gerenciador.listar_reservas()
        opcoes = []
        if lista_reservas_cadastradas:
            for reserva in lista_reservas_cadastradas:
                opcoes.append(ft.DropdownOption(reserva))
            return opcoes

    def listar_reservas(e):
        container_reservas.visible = True
        container_opcoes_quartos.visible = False
        container_opcoes_clientes.visible = False 
        botao_listar_reservas.visible = False
        botao_criar_reserva.visible = False
        botao_cancelar_reserva.visible = True
        botao_modificar_reserva.visible = True
        page.update()

    def cancelar_reserva(e):
        container_opcoes_quartos.visible= False
        container_opcoes_clientes.visible = False
        container_reservas.disabled = True
        botao_modificar_reserva.visible = False
        linha_selecao.visible = False
        page.update()

    def criar_reserva(e):
        linha_selecao.visible = True
        container_opcoes_quartos.visible = True
        container_opcoes_clientes.visible = True
        botao_listar_reservas.visible = False
        page.update()

    def alterar_reserva(e):
        container_reservas.disabled = True
        container_opcoes_quartos.visible = True
        container_opcoes_clientes.visible = False
        botao_cancelar_reserva.visible = False
        linha_selecao.visible = True
        page.update()
    
    def voltar_home(e):
        # ESTUDAR COMO IR PARA ARQUIVO MAIN.PY
        pass

    # LISTA CLIENTES
    container_opcoes_clientes = ft.Dropdown(options=opcoes_clientes(),label = "Clientes",width=400, visible=False)

    # LISTA QUARTOS
    container_opcoes_quartos = ft.Dropdown(options=opcoes_quartos(),label = "Quartos",width=400, visible=False)

    # LISTA RESERVAS
    container_reservas = ft.Dropdown(options=lista_das_reservas(),label = "Reservas",width=600, visible=False)

    # DATAS DA RESERVA
    data_reserva_inicio = ft.TextField(label="Data Início Reserva",width=195)
    data_reserva_final = ft.TextField(label="Data Início Reserva",width=195)
    linha_selecao = ft.Row([data_reserva_inicio,data_reserva_final],alignment='center', visible=False)

    # BOTOES
    botao_listar_reservas = ft.ElevatedButton(text="Listar reservas", bgcolor='indigo',color='white',width=200, on_click=listar_reservas)
    botao_criar_reserva = ft.ElevatedButton(text="Criar reserva", bgcolor='indigo',color='white',width=200, on_click=criar_reserva)
    botao_modificar_reserva = ft.ElevatedButton(text="Modificar reserva", bgcolor='indigo',color='white',width=200, on_click=alterar_reserva, visible=False)
    botao_cancelar_reserva = ft.ElevatedButton(text="Cancelar reserva", bgcolor='indigo',color='white',width=200, on_click=cancelar_reserva, visible=False)

    container_botoes_1 = ft.Row(controls=[botao_criar_reserva,botao_listar_reservas],spacing=10, alignment='center')

    container_botoes_2 = ft.Row(controls=[botao_modificar_reserva,botao_cancelar_reserva],spacing=10, alignment='center')

    botao_home = ft.ElevatedButton(text="Página Inicial", bgcolor='indigo',color='white',width=200, on_click=voltar_home, visible=True)

    page.add(cabecalho,container_reservas,container_opcoes_clientes,container_opcoes_quartos, linha_selecao, container_botoes_1, container_botoes_2,botao_home)

ft.app(target=main)