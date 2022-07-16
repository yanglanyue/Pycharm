import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 4, screenHeight / 2)

i = 0
# x = input('input num:') or 16

while i < 16:

    time.sleep(1)
    pyautogui.click(button='right')

    time.sleep(1)
    pyautogui.keyDown('v')

    time.sleep(3)
    pyautogui.keyDown('enter')

    time.sleep(1)
    pyautogui.keyDown('right')

    i += 1

time.sleep(1)
pyautogui.keyDown('esc')








