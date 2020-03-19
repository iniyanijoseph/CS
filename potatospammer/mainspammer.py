import pyautogui

while(True):
    hspot = pyautogui.locateOnScreen('Hangoutspic.png', confidence=0.9)
    print(hspot)
