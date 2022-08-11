import pyautogui
import random
from time import sleep
import cv2 as cv
from mss import mss
import numpy as np
from PIL import Image
import math

mon = {'left': 0, 'top': 0, 'width': 1024, 'height': 768}

with mss() as sct:
    while True:
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB',
            (screenShot.width, screenShot.height),
            screenShot.rgb,
        )
        img_hsv = cv.cvtColor(np.array(img), cv.COLOR_BGR2HSV)
        low_red = np.array([95, 140, 140])
        high_red = np.array([105, 255, 255])
        red_mask = cv.inRange(img_hsv, low_red, high_red)
        red = cv.bitwise_and(np.array(img), np.array(img), mask=red_mask)
        cv.imshow('test', red)
        if cv.waitKey(1) & 0xFF in (
            ord('q'),
            27,
        ):
            break


