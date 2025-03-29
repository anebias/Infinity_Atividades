# # ESTILIZAÇÃO COM FLET

# import flet as ft

# def main(page: ft.Page):

#     page.title = "Estilização Básica"
#     page.add(
#         ft.Text('Texto com cor personalizada', color='blue'),
#         ft.ElevatedButton('Botão com estilo', bgcolor='green', color='white')
#     )

# ft.app(target=main)

# APLICANDO CORES E FONTES
# import flet as ft

# def main(page: ft.Page):

#     page.title = "Aplicando Cores e Fontes"
#     page.add(
#         ft.Text('Texto vermelho', color='red', size=20),
#         ft.Text('Texto azul e negrito', color='blue',weight='bold', size=24),
#         ft.Text('Texto verde e itálico', color='green',italic=True, size=18),
#         ft.ElevatedButton('Botão com estilo', bgcolor='pink', color='white')
#     )

# ft.app(target=main)

# UTILIZANDO TEMAS

# Termos e Funções:
# 1. ‘primary_color’ (Cor Primária):
# Definição: A cor principal utilizada no tema, frequentemente aplicada a elementos
# importantes como botões e cabeçalhos.
# Função: Define a aparência principal do aplicativo, proporcionando um aspecto
# unificado e reconhecível.
# 2. ‘secondary_color’ (Cor Secundária):
# Definição: A cor secundária utilizada para complementar a cor primária, aplicada
# a elementos secundários.
# Função: Ajuda a criar contraste e variedade visual na interface do usuário.
# 3. ‘background_color’ (Cor de Fundo):
# Definição: A cor de fundo para o aplicativo ou componentes específicos.
# Função: Define o plano de fundo da interface, influenciando a legibilidade e o
# conforto visual.
# 4. ‘text_color’ (Cor do Texto):
# Definição: A cor aplicada ao texto.
# Função: Garante que o texto seja legível e contrastante com o plano de fundo.

# import flet as ft

# def main(page: ft.Page):

#     page.title = "Utilizando Temas"

#     theme = ft.Theme(color_scheme=ft.ColorScheme(
#         primary=ft.colors.BLUE,
#         secondary=ft.colors.GREEN,
#         background=ft.colors.WHITE,
#         surface=ft.colors.GREY,
#         on_primary=ft.colors.WHITE,
#         on_secondary=ft.colors.WHITE,
#         on_background=ft.colors.BLACK,
#         on_surface=ft.colors.BLACK
#     ))

#     page.theme = theme

#     page.add(
#         ft.Text('Texto com tema'),
#         ft.Text('Texto azul e negrito', color='blue',weight='bold', size=24),
#         ft.Text('Texto verde e itálico', color='green',italic=True, size=18),
#         ft.ElevatedButton('Botão com tema'),
#         ft.ElevatedButton('Botão com estilo', bgcolor='pink', color='white')
#     )

# ft.app(target=main)

# ESTILIZAÇÃO AVANÇADA COM CSS-LIKE:
# Estilização CSS-like:
# Flet permite definir estilos de forma semelhante ao
# CSS(Cascading Style Sheets), que é uma linguagem
# usada para descrever a apresentação de um
# documento escrito em HTML ou XML .
# Função: Facilita a aplicação e a manutenção de
# estilos complexos usando uma sintaxe familiar a
# desenvolvedores web.
# Classes de estilo:
# Podemos criar classes de estilo para reutilização.

# Termos e Funções:
# 1. ‘class’ (Classe):
# Definição: Um identificador que pode ser atribuído a um ou mais elementos para
# aplicar um conjunto de estilos.
# Função: Permite reutilizar estilos, aplicando-os a múltiplos elementos que
# compartilham a mesma classe.
# 2. ‘background-color ’ (Cor de Fundo):
# Definição: Define a cor de fundo de um elemento.
# Função: Personaliza a aparência do fundo de um componente, destacando-o ou
# alinhando-o ao tema geral.
# 3. ‘color ’ (Cor do Texto):
# Definição: Define a cor do texto dentro de um elemento.
# Função: Garante que o texto tenha uma cor apropriada e legível.
# 4. ‘font-size’ (Tamanho da Fonte):
# Definição: Define o tamanho do texto.
# Função: Ajusta a legibilidade e a hierarquia visual do texto.
# 5. ‘font-weight’ (Peso da Fonte):
# Definição: Define a espessura do texto (normal, negrito, etc.).
# Função: Destaca ou diferencia textos importantes dos restantes.

