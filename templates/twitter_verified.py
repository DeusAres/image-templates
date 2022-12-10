import funPIL as df
from resources.paths import *
# Will not be reloaded each time in batch ihihihihihih smart
import timeMyScript2
verified = df.openImage(str(IMAGES / 'twitterVerified.png'))[0]
timer = timeMyScript2.Timer();
def main(W: int=4800, H: int=4800, message: list[str]="programmer") -> df.Image:
    
    canvasB, canvasD = df.backgroundPNG(W, H)

    global verified
    if verified.width != W//3:
        verified = df.resizeToFit(verified, W//3)[0]

    df.pasteItem(canvasB, verified, 0, H//2 - verified.height//2)

    fontPath = (str(FONTS / 'Helvetica_Bold.ttf'))
    font = df.fitFontInCanvas(fontPath, message, [W//1.6, verified.height//4])
    message = ["verified", message]
    messageHeight = df.getSizeMultiline(message, font, font.size*0.2)[1]
    df.drawMultiline(W//2.66, H//2-messageHeight//2, canvasD, 
        message,
        font, 'black', 'la', font.size*0.2)
    
    canvasB, canvasD = df.centerContent(canvasB)

    return canvasB

