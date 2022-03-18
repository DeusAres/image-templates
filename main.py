import PySimpleGUI as sg
import os
import importlib
from pathlib import Path
import inspect
import templates

listTemplates = os.listdir(Path(__file__).parents[0] / 'templates')
listTemplates = [str(Path(each).stem) for each in listTemplates if each not in ['__pycache__', '__init__.py']]

startLayout = lambda : [
    [sg.Text('Template'), sg.Combo(listTemplates, enable_events=True, key='template')]
]

endLayout = lambda : [
    [sg.Push(), sg.Button('Generate'), sg.Push()]
]


middleLayout = ''

window = sg.Window("Template generator", startLayout())

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    print(event)
    if event == 'template':
        template = importlib.import_module(f"templates.{values['template']}")
        #args = template.main.__code__.co_varnames
        args = inspect.getfullargspec(template.main)[0]
        del middleLayout
        middleLayout = [startLayout()] + [[sg.Text(each.capitalize()), sg.Push(), sg.Multiline("", key=each),] for each in args] + [endLayout()]
        window.close()
        window = sg.Window("Template generator", middleLayout)

    if event == 'Generate':
        image = template.main(*[values[each] for each in args])
        image.show()
        

window.close()


