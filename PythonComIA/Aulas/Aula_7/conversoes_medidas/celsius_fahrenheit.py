def converter_celsius():
    temperatura_fahrenheit = input('Informe a temperatura em Fahrenheit: ')
    
    for _ in range(3):
        if not temperatura_fahrenheit.replace('.','').isnumeric():
            temperatura_fahrenheit = input('Inválido. Informe a temperatura em Fahrenheit: ')
        else:  
            temperatura_celsius = ((float(temperatura_fahrenheit) - 32)/9)*5
            return print(f'A temperatura de {temperatura_fahrenheit} graus Fahrenheit equivale à temperatura de {temperatura_celsius} graus Celsius')
    