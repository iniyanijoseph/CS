from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import os
import subprocess

templatestring = """"""
with open("maininterface.py", "r") as FILE:
    templatestring = FILE.read()
projects = []
projectname = ""


def newproject():
    global templatestring
    global projectname
    projectname = simpledialog.askstring("Caption Select", "Choose a Title for a Project")
    os.mkdir(projectname)
    if projectname is not None:
        try:
            with open(f"{projectname}\\interface.py", "w") as file:
                for line in templatestring:
                    file.write(line)

            def launchproject():
                global projectname
                subprocess.Popen(["python", f"{projectname}\\interface.py"])

            if projectname not in projects:
                givenclasses = Button(
                    uiside,
                    text=f"Open {projectname}",
                    command=launchproject,
                    width=35)
                givenclasses.pack(fill=X)
                projects.append(projectname)

        except Exception as e:
            messagebox.showerror("PROJECTNAME ALREADY EXISTS", "CHOOSE DIFFERENT NAME. PROJECT ALREADY EXISTS")


root = Tk()
root.resizable(width=FALSE, height=TRUE)

uiside = Frame(root, width=250, height=250, borderwidth=3, relief="solid")
uiside.pack(side=RIGHT, fill=BOTH, expand=True)

menubar = Menu(root)
menubar.add_command(label="New Project", command=newproject)

root.config(menu=menubar)
root.mainloop()
