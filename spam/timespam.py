import pyautogui
import time
import keyboard

time.sleep(2)
play = True
num = 1
while True:
    if play:
        for element in range(2):
            if element != 1:
                pyautogui.write("What is the time?")
            elif element == 1:
                pyautogui.write(f"The time since the epoch began in seconds is {time.time()}. The number is {num}")
            pyautogui.press("enter")
            time.sleep(0.75)
    num += 1
