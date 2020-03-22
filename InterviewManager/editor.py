from tkinter import *
import cv2
from PIL import ImageTk, Image
import io
root = Tk()
root.attributes('-fullscreen', True)

left = Frame(root, borderwidth=3, relief="solid")
right = Frame(root, borderwidth=2, relief="solid")


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



scrollbar = Scrollbar(left)
resscrollbar = Scrollbar(right)
text = Text(left, yscrollcommand=scrollbar.set, height="400")
results = Text(right, yscrollcommand=resscrollbar.set, height="200")
menubar = Menu(root)
lmain = Label(right)

menubar.add_command(label="Run", command=run)
left.pack(side="left", expand=False, fill="both")
right.pack(side="right", expand=False, fill="both")
cap = cv2.VideoCapture(0)

# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)

video_stream()

scrollbar.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT)
lmain.pack()
resscrollbar.pack(side=RIGHT, fill=Y)
results.pack()

root.config(menu=menubar)
root.mainloop()