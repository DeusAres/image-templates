from funPIL import df
from resources.paths import *

def main(champion):
    W, H = 2000, 2000
    message = [champion.upper(), "MAIN"]
    textB, textD = df.backgroundPNG(W, H)
    canvasB, canvasD = df.backgroundPNG(W, H)
    fontPath = FONTS / 'Arial Bold Italic.ttf'
    size = 100//250*min(W, H)
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


    

