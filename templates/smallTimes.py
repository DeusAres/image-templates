import funPIL as df
from resources.paths import * 

def main(W: int=1000, H: int=1000, message: str='Small minimal times', message_color: str='#ffffff'):
    fontPath = FONTS / "timesNewRoman.ttf"

    textB, textD = df.backgroundPNG(W, H)

    size = df.fitSize(fontPath, message, W)
    font = df.fontDefiner(fontPath, size)
    df.drawText(W//2, H//2, textD, message, message_color, font, 'mm')

    return textB