# interface gráfica

import PySimpleGUI as psg

import conv2

layout =     [
                 [psg.Text('Informe Celsius para Fahrenheit: '), psg.InputText(key='input_cel')],
                 [psg.Text('Informe Fahrenheit para Celsius: '), psg.InputText(key='input_fah')],
                 [psg.Text('Em Fahrenheit:'), psg.Text('', key='output_fah')],
                 [psg.Text('Em Celsius:'), psg.Text('', key='output_cel')],

                 [psg.Button('calcular:'), psg.Button('limpar')]
             ]
janela = psg.Window('Conversor Simples', layout)

while True:
    evento, graus = janela.read()

    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'limpar':
        janela['input_cel'].update('')
        janela['input_fah'].update('')
        janela['output_cel'].update('')
        janela['output_fah'].update('')
        janela['input_cel'].set_focus()
    elif evento == 'calcular:':
        try:
            cel = float(graus['input_cel'])
            fah = float(graus['input_fah'])
            janela['output_cel'].update(conv2.cel(cel, fah))
            janela['output_fah'].update(conv2.fah(cel, fah))
        except ValueError:
            pass