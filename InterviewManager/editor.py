from tkinter import *
import cv2
from PIL import ImageTk, Image
import io
import socket
import sys
import pickle
import sounddevice as sd
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
root = Tk()
root.attributes('-fullscreen', True)
box = Entry()
box.pack()


def enter():
    try:
        textres = box.get()
        root.destroy()
        s.connect((textres, 65527))
    except Exception as e:
        print(e)


menubar = Menu(root)
menubar.add_command(label="Exit", command=exit)
menubar.add_command(label="Submit and Continue", command=enter)
root.config(menu=menubar)
root.mainloop()
root = Tk()
root.attributes('-fullscreen', True)
left = Frame(root, borderwidth=3, relief="solid")
right = Frame(root, borderwidth=2, relief="solid")
myrecording = ([])
fs = 41100


def recvall():
    msg = b""
    packet = s.recv(1024)
    while sys.getsizeof(packet) > 1024:
        msg += packet
        packet = s.recv(1024)
    msg += packet
    return pickle.loads(msg)


def video_stream():
    duration = 1
    global myrecording
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float64')
    sd.wait()
    s.sendall(pickle.dumps(myrecording))
    myrecording = recvall()
    root.after(1, video_stream)


def video_strea():
    sd.play(myrecording, fs)
    sd.wait()
    root.after(1, video_strea)

# def textwidget():
#     _, frame = cap.read()
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     s.sendall(pickle.dumps(cv2image))
#     data = pickle.loads(recvall())
#     img = Image.fromarray(data)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#
#     txt = text.get("1.0", END)
#     s.send(pickle.dumps(txt))
#     msg = pickle.loads(s.recvall())
#     text.delete("1.0", END)
#     text.insert(END, msg)
#     root.after(2, textwidget)


def run():
    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        exec(text.get("1.0", END))
        sys.stdout = old_stdout
        results.delete("1.0", END)
        results.insert(END, redirected_output.getvalue())
    except Exception as e:
        results.config(state=NORMAL)
        results.delete("1.0", END)
        results.insert(END, e)
        results.config(state=DISABLED)


"""
Defining Widgets
"""
menubar = Menu(root)
menubar.add_command(label="Run", command=run)
menubar.add_command(label="Exit", command=exit)
scrollbar = Scrollbar(left)
resscrollbar = Scrollbar(right)
text = Text(left, yscrollcommand=scrollbar.set, height="400")
results = Text(right, yscrollcommand=resscrollbar.set, height="200")
results.config(state=DISABLED)
lmain = Label(right)

"""
Pack Frames
"""
left.pack(side="left", expand=False, fill="both")
right.pack(side="right", expand=False, fill="both")

lmain.pack()
scrollbar.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT)
resscrollbar.pack(side=RIGHT, fill=Y)
results.pack()

"""
Configure and Run
"""
cap = cv2.VideoCapture(0)
root.after(1, video_stream)
root.after(1, video_strea)
root.config(menu=menubar)
root.mainloop()
