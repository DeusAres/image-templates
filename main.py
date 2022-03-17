import PySimpleGUI as sg
import os
import importlib
from pathlib import Path

listTemplates = os.listdir(Path(__file__).parents[0] / 'templates')

layout = [
    [sg.Text('Template'), sg.Listbox(listTemplates, key='template')]
]

window = sg.Window("Template generator", layout)

while True:
    event, values = window.read()

    if sg.WINDOW_CLOSED:
        break

#template = importlib.import(f'template.{values['template']}')
