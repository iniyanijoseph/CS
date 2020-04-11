import time
import pyautogui
from tkinter import messagebox

countdown = 0
while True:
    if pyautogui.locateCenterOnScreen("youtubebar.png", confidence=0.9) and countdown == 0:
        time.sleep(5)
        messagebox.showinfo("Error", "Error")
        countdown -= 1