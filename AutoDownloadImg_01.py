import threading
from threading import Timer
import os
import pyautogui
import time
import _thread

input_msg = 16
screenWidth, screenHeight = pyautogui.size()

def download(msg = input_msg):

    pyautogui.moveTo(screenWidth / 9, screenHeight / 2 - 100)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(screenWidth / 4, screenHeight / 2)

    i = 0

    while i < int(msg):
        time.sleep(1)

        pyautogui.click(button="right")

        time.sleep(1)

        pyautogui.keyDown('v')

        time.sleep(3)

        pyautogui.keyDown('enter')

        time.sleep(1)

        pyautogui.keyDown('right')

        i += 1

    time.sleep(2)
    pyautogui.keyDown('esc')
    pyautogui.scroll(clicks = -1200)
    os._exit(0)  # 执行完成，退出程序


def input_with_timeout():

    pyautogui.moveTo(screenWidth / 9, 445)
    pyautogui.scroll(clicks=99999)
    # 连击三次鼠标左键
    pyautogui.click(clicks = 3)
    # 热键复制
    pyautogui.hotkey('ctrl','c')
    pyautogui.moveTo(screenWidth / 4 * 3, screenHeight / 4 * 3)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(1)
    t = Timer(4, download)
    t.start()
    msg = input("下载次数（默认16）：")
    input_msg = msg
    if len(input_msg) > 0:
        t.cancel()
        download(msg)

def input_0():
    f_name = input('创建文件夹名：')
    os.chdir(r'C:\Users\Pro\Desktop\新建文件夹')
    os.mkdir(f_name)


t1 = threading.Thread(target = input_0)
t2 = threading.Thread(target = input_with_timeout)

t1.start()
t2.start()

# input_with_timeout()
# input_0()
