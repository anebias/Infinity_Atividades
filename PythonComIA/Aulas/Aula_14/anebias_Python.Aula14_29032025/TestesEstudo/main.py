import flet as ft

def main(page: ft.Page):
    ola = ft.Text(value="Olá mundo!!", size=30, color="blue",bgcolor="yellow")
    page.controls.append(ola)
    page.update()

ft.app(target=main)

