import PySimpleGUI as sg

def tarefa_nova():
    sg.theme('Black')

    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]

    layout = [
        [sg.Frame('tarefas', layout=linha, key='container')],
        [sg.Button('nova tarefa'),sg.Button('resetar')]
    ]

    return sg.Window('Lista de Tarefas', layout=layout, finalize=True)

janela = tarefa_nova()

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'nova tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])

    elif event == 'resetar':
        janela.close()
        janela = tarefa_nova()

      