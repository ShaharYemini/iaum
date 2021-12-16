# ~-~ Shahar Yemini 5782 ~-~

from time import sleep

import cv2
import keyboard as keyboard
import mouse as mouse
import pyautogui
import numpy as np

def image(path):
    return cv2.imread(path, cv2.IMREAD_UNCHANGED)


def find(source, inside, accuracy=0.9):
    result = cv2.matchTemplate(source, inside, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val < accuracy:
        return

    x = max_loc[0] + 10
    y = max_loc[1] + 10
    return x, y


def screenshot():
    picture = pyautogui.screenshot()
    return cv2.cvtColor(np.array(picture), cv2.COLOR_RGB2BGRA)


def click(img, times=-1):
    if isinstance(img, type("o")):
        img = image(img)
    count = 0
    while True:
        if times == count:
            break
        count += 1
        try:
            shot = screenshot()
            pos = find(shot, img)
            mouse.move(*pos)
            mouse.click()
            break
        except Exception:
            sleep(0.3)


def waitImg(img):
    if isinstance(img, type("o")):
        img = image(img)
    while True:
        try:
            shot = screenshot()
            if find(shot, img):
                break
        except Exception:
            sleep(0.3)
