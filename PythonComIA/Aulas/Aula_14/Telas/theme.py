import flet as ft

def theme():
    theme_page = ft.Theme(color_scheme=ft.ColorScheme(
        primary=ft.colors.INDIGO, #botões primários, barras navegação, elementos destaque
        secondary=ft.colors.BLUE, #botões secundários, pequenos elementos
        background=ft.colors.WHITE, #tela fundo
        surface=ft.colors.INDIGO, #cartões, caixas diálogo, listas
        on_primary=ft.colors.WHITE, #cor sobre os elementos primários
        on_secondary=ft.colors.WHITE, #cor sobre os elementos secundários
        on_background=ft.colors.INDIGO, #cor dos elementos sobre o fundo
        on_surface=ft.colors.WHITE #cor sobre os elementos de superfície
    ))
    return theme_page