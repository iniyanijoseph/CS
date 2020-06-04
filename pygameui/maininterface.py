import pygame
from tkinter import *
from tkinter import colorchooser
import os
from tkinter import simpledialog

bgc = (255, 255, 255)
title = "Pygame Project"
global objectlist
global classtitle
global classtemplate
objectlist = """
"""
mainlooptext = """allobjects.update()
    allobjects.draw(win)"""
classes = []
clastring = """
"""

classtitle = ""

classtemplate = f"""class {classtitle}(pygame.sprite.Sprite):
def __init__(self):
    super().init()
    self.image = ""
    self.rect = self.image.get_rect()

def update(self):
    pass 
"""


def getcolor():
    global bgc
    bgc = colorchooser.askcolor(color=None)[0]


def getcaption():
    global title
    title = simpledialog.askstring("Caption Select", "Choose a Title for a Project")


def newclass():
    global classtitle
    global classtemplate
    global objectlist
    classtitle = simpledialog.askstring('New Class File', 'Choose a Name for your Class')
    classtemplate = f"""class {classtitle}(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("*.png").convert()
        self.rect = self.image.get_rect()
    
    def update(self):
        pass"""
    with open(f"{classtitle}.py", "w") as fg:
        fg.write(classtemplate)
        givenclasses = Label(uiside, text=classtitle)
        givenclasses.pack(fill=X)
        classes.append(f"{classtitle}.py")

        objectlist += f"allobjects.add({classtitle}())\n"


root = Tk()

pgside = Frame(root, width=750, height=500, borderwidth=3, relief="solid")
pgside.pack(side=LEFT, fill=BOTH, expand=True)
uiside = Frame(root, width=250, height=500, borderwidth=3, relief="solid")
uiside.pack(side=RIGHT, fill=BOTH, expand=True)

menubar = Menu(root)
menubar.add_command(label="ChooseBGColor", command=getcolor)
menubar.add_command(label="ChooseTitle", command=getcaption)
menubar.add_command(label="Non-Sprite Object", command=newclass)

os.environ['SDL_WINDOWID'] = str(pgside.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
win = pygame.display.set_mode((750, 500))
pygame.display.init()
pygame.display.update()


def draw():
    win.fill(bgc)
    pygame.draw.rect(win, (0, 0, 0), (5, 5, 10, 10))
    pygame.display.update()


root.config(menu=menubar)
while True:
    writestring = f"""import pygame  # Import the module for use
pygame.init()  # Initialize the video system for output

win = pygame.display.set_mode((750, 500))  # Create a window to which we can draw onto
configlist = {[bgc, title]}
pygame.display.set_caption(configlist[1]) 
allobjects = pygame.sprite.Group()

# Classes
{clastring}

{objectlist}
run = True  # Variable we can use to end the window
while run:
    win.fill(configlist[0])
    {mainlooptext}
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    pygame.time.delay(100)
"""
    clastring = """"""
    for file in classes:
        with open(file, "r") as fg:
            contents = fg.read()
            contents += "\n"
            clastring += contents
    with open("None.py", "w") as fg:
        for line in writestring:
            fg.write(line)
    draw()
    root.title(title)
    pygame.display.update()
    root.update()
