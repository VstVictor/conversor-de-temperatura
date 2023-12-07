# conversor de temperatura em python

# apresentação

print('\n\t\t\t -- Conversor de Temperatura --\n')

opcao = int(input('Escolha a opção:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\nOpção: '))

if opcao == 1:
    cel = float(input('Digite a temperatura em Celsius: '))
    fah = 9 * cel / 5 + 32
    print(f'A temperatura em Fahrenheit é: {fah}')
elif opcao == 2:
    fah = float(input('Digite a temperatura em Fahrenheit: '))
    cel = (fah - 32) / 9 * 5
    print(f'A temperatura em Celsius é: {cel}')
else:
    print('Opção inválida. Por favor, escolha 1 ou 2.')
