from textwrap import wrap
from PIL import Image
import funPIL as df
from resources.paths import * 

def main(W: int=1000, H: int=1000, message: list[str]='my iOS message as been delivered!', bubble_color: str='#0e7efa', message_color: str='#ffffff') -> Image:

    canvasB, canvasD = df.backgroundPNG(W, H)
    font = str(FONTS / "helvetica.ttf")
    
    perc = min(W, H)
    size = int(perc*0.075)
    font = df.fontDefiner(font, size)
    spacing = int(perc*0.030)

    pad_up, pad_down, pad_left, pad_right = int(perc*0.0425), int(perc*0.0425), int(perc*0.055), int(perc*0.07)

    new_message = []
    for each in message.split('\n'):
        wrap_size = 37
        while df.getSizeMultiline(wrap(each, wrap_size), font, spacing)[0] > perc - (pad_left + pad_right)*2:
            wrap_size -= 1
        for wrapped in wrap(each, wrap_size):
            new_message.append(wrapped)

    #values = df.getMultipleSize(new_message, font)
    values = df.getSizeMultiline(new_message, font, spacing)

    message_w, message_h = values[0], values[1]
    message_x, message_y = int((W - message_w)/2), int((H - message_h)/2)

    rectX1, rectY1 = message_x - pad_left, message_y - pad_up
    rectX2, rectY2 = message_x + message_w + pad_right, message_y + message_h + pad_down
    rectB, rectD = df.backgroundPNG(rectX2 - rectX1, rectY2 - rectY1, bubble_color)

    rectB = df.roundCorners(rectB, int(perc*0.07))
    

    canvasB = df.pasteItem(canvasB, rectB, rectX1, rectY1)
    #canvasB, canvasD = df.blurImage(canvasB, 1)

    bubble = df.openImage(str(IMAGES / "bubble.png"))[0]
    bubble, _ = df.resizeToFit(bubble, int(bubble.width * perc/4080))
    bubble = df.fillWithColor(bubble, bubble_color)
   
    pad_bubble = int(bubble.width*143/246) + 1#103
    canvasB = df.pasteItem(canvasB, bubble, rectX2 - pad_bubble , rectY2 - bubble.height)

    #df.drawMultiLine(message_x, message_x+message_w, message_y, new_message,
    #    font, message_color, justify='left', draw=canvasD, space = 0)
    df.drawMultiline(message_x, message_y, canvasD, new_message, font, message_color, anchor='la', spacing=spacing)

    return canvasB  