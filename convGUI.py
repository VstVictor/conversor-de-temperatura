import PySimpleGUI as sg
import conv2


layout = [
    [sg.Text('Escolha a conversão:')],
    [sg.Radio('Celsius para Fahrenheit', 'RADIO1', default=True, key='cel_to_fah'),
     sg.Radio('Fahrenheit para Celsius', 'RADIO1', key='fah_to_cel')],
    [sg.Text('Informe a temperatura:'), sg.InputText(key='input_temp')],
    [sg.Text('Resultado:'), sg.Text('', key='output')],
    [sg.Button('Calcular'), sg.Button('Limpar'), sg.Button('Sair', button_color=('white', 'red'))]
]

window = sg.Window('Conversor Simples', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Limpar':
        window['input_temp'].update('')
        window['output'].update('')
    elif event == 'Calcular':
        try:
            temp = float(values['input_temp'])
            resultado = ''

            if values['cel_to_fah']:
                resultado = conv2.cel(temp)
            elif values['fah_to_cel']:
                resultado = conv2.fah(temp)

            window['output'].update(resultado)
        except ValueError:
            sg.popup_error('Por favor, insira uma temperatura válida.')

window.close()
