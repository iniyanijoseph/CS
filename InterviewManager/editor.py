from tkinter import *
import cv2
from PIL import ImageTk, Image
import io
import socket
import pickle
root = Tk()
root.attributes('-fullscreen', False)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9873))
left = Frame(root, borderwidth=3, relief="solid")
right = Frame(root, borderwidth=2, relief="solid")
"""
# Audio
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
"""

def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    s.sendall(pickle.dumps(cv2image))
    data = b""
    for element in range(10000):
        packet = s.recv(4096)
        data += packet
        if not packet:
            break
    msg = pickle.loads(data)
    img = Image.fromarray(msg)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)


def textwid():
    txt = text.get("1.0", END)
    s.send(pickle.dumps(txt))
    print(pickle.dumps(txt))
    msg = pickle.loads(s.recv(4096))
    text.delete("1.0", END)
    text.insert(END, msg)
    root.after(1000, textwid)


def run():
    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        exec(text.get("1.0", END))
        sys.stdout = old_stdout
        results.delete("1.0", END)
        results.insert(END, redirected_output.getvalue())
    except:  # catch *all* exceptions
        e = sys.exc_info()[0]
        results.delete("1.0", END)
        results.insert(END, e)


"""
Defining Widgets
"""
# MenuBar
menubar = Menu(root)
# Menubar Command
menubar.add_command(label="Run", command=run)
menubar.add_command(label="Exit", command=exit)
# Scrollbar for Text
scrollbar = Scrollbar(left)
# Scrollbar for Result
resscrollbar = Scrollbar(right)
# Text for writing in
text = Text(left, yscrollcommand=scrollbar.set, height="400")
# Text for Results
results = Text(right, yscrollcommand=resscrollbar.set, height="200")
# Video Input/Output
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
textwid()
root.config(menu=menubar)
root.mainloop()
exit()
