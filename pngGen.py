from textwrap import wrap
import funPIL as df
from rootFolder import rf

ROOT = rf(__file__, "typography")
FONTS = ROOT / "fonts"
IMAGES = ROOT / "images"


def main(font, message, wrapping=True):
    canvasW, canvasH = 2000, 3000
    canvasB, canvasD = df.backgroundPNG(canvasW, canvasH)
    canvasB2 = df.backgroundPNG(canvasW, canvasH)[0]

    font_path = str(FONTS / font)
    def wrap_len(message):
        words = len(message.split(" "))
        if words <= 10:
            return 10
        elif words >= 18:   
            return 18
        else:
            return words + 2

    if wrapping == True:
        message = wrap(message, wrap_len(message), break_long_words=False, break_on_hyphens= True)
    else:
        message = [message]
    size = df.fitSize(font_path, message, canvasW)
    font = df.fontDefiner(font_path, int(size*1.5))
    

    textB, textD =  df.backgroundPNG(canvasW + 1500, canvasH + 1000)
    textD = df.drawMultiLine(750, canvasW+750, 0, message, font, 
        "black", border = False, draw = textD)
    
    textB2 = df.replaceColor(textB, (0,0,0), (255,255,255))
    textB2 = df.strokeImage(textB2, 3, "#000000")

    textB, textB2 = [df.cropToRealSize(each) for each in [textB, textB2]]
    textB, textB2 = [df.resizeToFitSpace(each, [canvasW - 20, canvasH - 100]) for each in [textB, textB2]]

    x, y = df.centerItem(canvasB, textB)
    if y > 200:
        y = 200
    canvasB = df.pasteItem(canvasB, textB, x, y)

    x, y = df.centerItem(canvasB2, textB2)
    if y > 200:
        y = 200
    canvasB2 = df.pasteItem(canvasB2, textB2, x, y)

    return canvasB, canvasB2








def shortMessage(font, message, fontColor):
    canvasW, canvasH = 2000, 3000
    canvasB, canvasD = df.backgroundPNG(canvasW, canvasH)
    perc = min(canvasW, canvasH)

    if '\n' in message:
        message = message.split('\n')[:-1]

    size = 100
    font_path = str(FONTS / font)
    font = df.fontDefiner(font_path, size)
    if type(message) in [list, tuple]:
        w_text, _, h_text, _ = df.getMultipleSize(message, font)
    else:
        w_text, h_text = df.getSize(message, font)
    
    size = int(perc * size / max(w_text, h_text))
    font = df.fontDefiner(font_path, size)
    
    if type(message) in [list, tuple]:
        w_text, _, h_text, _ = df.getMultipleSize(message, font)
        canvasD = df.drawMultiLine(0, canvasW, int(canvasH//2 - h_text//2), message, font, fontColor, justify="center", draw = canvasD)
    else:
        w_text, h_text = df.getSize(message, font)
        canvasD = df.drawText(int(canvasW/2 - w_text/2), int(canvasH/2 - h_text/2), canvasD, message, fontColor, font)

    return canvasB


def largeText(message, color='white', font='Impact.ttf'):
    canvasW, canvasH = 4000, 6000
    message = message.strip('\n').split('\n')
    message = [each.strip() for each in message]
    font_path = str(FONTS / font)
    space = 100
    pad = int(canvasW*5/100)
    Hs = [0]
    sizes = []
    for line in message:
        sizes.append(df.fitSize(font_path, line, canvasW - pad))
        Hs.append(Hs[-1] + df.getSize(line, df.fontDefiner(font_path, sizes[-1]))[1])
        Hs[-2] = Hs[-2] - int(Hs[-1]*20/100)
        Hs[-1] += space

    # canvasH = Hs[-1] - int(Hs[-1]*20/100)
    canvasB, canvasD = df.backgroundPNG(canvasW, canvasH)

    for i in range(len(message)):
        font = df.fontDefiner(font_path, sizes[i])
        canvasD = df.drawText(pad//2, Hs[i], canvasD, message[i], color, font)

    return canvasB

"""
def sticker(img, color):
    expand = int(min(*img.size) * 30 / 100)
    img = df.expand(img, expand, expand)[0]
    img = df.fillTransparent(img, color)

    return img
"""

def sticker(img, color):
    if type(img) == str:
        img = df.openImage(img)[0]

    img = df.cropToRealSize(img)
    W, H = img.size
    expand = int(min(W, H) * 30 / 100)
    CB, CD = df.backgroundPNG(W+expand, H+expand, color)
    CB = df.pasteItem(CB, img, *[expand//2]*2)

    return CB

