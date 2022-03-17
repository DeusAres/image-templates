import PySimpleGUI as sg
import os

layout = [
    [sg.Text('Template'), sg.Listbox([], key='template')]
]

window = sg.Window("Template generator", layout)
templates = os.listdir(__file__+'/templates')

