# conversor de temperatura em python

# apresentação

print('\n\t\t\t -- Conversor de Temperatura --\n')

# celsius para fahrenheit
cel = float(input('Digite a temperatura em Celsius: '))
fah = 9 * cel / 5 + 32
print(f'A temperatura em Fahrenheit é: {fah}')

# fahrenheit para celsius
fah = float(input('Digite a temperatura em Fahrenheit: '))
cel = (fah - 32) / 9 * 5
print(f'A temperatura em Celsius é: {cel}')