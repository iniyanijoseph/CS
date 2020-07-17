import pyautogui
import time
from random_word import RandomWords

time.sleep(2)
wordlist = RandomWords()


def main():
    while True:
        try:
            for element in range(3):
                pyautogui.write(wordlist.get_random_word())
                pyautogui.press("enter")
                time.sleep(4)
                pyautogui.hotkey("ctrl", "t")
                pyautogui.hotkey("ctrl", "1")
                pyautogui.hotkey("ctrl", "w")
        except Exception:
            pass


if __name__ == "__main__":
    main()
