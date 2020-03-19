import pyperclip
import tkinter
win = tkinter.Tk()
win.title("Reverse String")
width = 200
height = 200
win.geometry(str(width) + "x" + str(height))


def main():
    stdin = text.get()
    leng = len(stdin) - 1
    finstr = ""
    while leng >= 0:
        finstr += stdin[leng]
        leng -= 1
    pyperclip.copy(finstr)


text = tkinter.Entry(win)
text.pack()
b = tkinter.Button(win, text="Reverse", width=20, command=main)
b.pack()
tkinter.mainloop()
