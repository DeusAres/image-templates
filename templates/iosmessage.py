from textwrap import wrap
from funPIL import df
from resources.paths import * 


def main(message, bubbleColor='#0e7efa'):
    W, H = 2000, 3000
    canvasB, canvasD = df.backgroundPNG(W, H)
    font = str(FONTS / "Helvetica.ttf")
    
    perc = min(W, H)
    size = int(perc*0.075)
    font = df.fontDefiner(font, size)

    pad_up, pad_down, pad_left, pad_right = int(perc*0.0425), int(perc*0.03), int(perc*0.055), int(perc*0.07)

    new_message = []
    for each in message.split('\n'):
        wrap_size = 37
        while df.getMultipleSize(wrap(each, wrap_size), font)[0] > perc - (pad_left + pad_right)*2:
            wrap_size -= 1
        for wrapped in wrap(each, wrap_size):
            new_message.append(wrapped)

    values = df.getMultipleSize(new_message, font)

    message_w, message_h = values[0], values[2]
    message_x, message_y = int((W - message_w)/2), int((H - message_h)/2)

    rectX1, rectY1 = message_x - pad_left, message_y - pad_up
    rectX2, rectY2 = message_x + message_w + pad_right, message_y + message_h + pad_down
    rectB, rectD = df.backgroundPNG(rectX2 - rectX1, rectY2 - rectY1, bubbleColor)

    rectB = df.roundCorners(rectB, int(perc*0.07))
    #rectB = df.blurEdges(rectB, 1)

    canvasB = df.pasteItem(canvasB, rectB, rectX1, rectY1)

    bubble = df.openImage(str(IMAGES / "bubble.png"))[0]
    bubble, _ = df.resizeToFit(bubble, int(bubble.width * perc/4080))[0]
    bubble = df.fillWithColor(bubble, bubbleColor)
    pad_bubble = int(bubble.width*143/246) + 2#103
    canvasB = df.pasteItem(canvasB, bubble, rectX2 - pad_bubble , rectY2 - bubble.height)

    df.drawMultiLine(message_x, message_x+message_w, message_y, new_message,
        font, 'white', justify='left', draw=canvasD, space = 0)

    return canvasB  