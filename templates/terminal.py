import funPIL as df
from resources.paths import *


def main(W: int=1000, H: int=1000, message: list[str]='rm -rf /', root: bool=False):

    if root:
        message = "root@user:~$ " + message
    else:
        message = "~$ " + message
    message = message.split('\n')
    
    fontPath = FONTS / 'consolas.ttf'
    font = df.fitFontInCanvas(fontPath, message, (W, H))

    canvasB, canvasD = df.backgroundPNG(W, H)

    df.drawMultiline(0, 0, canvasD, message, font, 'white')
    #df.drawMultiLine(0, W, 0, message, font, 'white', 'left', draw=canvasD)

    return canvasB

