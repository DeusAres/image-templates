import funPIL as df
from PIL import Image
from resources.paths import *

def main(W: int=2400, H: int=2400, message: list[str]='Li mortacci tua') -> Image:
    
    message = message.upper().strip()
    
    canvasB, canvasD = df.backgroundPNG(W, H)

    fontPath = str(FONTS / "futura_italic.ttf")

    font = df.fitFontInCanvas(fontPath, message, (W-50, 500))

    w, y = df.getSize(message, font)

    df.drawText(W//2, H//2 - y//2, canvasD, message, 'black', font, anchor='mt')

    return canvasB