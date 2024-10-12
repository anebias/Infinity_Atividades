numero = float(input('Informe um número: '))

if numero == 0:
    print(f'O número{numero: .0f} é zero.')
elif numero > 0:
    print(f'O número{numero: .2f} é positivo.')
else:
    print(f'O número{numero: .2f} é negativo.')