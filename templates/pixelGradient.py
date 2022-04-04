import funPIL as df
from resources.paths import *
from textwrap import wrap

def main(W: int=1000, H: int=1000, message: list[str]='Pixel gradient!'):
    from random import randint as ri
    canvasB, canvasD = df.backgroundPNG(W, H)
    prop = lambda x : int(min(W, H) * x)
    pad = prop(0.1)
    font_path = str(FONTS / "04b.ttf")
    message = wrap(message, 14)
    size = df.fitSize(font_path, message, W - pad)
    font = df.fontDefiner(font_path, size)
    
    values = df.getMultipleSize(message, font)

    textB, textD = df.backgroundPNG(W, H)
    df.drawMultiLine(0, W, H // 2 - values[2]//2, message, font, 
        "white", draw=textD, space=prop(0.012))
    
    textB = df.cropToRealSize(textB)[0]
   
    canvasB = df.pasteItem(canvasB, textB, *df.centerItem(canvasB, textB))

    gradientB, gradientD = df.backgroundJPG(W, H, "white")

    color = ri(0,360), 100, 65
    x = 30
    for y in range(df.centerItem(canvasB, textB)[0], H, x):
        gradientD.line((0, y, W, y), fill = df.hslToRgb(*color), width = x)
        color = df.addColor(color, (20, 0, 0))
    
    canvasB = df.cutWithMask(gradientB, canvasB, canvasB.copy().convert('L'))
    canvasB = df.strokeImage(canvasB, prop(0.004), '#000000', 2)
    return canvasB