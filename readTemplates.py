import os
from pathlib import Path
import importlib
import PySimpleGUI as sg
import inspect


def listT():
    listTemplates = os.listdir(Path(__file__).parents[0] / 'templates')
    listTemplates = [str(Path(each).stem) for each in listTemplates if each not in ['__pycache__', '__init__.py']]
    return listTemplates

def importT(templateName):
    template = importlib.import_module(f"templates.{templateName}")
    return template

def readArgs(template):
    """
    Read arguments name, data annotation and defaults from main function
    """
    datas = inspect.getfullargspec(template.main)

    templateArgs = {}
    for i in range(len(datas.args)):
        templateArgs[datas.args[i]] = {
            "default" : datas.defaults[i],
            "type" : datas.annotations[datas.args[i]]
        }

    return templateArgs

def makeLayout(templateArgs):
    """
    Make a new portion of layout for PySimpleGUI
    """
    newMiddle = []

    def makeLine(text, newElement, newMiddle):
        if type(newElement) == list:
            newMiddle.append([sg.Text(text.capitalize().replace('_', ' '), s = (20,1)), sg.Push(), *newElement])
        else:
            newMiddle.append([sg.Text(text.capitalize().replace('_', ' '), s = (20,1)), sg.Push(), newElement])
        return newMiddle

    for keys in templateArgs.keys():
        def sendToMake(element):
            if element == sg.ColorChooserButton:
                return makeLine(keys, [sg.Input(templateArgs[keys]['default'], s=(20,1), key=keys,), element('Choose', s=(10, 1))], newMiddle)
            elif element == sg.Checkbox:
                return makeLine(keys, element(keys, templateArgs[keys]['default'], key=keys), newMiddle)
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

    return newMiddle

def correctDatas(templateArgs, values):
    """
    PySimpleGUI/tkinter manages datas in a different way
    They needs correction
    Integrated in this module for readability
    """
    datas = []
    for each in templateArgs.keys():
        if templateArgs[each]['type'] is int:
            datas.append(int(values[each]))
        elif templateArgs[each]['type'] is str:
            datas.append(values[each].strip('\n').strip(' '))
        else:
            datas.append(values[each])

    return datas
