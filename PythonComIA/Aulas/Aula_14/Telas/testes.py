# MASSA DE TESTES GERADA PELO CHAT GPT

def testes(gerenciador):
    from datetime import date, timedelta
    import random

    # CLIENTES FICTICIOS
    clientes = [
        gerenciador.cadastrar_cliente("Ana Paula", "1199887766", "ana.paula@email.com"),
        gerenciador.cadastrar_cliente("Bruno Silva", "2199123456", "bruno.silva@email.com"),
        gerenciador.cadastrar_cliente("Carlos Mendes", "3199988776", "carlos.m@email.com"),
        gerenciador.cadastrar_cliente("Daniela Lima", "1199567432", "daniela.lima@email.com"),
        gerenciador.cadastrar_cliente("Eduardo Gonçalves", "4199123123", "eduardo.g@email.com"),
        gerenciador.cadastrar_cliente("Fernanda Rocha", "5199988112", "fernanda.rocha@email.com"),
        gerenciador.cadastrar_cliente("Gabriel Souza", "6199678910", "gabriel.souza@email.com"),
        gerenciador.cadastrar_cliente("Helena Torres", "7199988776", "helena.torres@email.com"),
        gerenciador.cadastrar_cliente("Igor Almeida", "8199123456", "igor.almeida@email.com"),
        gerenciador.cadastrar_cliente("Juliana Castro", "9199678943", "juliana.castro@email.com"),
    ]

    # QUARTOS FICTICIOS
    quartos = [
        gerenciador.cadastrar_quarto(101, "Solteiro", 120.00),
        gerenciador.cadastrar_quarto(102, "Solteiro", 120.00),
        gerenciador.cadastrar_quarto(201, "Casal", 180.00),
        gerenciador.cadastrar_quarto(202, "Casal", 180.00),
        gerenciador.cadastrar_quarto(301, "Luxo", 250.00),
        gerenciador.cadastrar_quarto(302, "Luxo", 250.00),
        gerenciador.cadastrar_quarto(401, "Suíte Master", 400.00),
        gerenciador.cadastrar_quarto(402, "Suíte Master", 400.00),
        gerenciador.cadastrar_quarto(103, "Solteiro", 120.00),
        gerenciador.cadastrar_quarto(203, "Casal", 180.00),
    ]

    # RESERVAS FICTICIAS
    for i in range(len(clientes)):
        checkin = date.today() + timedelta(days=random.randint(0, 5))
        checkout = checkin + timedelta(days=random.randint(1, 5))
        gerenciador.criar_reserva(clientes[i], quartos[i], checkin, checkout)
    
    print("Testes concluídos.")



# # TESTES QUE REALIZEI NO TERMINAL
# gerenciador = GerenciadorReservas()

# hospede_1 = gerenciador.cadastrar_cliente("Ana","3198877-1645","ana@gmail.com")
# hospede_2 = gerenciador.cadastrar_cliente("Jose","6198555-1254","jose@outlook.com")
# hospede_3 = gerenciador.cadastrar_cliente("Viviane","5198526-1475","vivi@hotmail.com")

# quarto_1 = gerenciador.cadastrar_quarto(401,"single",269.00)
# quarto_2 = gerenciador.cadastrar_quarto(402,"double",469.00)
# quarto_3 = gerenciador.cadastrar_quarto(403,"suite",669.00)

# reserva_1 = gerenciador.criar_reserva(hospede_1,quarto_1,"2025-02-28","2025-03-04")
# reserva_2 = gerenciador.criar_reserva(hospede_2,quarto_2,"2025-03-03","2025-03-13")
# reserva_3 = gerenciador.criar_reserva(hospede_3,quarto_3,"2025-03-28","2025-04-04")

# print(gerenciador.verificar_disponibilidade_quarto(quarto_1))
# print(gerenciador.verificar_disponibilidade_quarto(quarto_2))
# print(gerenciador.verificar_disponibilidade_quarto(quarto_3))

# gerenciador.listar_reservas()

# gerenciador.modificar_reserva(reserva_1,quarto_2,"2025-01-01","2025-01-15")
# gerenciador.modificar_reserva(reserva_2,quarto_1,"2025-10-01","2025-10-15")
# gerenciador.modificar_reserva(reserva_3,quarto_3,"2025-10-01","2025-10-11")

# gerenciador.listar_reservas()

# print(gerenciador.verificar_disponibilidade_quarto(quarto_1))
# print(gerenciador.verificar_disponibilidade_quarto(quarto_2))
# print(gerenciador.verificar_disponibilidade_quarto(quarto_3))

# gerenciador.cancelar_reserva(reserva_1)
# gerenciador.cancelar_reserva(reserva_2)
# gerenciador.cancelar_reserva(reserva_3)

# gerenciador.listar_reservas()

# print(gerenciador.consultar_cliente(hospede_1))
# print(gerenciador.consultar_cliente(hospede_2))
# print(gerenciador.consultar_cliente(hospede_3))