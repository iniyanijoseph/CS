import pyautogui
import time
from random_word import RandomWords

time.sleep(2)

wordlist = RandomWords()

while True:
    for element in range(3):
        pyautogui.write(word = wordlist.get_random_word())
        pyautogui.press("enter")
        time.sleep(0.75)
