import PySimpleGUI as sg
import batch, manual

layout = [
    [sg.Button('Manual', s=(10,1)), sg.Button('Batch', s=(10,1))]
]

window = sg.Window('Image templates', layout)

while True:
    event, values = window.read()

    if event or event == sg.WINDOW_CLOSED:
        break

window.close()

if event == 'Manual':
    manual.main()

if event == 'Batch':
    batch.main()