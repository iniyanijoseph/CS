from tkinter import *
from tkinter import colorchooser
from tkinter import simpledialog
import subprocess

bgc = (255, 255, 255)
title = "Pygame Project"
objectlist = """
"""
mainlooptext = """allobjects.update()
    allobjects.draw(win)"""
classes = []
clastring = """
"""
classtitle = ""
sizing = (500, 300)
continueupdate = True

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
    check = colorchooser.askcolor(color=None)[0]
    if check is not None:
        bgc = check


def getcaption():
    global title
    check = simpledialog.askstring("Caption Select", "Choose a Title for a Project")
    if check is not None:
        title = check


def getsizing():
    global sizing
    check = simpledialog.askstring("Sizing Select", "Choose the Dimesnsions for your project")
    if check is not None:
        sizing = check


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

    def launchnotepad():
        global classtitle
        programname = "notepad.exe"
        filename = f"{classtitle}.py"
        subprocess.Popen([programname, filename])

    with open(f"{classtitle}.py", "w") as FILE:
        FILE.write(classtemplate)
        if f"{classtitle}.py" not in classes:
            givenclasses = Button(
                uiside,
                text=f"Launch Notepad with {classtitle} class",
                command=launchnotepad,
                width=35)
            givenclasses.pack(fill=X)
            classes.append(f"{classtitle}.py")

            objectlist += f"""for element in range(1):
                allobjects.add({classtitle}())\n"""


def preview():
    subprocess.Popen(["python", "main_script.py"])


root = Tk()
root.resizable(width=FALSE, height=TRUE)

uiside = Frame(root, width=250, height=250, borderwidth=3, relief="solid")
uiside.pack(side=RIGHT, fill=BOTH, expand=True)

menubar = Menu(root)
menubar.add_command(label="ChooseBGColor", command=getcolor)
menubar.add_command(label="ChooseTitle", command=getcaption)
menubar.add_command(label="ChooseWindowSizing", command=getsizing)
menubar.add_command(label="Non-Sprite Object", command=newclass)
menubar.add_command(label="Preview Pygame", command=preview)


root.config(menu=menubar)
while True:
    writestring = f"""import pygame  # Import the module for use
pygame.init()  # Initialize the video system for output

configlist = {[bgc, title, sizing]}
win = pygame.display.set_mode(configlist[2])  # Create a window to which we can draw onto
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
            run = False
    pygame.display.update()
    pygame.time.delay(100)
pygame.quit()
"""
    clastring = """"""
    for file in classes:
        with open(file, "r") as fg:
            contents = fg.read()
            contents += "\n"
            clastring += contents
    if continueupdate:
        with open("Thing/main_script.py", "w") as fg:
            for line in writestring:
                fg.write(line)
    root.title(title)
    root.update()
