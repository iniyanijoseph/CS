from tkinter import *
import cv2
from PIL import ImageTk, Image
import io
import socket
import pickle
import sys
root = Tk()
root.attributes('-fullscreen', True)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 65527))

left = Frame(root, borderwidth=3, relief="solid")
right = Frame(root, borderwidth=2, relief="solid")


def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    s.sendall(pickle.dumps(cv2image))
    msg = b""
    packet = s.recv(4096)
    while sys.getsizeof(packet) > 4000:
        msg += packet
        packet = s.recv(4096)
    msg += packet
    data = pickle.loads(msg)
    img = Image.fromarray(data)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)


def textwidget():
    txt = text.get("1.0", END)
    s.send(pickle.dumps(txt))
    msg = pickle.loads(s.recv(4096))
    text.delete("1.0", END)
    text.insert(END, msg)
    root.after(1000, textwidget)


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

""""""
lmain.pack()
scrollbar.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT)
resscrollbar.pack(side=RIGHT, fill=Y)
results.pack()

"""
Configure and Run
"""
cap = cv2.VideoCapture(0)
video_stream()
textwidget()
root.config(menu=menubar)
root.mainloop()

"""
packet = s.recv(1)
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
"""