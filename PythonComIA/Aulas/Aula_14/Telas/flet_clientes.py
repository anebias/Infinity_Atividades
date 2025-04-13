'''Gerenciamento de clientes:
Inclua uma tela para visualizar, adicionar e editar
informações dos clientes.'''

import flet as ft
from class_gerenciadorReservas import GerenciadorReservas
from testes import testes

gerenciador = GerenciadorReservas()
testes(gerenciador)

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
        on_primary=ft.colors.BLACK, #cor sobre os elementos primários
        on_secondary=ft.colors.BLACK, #cor sobre os elementos secundários
        on_background=ft.colors.INDIGO, #cor dos elementos sobre o fundo
        on_surface=ft.colors.BLACK #cor sobre os elementos de superfície
    ))

    cabecalho = ft.Text("GESTÃO DE CLIENTES", size=36, color="indigo")

    subtitulo = ft.Text("LISTA DE CLIENTES", size=24, color="indigo", visible=False)

    # FUNÇÕES DA PÁGINA
    def opcoes_clientes():
        opcoes = []
        for cliente in lista_clientes:
            opcoes.append(ft.DropdownOption(cliente))
        return opcoes


    def listar_clientes(e):
        subtitulo.visible = True
        container_opcoes_clientes.visible = True
        container_botoes_1.visible = False
        container_botoes_2.visible = True
        page.update()

    def editar_cliente(e):
        # APRENDER COMO RECUPERAR OS DADOSDO CLIENTE SELECIONADOS PARA PREENCHIMENTO DOS CAMPOS
        subtitulo.value = "Editar Dados do Cliente"
        container_opcoes_clientes.visible = False
        linha_captura_dados_cliente.visible = True
        linha_captura_dados_cliente.disabled = False
        linha_visualizacao_dados_cliente.visible = True
        linha_visualizacao_dados_cliente.disabled = True
        container_botoes_1.visible = False
        botao_consultar_cliente.visible = False
        botao_editar_cliente.visible = True
        page.update()

    def consultar_cliente(e):
        # APRENDER COMO RECUPERAR OS DADOSDO CLIENTE SELECIONADOS PARA PREENCHIMENTO DOS CAMPOS
        subtitulo.value = "Dados do Cliente"
        container_opcoes_clientes.visible = False
        linha_captura_dados_cliente.visible = True
        linha_captura_dados_cliente.disabled = True
        container_botoes_1.visible = False
        botao_consultar_cliente.visible = False
        botao_editar_cliente.visible = True
        page.update()

    def adicionar_cliente(e):
        subtitulo.value = "Adicionar Cliente"
        subtitulo.visible = True
        botao_adicionar_cliente.visible = True
        botao_listar_clientes.visible = False
        container_botoes_2.visible = False
        linha_captura_dados_cliente.visible = True
        page.update()

    def voltar_home(e):
        # ESTUDAR COMO IR PARA ARQUIVO MAIN.PY
        pass

    # DADOS CADASTRO CLIENTE
    nome = ft.TextField(label="Nome")
    telefone = ft.TextField(label="Telefone")
    email = ft.TextField(label="Email")
    __id = '123'

    linha_captura_dados_cliente = ft.Row([nome, telefone, email],alignment='center', visible=False)

    linha_visualizacao_dados_cliente = ft.Row([nome, telefone, email],alignment='center', visible=False)

    # BOTOES
    botao_listar_clientes = ft.ElevatedButton(text="Listar Clientes", bgcolor='indigo',color='white',width=200, on_click=listar_clientes)

    botao_editar_cliente = ft.ElevatedButton(text="Editar Cliente", bgcolor='indigo',color='white',width=200, on_click=editar_cliente)

    botao_adicionar_cliente = ft.ElevatedButton(text="Adicionar Cliente", bgcolor='indigo',color='white',width=200, on_click=adicionar_cliente)
    
    botao_consultar_cliente = ft.ElevatedButton(text="Consultar Cliente", bgcolor='indigo',color='white',width=200, on_click=consultar_cliente)

    botao_home = ft.ElevatedButton(text="Página Inicial", bgcolor='indigo',color='white',width=200, on_click=voltar_home, visible=True)

    container_botoes_1 = ft.Row(controls=[botao_listar_clientes, botao_adicionar_cliente],spacing=10, alignment='center')

    container_botoes_2 = ft.Row(controls=[botao_consultar_cliente, botao_editar_cliente],spacing=10, alignment='center', visible=False)

    # linha_divisoria = ft.Divider(color=ft.colors.GREY, thickness=2, height=20)
    lista_clientes = gerenciador.listar_clientes()
   
    container_opcoes_clientes = ft.Dropdown(options=opcoes_clientes(),label = "Clientes",width=400, visible=False)

    page.add(cabecalho, subtitulo,container_opcoes_clientes, linha_visualizacao_dados_cliente,  linha_captura_dados_cliente , container_botoes_1, container_botoes_2, botao_home )

ft.app(target=main)