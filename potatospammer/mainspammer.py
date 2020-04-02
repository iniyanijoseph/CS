import pyautogui
import time
import pyperclip
time.sleep(5)
num = 0
bored = "POTATO"
thing = list(bored)
joined = ""

def paste(joined):
    #pyperclip.copy(joined)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
while True:
    while len(thing) <= 30:
        thing.insert(0, " ")
        paste(joined.join(thing))
    while len(thing)>len(bored):
        thing.pop(0)
        paste(joined.join(thing))
"""
"""