from templates.chooseYourStarter import main

images = r"""C:\Users\Exa\Desktop\chooseYourStarter\ps.png
C:\Users\Exa\Desktop\chooseYourStarter\ae.png
C:\Users\Exa\Desktop\chooseYourStarter\ai.png
"""

images = images.split('\n')[:-1]
print(images)
main(images).save(r'C:\Users\Exa\Desktop\chooseYourStarter\adobe.png')