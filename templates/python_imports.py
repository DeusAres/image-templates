import funPIL as df
from resources.paths import *

def main(W: int=4800, 
            from_text: list[str]="multiprocessing",
            import_text: list[str]="Threading",
            as_text: list[str]="T",
            builtin_color: list[str]='#4ec9b0',
            library_color: list[str]='#c586c0',
            background_color: list[str]='#292929') -> df.Image:


    fontPath = str(FONTS / "Consolas.ttf")

    if from_text not in ['', None]:
        message = "from " + from_text + " import " + import_text
    else:
        message = "import " + import_text
    
    if as_text not in ['', None]:
        message += " as " + as_text



    # I know, 1 can be changed to give more height to rectangle
    hRectSpace = lambda y : y+int(y*0.5) 
    wRectSpace = W*0.1

    font = df.fitFontInCanvas(fontPath, message, [W - wRectSpace, W])
    #font = df.fontDefiner(fontPath, 31)
    print(font.size)
    
    
    space, y = df.getSize('M', font)
    ascDesc = font.getmetrics()
    y += ascDesc[0] - ascDesc[1]

    H = hRectSpace(y)

    canvasB, canvasD = df.backgroundPNG(W, H, background_color)

    y = H//2

    df.roundCorners(canvasB, H*0.2)
    
    x = df.getSize(message, font)[0]
    print(x)
    x = W//2 - x//2
    for text in message.split(' '):
        if text in ['from', 'import', 'as']:
            fontColor = builtin_color
        else:
            fontColor = library_color
        df.drawText(x, y, canvasD, text, fontColor, font, 'lm')
        x += df.getSize(text, font)[0] + space

    return canvasB