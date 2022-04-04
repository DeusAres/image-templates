import importlib
import inspect
import os
from pathlib import Path

import PySimpleGUI as sg
import funPIL as df

import imgSave
import jpgGen
import readTemplates
from resources.paths import *

def main():

    listTemplates = readTemplates.listT()

    def total(new, temp=None):

        l = [
                [
                    sg.Column([
                        [sg.Text('Template'), sg.Combo(listTemplates, default_value=temp, enable_events=True, key='template')],
                        *new,
                        [sg.Push(), sg.Button('Generate'), sg.Push()]
                    ]),
                    sg.Column([
                        [sg.Push(), sg.Frame("Preview", [[sg.Image(key='prev', s=(300,300))]]), sg.Push()],
                        [
                            sg.Input(s=(8,1), key='backgroundColor'), sg.ColorChooserButton('Color'), 
                            sg.Combo(['instagram', 'pinterest'], default_value='instagram', key='destination'), 
                            sg.Push(), sg.Input(enable_events=True, visible=False, key='SaveJPG'), 
                            sg.FileSaveAs('Save JPG', file_types=(('JPG','.jpg'),), s=(10,1))
                        ],
                        [
                            sg.Push(), sg.Input(enable_events=True, visible=False, key='SavePNG'), 
                            sg.FileSaveAs('Save PNG', file_types=(('PNG','.png'),), s=(10,1))
                        ]
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
            template = readTemplates.importT(values['template'])

            templateArgs = readTemplates.readArgs(template)

            newMiddle = readTemplates.makeLayout(templateArgs)

        
            layout = total(newMiddle, values['template'])
            window.close()
            window = sg.Window("Template generator", layout)

        if event == 'Generate':
            image = template.main(*readTemplates.correctDatas(templateArgs, values))

            prev = df.image_to_data(df.resizeToFit(image, 300)[0])
            window['prev'].Update(data=prev)


        if event == 'SavePNG' and values['SavePNG'] != '':
            imgSave.choosen(image, values['SavePNG'])
        if event == 'SaveJPG' and values['SaveJPG'] != '':
            jpg = jpgGen.main(image, values['backgroundColor'], values['destination'])
            imgSave.main(jpg, values['SaveJPG'])

    window.close()


if __name__ == '__main__':
    main()