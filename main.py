import importlib
import inspect
import os
from pathlib import Path

import PySimpleGUI as sg
from funPIL import df

import imgSave
from resources.paths import *

listTemplates = os.listdir(Path(__file__).parents[0] / 'templates')
listTemplates = [str(Path(each).stem) for each in listTemplates if each not in ['__pycache__', '__init__.py']]

def total(new, temp=None):

    l = [
            [
                sg.Column([
                    [sg.Text('Template'), sg.Combo(listTemplates, default_value=temp, enable_events=True, key='template')],
                    *new,
                    [sg.Push(), sg.Button('Generate'), sg.Push()]
                ]),
                sg.Column([
                    [sg.Frame("Preview", [[sg.Image(key='prev', s=(300,300))]])],
                    [sg.Push(), sg.Button('Save')]
                ])
            ]
    ]

    return l

layout = ''

window = sg.Window("Template generator", total([]))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'template':
        template = importlib.import_module(f"templates.{values['template']}")
        #args = template.main.__code__.co_varnames
        datas = inspect.getfullargspec(template.main)

        templateArgs = {}
        for i in range(len(datas.args)):
            templateArgs[datas.args[i]] = {
                "default" : datas.defaults[i],
                "type" : datas.annotations[datas.args[i]]
            }

        newMiddle = []

        def makeLine(text, newElement, newMiddle):
            if type(newElement) == list:
                newMiddle.append([sg.Text(text.capitalize().replace('_', ' '), s = (20,1)), sg.Push(), *newElement])
            else:
                newMiddle.append([sg.Text(text.capitalize().replace('_', ' '), s = (20,1)), sg.Push(), newElement])
            return newMiddle

        del layout

        for keys in templateArgs.keys():
            def sendToMake(element):
                if element == sg.ColorChooserButton:
                    return makeLine(keys, [sg.Input(templateArgs[keys]['default'], s=(20,1), key=keys,), element('Choose', s=(10, 1))], newMiddle)
                elif element == sg.Multiline:
                    return makeLine(keys, element(templateArgs[keys]['default'], s=(33-2, 2), key=keys), newMiddle)
                else:
                    return makeLine(keys, element(templateArgs[keys]['default'], s=(33, 2), key=keys), newMiddle)

            if 'color' in keys:
                newMiddle = sendToMake(sg.ColorChooserButton)
            elif templateArgs[keys]['type'] == list[str]:
                newMiddle = sendToMake(sg.Multiline)
            elif templateArgs[keys]['type'] is int or templateArgs[keys]['type'] is str:
                newMiddle = sendToMake(sg.Input)
            elif templateArgs[keys]['type'] is bool:
                newMiddle = sendToMake(sg.Checkbox)

    
        layout = total(newMiddle, values['template'])
        window.close()
        window = sg.Window("Template generator", layout)

    if event == 'Generate':
        datas = []
        for each in templateArgs.keys():
            if templateArgs[each]['type'] is int:
                datas.append(int(values[each]))
            else:
                datas.append(values[each])

            
        image = template.main(*datas)
        prev = df.image_to_data(df.resizeToFit(image, 300)[0])
        window['prev'].Update(data=prev)


    if event == 'Save':
        imgSave.main(image, values['template'], values['message'], 'PNG', ROOT)

        

window.close()


