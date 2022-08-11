import pyautogui
import random
from time import sleep
import cv2 as cv
from mss import mss
import numpy as np
import math
# pyautogui.moveTo(x=515, y=345, duration=0.5)

speed = 400
test_ferndell = []
test_black = []
i = 0
maximum_ferndell = 0
maximum_black = 0

pyautogui.keyDown('alt')
pyautogui.keyDown('tab')
pyautogui.keyUp('alt')
pyautogui.keyUp('tab')

while i == 0:
    x = random.randint(736, 776)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.press('tab')
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(636, 676)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(736, 776)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(736, 776)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(336, 376)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)
    speed *= 1.9166

    x = random.randint(536, 576)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(536, 576)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(236, 276)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(236, 276)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(236, 276)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(236, 276)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)
    distance = math.sqrt(math.pow(x - 515, 2) + math.pow(y - 345, 2))
    sleep_time = round(distance / speed, 1)
    sleep(sleep_time)

    x = random.randint(236, 276)
    y = random.randint(547, 587)
    pyautogui.moveTo(x, y, duration=0.5)

    i += 1


mon = {'left': 0, 'top': 0, 'width': 1024, 'height': 768}


def black_finder():
    with mss() as sct:
        while True:
            cv.imwrite('pictures/screen1.jpg', np.array(sct.grab(mon)))
            first = cv.imread('pictures/screen1.jpg', cv.IMREAD_UNCHANGED)
            second = cv.imread('pictures/black_screen.png', cv.IMREAD_UNCHANGED)

            result = cv.matchTemplate(first, second, cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            global maximum_black
            global test_black
            maximum_black = max_val
            test_black = max_loc
            break


while maximum_black < 0.95:
    black_finder()


sleep(4)




