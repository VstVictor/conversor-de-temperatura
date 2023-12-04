# Conversor de Temperatura em Python

# Apresentação

print('\n\t\t\t -- Conversor de Temperatura --\n')

# Celsius para Fahrenheit
cel = float(input('Digite a temperatura em Celsius: '))
fah = 9 * cel / 5 + 32
print(f'A temperatura em Fahrenheit é: {fah}')

# Fahrenheit para Celsius
fah = float(input('Digite a temperatura em Fahrenheit: '))
cel = (fah - 32) / 9 * 5
print(f'A temperatura em Celsius é: {cel}')