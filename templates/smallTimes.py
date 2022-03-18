from funPIL import df
from resources.paths import * 

def main(message):
    W, H = 2000, 2000
    fontPath = FONTS / "Times New Roman.ttf"

    textB, textD = df.backgroundPNG(W, H)

    size = df.fitSize(fontPath, message, W)
    font = df.fontDefiner(fontPath, size)
    df.drawText(W//2, H//2, textD, message, 'white', font, 'mm')

    return textB