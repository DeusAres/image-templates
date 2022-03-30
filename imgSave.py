from pathlib import Path
from os import mkdir, path

def main(img, design, quote, folder, imgType):
    quote = quote[:15]
    no = """#%&{}\\<>*?/ $!'":@+`|=\n,;-_°()[].~"""
    for each in no:
        quote = quote.replace(each, '')

    folder = Path(folder)
    if path.isdir(folder / design) is False:
        mkdir(str(folder / design))

    pathToFile = folder / design
    filename = (f'{design}_{quote}')
    i = 1
    while path.isfile(pathToFile / (f'{filename}_{str(i)}.{imgType}')):
        i+=1

    img.save(pathToFile/(f'{filename}_{str(i)}.{imgType}'), optimize=True)

    return filename

def choosen(img, target):
    img.save(target, optimize=True)