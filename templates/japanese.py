import textwrap
from funPIL import df
from resources.paths import * 

def main(W: int=1000, H: int=1000, japanese: str="起死回生", english: str='Wake from death and return to life'):
    
    prop = lambda x : int(min(W, H) * x)
    fontPath = str(FONTS / "zen antique.ttf")

    textB, textD = df.backgroundPNG(W, H)

    size = df.fitSize(fontPath, japanese, W)
    font = df.fontDefiner(fontPath, size)
    df.drawText(W//2, 0, textD, japanese, 'white', font, 'mt')
    _, h = df.getSize(japanese, font)
    h += prop(0.03)

    english = f'({english})'
    english = textwrap.wrap(english, width=20)
    size = prop(0.075)
    font = df.fontDefiner(fontPath, size)
    df.drawMultiLine(prop(0.05), prop(0.95), h, english, font, "white", draw=textD, space=-prop(0.02))

    textB, textD = df.cropToRealSize(textB)

    canvasB = df.backgroundPNG(W, H)[0]
    canvasB = df.pasteItem(canvasB, textB, W//2-textB.width//2, H//2-textB.height//2)

    return canvasB
