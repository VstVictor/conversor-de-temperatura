# conversor de temperatura em python

# apresentação

while True:
    print('\n\t\t\t -- Conversor de Temperatura --\n')

    opcao = int(input('Escolha a opção:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n3. Sair\nOpção: '))

    if opcao == 1:
        cel = float(input('Digite a temperatura em Celsius: '))
        fah = 9 * cel / 5 + 32
        print(f'A temperatura em Fahrenheit é: {fah}')
    elif opcao == 2:
        fah = float(input('Digite a temperatura em Fahrenheit: '))
        cel = (fah - 32) / 9 * 5
        print(f'A temperatura em Celsius é: {cel}')
    elif opcao == 3:
        print('Até depois!')
        break
    else:
        print('Opção inválida. Por favor, escolha 1, 2 ou 3.')

    resposta = input('Deseja realizar outra conversão? (s/n): ').lower()
    if resposta != 's':
        break
