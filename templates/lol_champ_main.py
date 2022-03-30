from funPIL import df
from resources.paths import *

def main(W: int=1000, H: int=1000, champion: str="Yasuo"):
    message = [champion.upper(), "MAIN"]

    prop = lambda x : int(min(W, H) * x)

    textB, textD = df.backgroundPNG(W, H)
    canvasB, canvasD = df.backgroundPNG(W, H)
    fontPath = FONTS / 'arialBoldItalic.ttf'
    size = prop(0.125)
    #df.fitSize(fontPath, message[0], W-100)
    font = df.fontDefiner(fontPath, size)

    df.drawMultiLine(0, W, 0, message, font, "white", draw=textD)

    # w, _, h, _ = df.getMultipleSize(message, font)
    # w += 100
    # h += 200
    
    w, h = 2000, 600
    cw, ch = W//2, H//2

    canvasD.rectangle([cw-w//2, ch-h//2, cw+w//2, ch+h//2], fill='red')
    textB, textD = df.cropToRealSize(textB)
    canvasB = df.pasteItem(canvasB, textB, *df.centerItem(canvasB, textB))

    return canvasB


    

