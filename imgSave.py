from pathlib import Path
from os import mkdir, path
from threading import Thread

import timeMyScript2
timer = timeMyScript2.Timer();
def main(img, design, quote, folder, imgType):
    timer.start()
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
    
    # This makes everything fast as fuck god I love computers
    thread = Thread(target=img.save, args=(pathToFile/(f'{filename}_{str(i)}.{imgType}'), ))
    thread.start()
    #img.save(pathToFile/(f'{filename}_{str(i)}.{imgType}'))#, optimize=True)
    
    print("save");timer.lap()
    timer.stop()
    return filename

def choosen(img, target):
    img.save(target)#, optimize=True)