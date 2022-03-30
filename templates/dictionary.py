from funPIL import df
from resources.paths import *

def main(W:int=2000, H:int=3000, 
    word:str='gioia', 
    pronounce:str='/giò·ia/', 
    definitions:list[str]=[
        "Stato o motivo di viva, completa, incontenibile soddisfazione: una g. piena; grida, lacrime di g.; quella ragazza è la sua g.",
        "Felicità, diletto: Gioia promette e manda pianto Amore (Foscolo); motivo di gaudio, di letizia o di soddisfazione e di compiacimento: le g. della famiglia; anche iron. : che g.!, a proposito di una situazione particolarmente noiosa o seccante."
    ],
    text_color:str='#000000'):


    prop = lambda x : int(min(W, H) * x)
    CB, CD = df.backgroundPNG(W,H)
    fontPath = FONTS / 'timesNewRoman.ttf'

    # WORD 
    size = prop(0.15)
    font = df.fontDefiner(fontPath, size)
    x, y = [prop(0.05)]*2
    df.drawText(x, y, CD, word, text_color, font, anchor='la')

    # FROM WORD TO PRONOUNCE
    y += df.getSize(word, font)[1] + font.getmetrics()[1] + prop(0.07)
    #PRONOUNCE

    size = prop(0.073)
    font = df.fontDefiner(fontPath, size)

    hsl = [*df.rgbToHsl(*df.hexToRgb(text_color))]
    hsl[2] = hsl[2] + 20 if hsl[2] < 50 else hsl[2] - 20
    pronColor = df.hslToRgb(*hsl)

    df.drawText(x, y, CD, pronounce, pronColor, font)

    #FROM PRONOUNCE TO DEFINITION
    y += df.getSize(pronounce, font)[1] + prop(0.07)
    #DEFINITION(S)
    size = prop(0.05)
    font = df.fontDefiner(fontPath, size)
    i = 1
    x1 = prop(0.15)
    x1plus = df.getSize('5.', font)[0]
    x2 = W-prop(0.15)
    

    if type(definitions) == str:
        definitions = definitions.split('\n')
    for each in definitions:
        df.drawText(x, y, CD, f'{str(i)}.', text_color, font, anchor = 'la')
        each = df.wrapToCanvas(each.replace('( ', '(').replace(' )', ')'), x2-x1, font)
        
        df.drawMultiline(x1, y, CD, each, font, text_color, 'la', spacing=prop(0.03), align='left')
        y += df.getSizeMultiline(each, font, prop(0.03))[1] + prop(0.05)
        i += 1
        #df.drawMultiLine(x1, x2,  y, each, font, text_color, 'left', None, CD)
        #y += df.getMultipleSize(each, font)[3]
    

        
    return CB
