import funPIL as df
from resources.paths import *

def main(W: int=1000, H: int=1000, message: str='instagram.tag_image'):
    
    canvasB, canvasD = df.backgroundPNG(W, H)
    prop = lambda x : int(min(W, H)*x)

    message = message.lower()

    pad = prop(0.23)
    font_path = (str(FONTS / "proxima.otf"))

    size = df.fitSize(font_path, message, W - pad)
    font = df.fontDefiner(font_path, size)
    x,y = df.getSize(message, font)

    if y*1.7 > H//2:
        size = int((H//2) * size / (y*1.7))
        font = df.fontDefiner(font_path, size)
        x,y = df.getSize(message, font)
        

    triangle = df.openImage(str(IMAGES / "triangle.png"))[0]
    triangle = df.resizeToFit(triangle, int(y*0.7), True)[0]

    padRect = y*2
    rectW, rectH = int(x + padRect/2), int(y + padRect/2)
    if rectW/rectH < 2:
        rectW = int(rectH*1.8)

    if rectW > W:
        p = W/rectW
        font = df.fontDefiner(font_path, int(size*p))
        x,y = df.getSize(message, font)
        padRect = y*2
        rectH = int(y + padRect/2)
        rectW = int(W*0.98)
        
    rectB, rectD = df.backgroundPNG(rectW, rectH, 'black')
    rectB = df.roundCorners(rectB, int(y*0.5))
    rectB = df.setOpacity(rectB, 90)
    rectB = df.pasteItem(canvasB, rectB, *df.centerItem(canvasB, rectB))

    df.drawText(W//2, H//2, canvasD, message, "white", font, 'mm')
    triangle = df.setOpacity(triangle, 90)
    triangle = df.blurImage(triangle, 1)

    xCent, yCent = int(W/2 - triangle.width/2), int(H//2 - rectH//2 - triangle.height)
    canvasB = df.pasteItem(canvasB, triangle, xCent, yCent)

    

    return canvasB