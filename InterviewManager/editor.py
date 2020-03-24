from tkinter import *
import cv2
from PIL import ImageTk, Image
import io
import socket
root = Tk()
root.attributes('-fullscreen', True)

# Main Frames
left = Frame(root, borderwidth=3, relief="solid")
right = Frame(root, borderwidth=2, relief="solid")
left.pack(side="left", expand=False, fill="both")
right.pack(side="right", expand=False, fill="both")


# Function to Video stream
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)


# Function to run
def run():
    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        exec(text.get("1.0", END))
        sys.stdout = old_stdout
        results.delete("1.0", END)
        results.insert(END, redirected_output.getvalue())
    except:
        e = sys.exc_info()[0]
        results.delete("1.0", END)
        results.insert(END, e)


# Scrollbar for editing side
scrollbar = Scrollbar(left)
scrollbar.pack(side=RIGHT, fill=Y)

# Scrollbar for results
resscrollbar = Scrollbar(right)
resscrollbar.pack(side=RIGHT, fill=Y)

# Text for editing
text = Text(left, yscrollcommand=scrollbar.set, height="400")
text.pack(side=LEFT)

# Text for results
results = Text(right, yscrollcommand=resscrollbar.set, height="200")

# Menubar
menubar = Menu(root)
menubar.add_command(label="Run", command=run)
menubar.add_command(label="Exit", command=exit)

# Video Stream
lmain = Label(right)
cap = cv2.VideoCapture(0)
video_stream()
lmain.pack()

# Configure and run
root.config(menu=menubar)
root.mainloop()
