from tkinter import *
from tkinter import filedialog
import os
win = Tk()
win.title("CodeBot")
width = 500
height = 600
win.geometry(str(width) + "x" + str(height))


def openfile():
    try:
        file = filedialog.askopenfilename(defaultextension=".py", filetypes=[("All Files", "*.*")])
        file = open(file)
        file = file.read()
        text.delete(1.0, END)
        text.insert(END, file)
    except:
        pass


def saveasfile():
    try:
        file = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("All Files", "*.*"), ("Python Files", "*.py")])
        file = open(file, "w")
        file = file.write(text.get(1.0, END))
        text.delete(1.0, END)
        text.insert(END, file)
    except:
        pass


def runfile():
    try:
        file = filedialog.askopenfilename(defaultextension=".py", filetypes=[("All Files", "*.*")])
        exec(open(file).read())
    except:
        pass


def savefile():
    try:
        file = os.path.dirname(os.path.abspath(__file__))
        print(file)
        file = open(file, "w")
        file = file.write(text.get(1.0, END))
        text.delete(1.0, END)
        text.insert(END, file)
    except:
        pass


def texthighlight():
    textlist = text.get(1.0, END)
    textlist = textlist.split("\n")
    for line in textlist:
        line.split(" ")
    print(textlist)


def quit():
    exit()


def battle():
    pass

menu = Menu(win)
menu.add_command(label="Open", command=openfile)
menu.add_command(label="New File", command=saveasfile)
menu.add_command(label="Save", command=savefile)
menu.add_command(label="Run", command=runfile)
menu.add_command(label="Highlight", command=texthighlight)
menu.add_command(label="Quit", command=quit)
menu.add_command(label="Battle!", command=battle)

text = Text(win, width=width, height=height)

text.grid(row=1, column=0)

win.config(menu=menu)

mainloop()
