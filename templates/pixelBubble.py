from PIL import Image
from textwrap import wrap
from funPIL import df
from resources.paths import * 

def main(message):
    if type(message) not in [list, tuple]:
        message = wrap(message, 14, break_long_words=False)

    def diagonal(x, y, diag, center_x, center_y):
        def check(z, center, diag):
            z = z+diag if z < center else z-diag
            return z

        x, y = [check(i, j, diag) for i, j in [[x, center_x], [y, center_y]]]
        return [x, y]

    def transparent(coordinates, diag, draw):
        squares = [
                   lambda x, y, diag: [x, y],
                   lambda x, y, diag: [x, y-diag],
                   lambda x, y, diag: [x-diag, y-diag],
                   lambda x, y, diag: [x-diag, y]
                  ]

        for x, y in coordinates:
            for i in range(len(squares)):
                alpha = 255 if i == 0 else 0
                sx, sy = squares[i](x, y, diag)
                draw.rectangle([sx, sy, sx+diag-1, sy+diag-1], fill=(0, 0, 0, alpha))
            squares.append(squares.pop(0))

    W, H = 3000, 3000
    prop = lambda x : int(min(W, H) * x)
    canvasB, canvasD = df.backgroundPNG(W, H)
    center_w, center_h = canvasB.width//2, canvasB.height//2

    # TEXT RELATED
    textB, textD = df.backgroundPNG(W, H)
    font = df.fontDefiner(str(FONTS / "silk_screen.ttf"), prop(0.016))
    df.drawMultiLine(0, W, 0, message, font, 'black', 'center', draw=textD, space=prop(0.003))
    textB, textD = df.cropToRealSize(textB)
    textB = df.fillOpaque(textB)
    textB = textB.resize([int(textB.width//prop(0.001)), int(textB.height//prop(0.001))], resample=Image.NEAREST)
    # END TEXT RELATED

    diagonal_sum = 3
    x_pad = 7 + diagonal_sum
    y_pad = 8 + diagonal_sum

    zero_text_w, zero_text_h = center_w - textB.width//2, center_h - textB.height//2
    full_text_w, full_text_h = center_w + textB.width//2, center_h + textB.height//2

    a = zero_text_w - x_pad, zero_text_h - y_pad
    c = full_text_w + x_pad, full_text_h + y_pad
    b = a[0], c[1]
    d = c[0], a[1]

    z1 = diagonal(*a, diagonal_sum, center_w, center_h)
    z2 = diagonal(*b, diagonal_sum, center_w, center_h) ; z2[1] += 1
    z3 = diagonal(*c, diagonal_sum, center_w, center_h) ; z3[0]+= 1 ; z3[1] += 1
    z4 = diagonal(*d, diagonal_sum, center_w, center_h) ; z4[0] += 1

    canvasD.rectangle([*a,*c], fill = (255,255,255,255), outline = (0,0,0,255), width = 3)
    transparent([z1, z2, z3, z4], diagonal_sum, canvasD)

    spike = df.openImage(str(IMAGES / "spike.png"))[0].convert("RGBA")
    x_spike = center_w - spike.width//2 - ((z3[0] - z1[0]) // 4)
    canvasB = df.pasteItem(canvasB, spike, x_spike, z2[1])

    shadow = df.fillWithColor(canvasB, (0, 0, 0))
    shadow = df.setOpacity(shadow, prop(0.006))

    canvasB = df.pasteItem(shadow, canvasB, 0+prop(0.001), 0-prop(0.001))
    canvasB = df.pasteItem(canvasB, textB, zero_text_w+prop(0.001), zero_text_h-prop(0.001))
    
    canvasB, _ = df.cropToRealSize(canvasB)
    canvasZ = df.backgroundPNG(2000, 3000)[0]
    canvasB, _ = df.resizeToFit(canvasB, 2000, None, Image.NEAREST)
    canvasZ = df.pasteItem(canvasZ, canvasB, 0, 0)
    return canvasZ