from funPIL import df


def main(png, backgroundColor = "white"):

    png = df.cropToRealSize(png.convert("RGBA"))
    CW, CH = 1000, 1500
    pad = 200

    C = df.backgroundJPG(CW, CH, backgroundColor)[0]

    df.resizeToFitSpace()
    png = df.resizeToFit(png, CW-pad)

    C = df.pasteItem(C, png, *df.centerItem(C, png))

    return C

