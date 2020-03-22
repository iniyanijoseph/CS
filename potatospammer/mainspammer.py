import pyautogui
import time
import pyperclip
time.sleep(5)
num = 0
bored = "POTATO"
thing = list(bored)
print(thing)
joined = ""
"""
def paste(joined):
    pyperclip.copy(joined)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(5)
while True:
    while len(thing)<=30:
        thing.insert(0, " ")
        print(joined.join(thing))
        paste(joined.join(thing))
    while len(thing)>len(bored):
        thing.pop(0)
        print(joined.join(thing))

        paste(joined.join(thing))
"""
while True:
    time.sleep(0.1)
    for element in range(2):
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.press('enter')
    pyautogui.write('Not spam')
    time.sleep(0.1)
    pyautogui.press('e')