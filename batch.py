import PySimpleGUI as sg
import readTemplates
import imgSave
import jpgGen

def main():
    templates = readTemplates.listT()

    def layout(new, temp=None): 
        return [
        [   
            sg.Frame('Template', [
                [sg.Text('Template'), sg.Combo(templates, default_value=temp, enable_events=True, key='template')],
                [*new],
            ])
        ],
        [
            sg.Frame('File', [
                [sg.Text('File'), sg.Input(key='file'), sg.FileBrowse('Browse')],
                [sg.Text('Terminator for each design', s=(20,1)), sg.Input(s=(3,1), key='terminator')],
                [sg.Text('Variable splitter for each design', s=(20,1)), sg.Input(s=(3,1), key='splitter')]
            ])
        ],
        [   
            sg.Frame('PNG', [
                [sg.Checkbox('PNG', key='PNG')], 
                [sg.Text('Destination'), sg.Input(key='pngFolder'), sg.FolderBrowse('Browse')],
                [sg.Text('Save name'), sg.Input(key='saveName1')]
            ])
        ],
        [
            sg.Frame('JPG', [
                [sg.Checkbox('JPG', key='JPG')],
                [sg.Text('Destination'), sg.Input(key='jpgFolder'), sg.FolderBrowse('Browse')],
                [sg.Text('Save name'), sg.Input(key='saveName2')],
                [sg.Text('Color'), sg.Input(size=(7,1), key='backgroundColor'), sg.ColorChooserButton('Color')],
                [sg.Text('Social'), sg.Combo(['instagram', 'pinterest'], key='destination')]
            ])
        ],
        [sg.Button('Generate')]
    ]

    window = sg.Window('Batch image templates', layout([]))

    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED:
            break

        if event == 'template':
            template = readTemplates.importT(values['template'])
            templateArgs = readTemplates.readArgs(template)

            lenTemplateArgs = len(list(templateArgs.keys()))

            l = []
            for key, i in zip(list(templateArgs.keys()), range(1, lenTemplateArgs+1)):
                l.append([
                        sg.Text(key, s=(30,1)), 
                        sg.Combo(['text', 'default', 'fixed'], default_value='default', key=f'which{i}'), 
                        sg.Input(key=f'fixed{i}')
                    ])

            l = [sg.Frame("Datas", l)]

            window.close()
            window = sg.Window("Batch image templates", layout(l, values['template']))

        if event == 'Generate':
            with open(values['file'], 'r', encoding='utf-8') as f:
                quotes = "".join(f.readlines())

            if values['terminator'] == '' : values['terminator'] = None
            elif values ['terminator'] == '\\n' : values['terminator'] = '\n'
            quotes = quotes.split(values['terminator'])
            if values['splitter'] == '' : quotes = [[each] for each in quotes]
            else:
                quotes = [quotes[i].strip('\n').split(values['splitter']) for i in range(len(quotes))]

            quotes = list(filter(lambda x : x != [''], quotes))

            whichValues = [values[f'which{i}'] for i in range(1, lenTemplateArgs+1)]
            fixedValues = [values[f'fixed{i}'] for i in range(1, lenTemplateArgs+1)]
            defaultValues = [templateArgs[key]['default'] for key in templateArgs.keys()]

            datasTemplate = [0]*lenTemplateArgs
            for i in range(lenTemplateArgs):
                if whichValues[i] == 'fixed':
                    datasTemplate[i] = fixedValues[i]
                elif whichValues[i] == 'default':
                    datasTemplate[i] = defaultValues[i]
                elif whichValues[i] == 'text':
                    datasTemplate[i] = None

            newQuotes = []

            for i in range(len(quotes)):
                dt2 = datasTemplate.copy()
                k = 0
                for j in range(len(datasTemplate)):
                    if dt2[j] is None:
                        dt2[j] = quotes[i][k]
                        k+=1
                
                dt3 = {}
                for a, b in zip(templateArgs.keys(), dt2):
                    dt3[a] = b
                dt3 = readTemplates.correctDatas(templateArgs, dt3)
                newQuotes.append(dt3)
                
            for each in newQuotes:
                image = template.main(*each)
                if values['PNG']:
                    imgSave.main(image, values['template'], values['saveName1'], values['pngFolder'].strip('"'), '.png')
                if values['JPG']:
                    jpg = jpgGen.main(image, values['backgroundColor'], values['destination'])
                    imgSave.main(jpg, values['template'], values['saveName1'], values['jpgFolder'].strip('"'), '.jpg')

    window.close()

if __name__ == '__main__':
    main()