# import flet as ft

# def main(page:ft.Page):
#     page.title = "Estilização Avançada"

#     page.add(
#         ft.Text("Texto Estilizado", color=ft.colors.BLUE,weight=ft.FontWeight.BOLD),
#         ft.ElevatedButton("Botão Estilizado", bgcolor=ft.colors.ORANGE, color=ft.colors.WHITE)
#     )

# ft.app(target=main)

'''ATIVIDADE PRÁTICA 1
Personalização de Texto
Crie uma interface com três textos estilizados de
maneiras diferentes. Aplique cores, tamanhos de fonte e
pesos de fonte diferentes a cada texto.'''

# import flet as ft

# def main(page:ft.Page):
#     page.title = "Personalização de Texto"

#     page.add(
#         ft.Text('Texto personalizado nº 1', color='orange', size=16),
#         ft.Text('Texto personalizado nº 2',color='grey', size=36,weight='bold'),
#         ft.Text('Texto personalizado nº 3', color='pink', size=24, italic=True)
#     )

# ft.app(target=main)


'''ATIVIDADE PRÁTICA 2
Estilizando Botões
Crie uma interface com três botões estilizados. Aplique
diferentes cores de fundo, cores de texto e tamanhos de
fonte a cada botão.'''

# import flet as ft

# def main(page:ft.Page):
#     page.title = "Personalização de Botões"

#     page.add(
#         ft.ElevatedButton('Botão personalizado nº 1', color='black',bgcolor='grey'),
#         ft.ElevatedButton('Botão personalizado nº 2',color='grey',bgcolor='yellow'),
#         ft.ElevatedButton('Botão personalizado nº 3', color='white',bgcolor='orange')
#     )

# ft.app(target=main)

'''ATIVIDADE PRÁTICA 3
Formulário Estilizado
Crie uma interface de formulário com campos de entrada para nome e e-
mail, e um botão de envio. Estilize os campos de entrada e o botão.'''

# import flet as ft

# def main(page:ft.Page):
#     page.title = "Personalização de Formulários"

#     page.add(
#         ft.TextField(color='black',bgcolor='yellow', label = 'Nome'),
#         ft.TextField(color='black',bgcolor='yellow', label = 'Email'),
#         ft.ElevatedButton('Enviar', color='white',bgcolor='orange')
#     )

# ft.app(target=main)

'''ATIVIDADE PRÁTICA 4
Interface com Temas
Crie uma interface que aplica um tema personalizado com cores
primária, secundária, de fundo e de texto. Inclua pelo menos um texto e
um botão para visualizar o tema aplicado.'''

# import flet as ft

# def main(page:ft.Page):
#     page.title = "Personalização de Formulários"

#     theme = ft.Theme(color_scheme=ft.ColorScheme(
#         primary=ft.colors.PINK, #botões primários, barras navegação, elementos destaque
#         secondary=ft.colors.BLUE, #botões secundários, pequenos elementos
#         background=ft.colors.PINK, #tela fundo
#         surface=ft.colors.GREEN, #cartões, caixas diálogo, listas
#         on_primary=ft.colors.WHITE, #cor sobre os elementos primários
#         on_secondary=ft.colors.GREY, #cor sobre os elementos secundários
#         on_background=ft.colors.PINK, #cor dos elementos sobre o fundo
#         on_surface=ft.colors.YELLOW #cor sobre os elementos de superfície
#     ))

#     page.theme = theme

#     page.add(

#         ft.Text('Estilo personalizado'),
#         ft.TextField(label = 'Nome'),
#         ft.TextField(label = 'Email'),
#         ft.ElevatedButton('Enviar')
#     )

# ft.app(target=main)