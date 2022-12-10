import funPIL as df
from resources.paths import *
from random import randint

def main(W:int=2000, H:int=2000, message:list[str]='Color cascade'):
    
    prop = lambda x : int(min(W, H) * x)

    distance = prop(0.01)

    times = 5
    fontPath = FONTS / 'arialBoldItalic.ttf'
    font = df.fitFontInCanvas(fontPath, message, min(W, H)-(distance*times))

    CB, CD = df.backgroundPNG(W, H)
    TB, TD = df.backgroundPNG(W, H)

    center = W//2, H//2
    start = center[0] - distance*2, center[1] - distance*2

    df.drawMultiline(*start, TD, message, font, 'white', 'ma', align='center')

    TB = df.strokeImage(TB, prop(0.004), '#000000')
    TB = df.cropToRealSize(TB)[0]

    randomColor = randint(0, 360), 57, 100
    add = randint(20, 360/times)
    colors = 
    for x in (start[0], start[0]*5, distance):
        for y in (start[1], start[1]*5, distance):


    