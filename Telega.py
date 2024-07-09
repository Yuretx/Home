import pyautogui
import time
def main():
    pyautogui.FAILSAFE = False
    while True:
        #pyautogui.click(299,599)
        pyautogui.moveTo(81, 364)
        pyautogui.scroll(-150)
        #time.sleep (1)

if __name__ == '__main__':
    main()
