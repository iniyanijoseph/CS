from tkinter import *
import cv2
from PIL import ImageTk, Image
import io
import socket
import pickle
root = Tk()
root.attributes('-fullscreen', True)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9873))
left = Frame(root, borderwidth=3, relief="solid")
right = Frame(root, borderwidth=2, relief="solid")

def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    s.send(pickle.dumps(img))
    msg = pickle.loads(s.recv(1024))
    imgtk = ImageTk.PhotoImage(image=msg)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)


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
root.config(menu=menubar)
root.mainloop()
