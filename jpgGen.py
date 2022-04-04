import funPIL as df



def main(png, backgroundColor, destination):

    png = df.cropToRealSize(png.convert("RGBA"))[0]

    if destination == 'instagram':
        CW, CH = 1080, 1350
    elif destination == 'pinterest':
        CW, CH = 1000, 1500

    C = df.backgroundPNG(CW, CH, backgroundColor)[0]
    png = df.resizeToFit(png, min(CW, CH) - 50)[0]
    C = df.pasteItem(C, png, *df.centerItem(C, png))

    return C.convert('RGB')