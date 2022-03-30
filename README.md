# 🎴 image-templates

## 🎈 Create PNGs and JPGs from templates. Modular and easy

A collection of expanding templates to create from little datas fancy images. Like you would do with Photoshop's psd and mockups, but free and faster  

#### The collection features : 
- Japanese text and english translation
- Instagram tag
- iOS iMessage
- Pixel art speech bubble
- Message in a terminal(bash/cmd)
- Minimal text in times new roman
- Pixel text with gradients color
- Dictionary definitions

## 🔧 Installation  
Start your terminal, navigate to the folder that contains `requirements.txt` and enter the follow command
```console
pip install -r requirements.txt
```

## 🎨 Usage  
Start `main.py` file and choose between `Manual` and `Batch`
**Note**: since fonts are copyrighted, those are not included in this repository  
They can be added in `resources/fonts/`. Naming convention is to rename them with no spaces and caps for every word

#### Examples
`Times New Roman.ttf -> timesNewRoman.ttf`  
`Proxima.ttf -> proxima.ttf`

## 🔬 Contributing and expanding the templates
Everything that it's added to templates, correctly formatted, can become a new template
Using defaults in functions definitions, type notations, and returning PIL.Image is enough to make it work

#### Naming the template:
You can name your template every way you wish as long there are no spaces in the name

#### Managing resources:
Fonts go in `resources/fonts/` named with no spaces and caps every word  
Images to be pasted, manipulated, etc. go in `resources/images`  
Once that is done, the files can be imported using:  
```python
from resources.paths import * 
```
`FONTS` and `IMAGES` are now included variables.  
These are `pathlib.Path` and you can join names, folders and paths with `/`
```python
# Example
fontPath = FONTS / 'timesNewRoman.ttf'
# fontPath = str(fontPath) if you have problems with fontPath
```

#### Create a main function:
Creating a main function is easy but it's better to follow a couple rules:  

Let's start with an example:
```python
def main(W:int=2000, H:int=2000, message:str='Welcome'):
```
As you can see, every variable is type declared and with defaults
Defaults can be everything you want as long they reflect type notations  
This way, when using the GUI, data will be converted in the right type, and the other way around.  
It's pretty straightforward except, accepted types are
```python
int
str
list[str] # This is for accepting long texts or containing new lines
```
Respecting this guidelines will make GUI and templates work fine

#### Don't use fixed values
When creating a template the first time I made a mistake, using fix values for sizes, and coordinates.  
It meant that it wasn't possible to scale the image without losing quality  

The right way is to use proportions relative to Width and Height of the Canvas you will work on.  
You can see some examples in the templates using a lambda function  
```python
prop = lambda x : int(min(W,H)*x)
fontSize = prop(0.1)
```
Where `x` will be the position relative to the percentage of the smaller size divided by `100`

#### The output
There's only one possible output that will be useful, and that's a PIL.Image  
You can manage it how you wish, as long it's numpy and Pillow  
Since for now I'm the only one contributing, I don't need other dependecies, but those can be included with no problem.  

#### If you have choosen to contribute:
Don't esitate to contact me for anything

