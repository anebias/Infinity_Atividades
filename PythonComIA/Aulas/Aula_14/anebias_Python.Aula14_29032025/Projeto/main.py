import flet as ft

# Função para gerar a resposta do chatbot
def resposta_chatbot(mensagem):
    respostas = {
        "oi": "Olá! Como posso ajudar?",
        "qual seu nome?": "Eu sou o ChatBot. Como posso te ajudar?",
        "tchau": "Até logo!",
    }
    # Retorna uma resposta baseada na mensagem do usuário ou uma resposta padrão
    return respostas.get(mensagem.lower().strip(), "Desculpe, não entendi sua pergunta.")

# Função que atualiza a interface com a nova mensagem
def main(page: ft.Page):
    page.title = "ChatBot"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Criação dos elementos da interface
    chat_box = ft.Column(scroll=ft.ScrollMode.AUTO)  # Caixa de chat para exibir mensagens
    text_input = ft.TextField(label="Digite sua mensagem", autofocus=True, on_submit=lambda e: enviar_mensagem(e, chat_box, text_input))

    # Função para enviar e exibir a mensagem
    def enviar_mensagem(event, chat_box, text_input):
        usuario_mensagem = text_input.value
        chat_box.controls.append(ft.Text(f"Você: {usuario_mensagem}", color=ft.colors.BLUE))
        bot_resposta = resposta_chatbot(usuario_mensagem)
        chat_box.controls.append(ft.Text(f"Bot: {bot_resposta}", color=ft.colors.GREEN))
        text_input.value = ""  # Limpar campo de texto
        text_input.focus()  # Colocar o foco de volta no campo de texto
        page.update()

    # Adiciona o layout inicial
    page.add(chat_box, text_input)

# Executar o aplicativo Flet
ft.app(target=main)