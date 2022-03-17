from os import mkdir, path


def main(img, design, quote, type, ROOT):
    quote = quote[:15]
    type = type.upper()
    no = """#%&{}\\<>*?/ $!'":@+`|=\n,;-_°()[]. """
    for each in no:
        quote = quote.replace(each, '')

    if path.isdir(ROOT / type / design) is False:
        mkdir(ROOT / type / design)

    filename = str(ROOT / type / design / (design + "_" + quote + "." + type))

    img.save(filename, optimize=True)

    return filename
