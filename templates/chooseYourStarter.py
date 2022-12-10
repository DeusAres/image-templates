import funPIL as df
from resources.paths import *

def main(images:list[str]='Put paths with comma'):

    CB = df.openImage(IMAGES/'chooseYourStarter.png')[0].convert('RGBA')

    if type(images) == str:
        images = images.split(',')
        images = [each.strip(' ') for each in images]

    images = [df.openImage(each)[0].convert('RGBA') for each in images]
    images = [df.cropToRealSize(each)[0] for each in images]
    images = [df.resizeToFit(each, 833)[0] for each in images]

    centers = [[912,460], [1800,460], [2705,460]]
    for i in range(len(images)):
        x,y = centers[i][0]-images[i].width//2, centers[i][1]-images[i].height//2
        CB = df.pasteItem(CB, images[i], x, y)

    return CB

    

