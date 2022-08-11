import pyautogui
import random
from time import sleep
import math
import cv2 as cv
from mss import mss
import numpy as np
from PIL import Image

# global variable
H_low = 96
H_high = 109
S_low = 93
S_high = 217
V_low = 103
V_high = 255

# trackbar callback fucntion to update HSV value
# def callback(x):
#     global H_low, H_high, S_low, S_high, V_low, V_high
#     # assign trackbar position value to H,S,V High and low variable
#     H_low = cv.getTrackbarPos('low H', 'controls')
#     H_high = cv.getTrackbarPos('high H', 'controls')
#     S_low = cv.getTrackbarPos('low S', 'controls')
#     S_high = cv.getTrackbarPos('high S', 'controls')
#     V_low = cv.getTrackbarPos('low V', 'controls')
#     V_high = cv.getTrackbarPos('high V', 'controls')
#
#
# # create a seperate window named 'controls' for trackbar
# cv.namedWindow('controls', 2)
# cv.resizeWindow("controls", 550, 10)
#
# # create trackbars for high,low H,S,V
# cv.createTrackbar('low H', 'controls', 0, 179, callback)
# cv.createTrackbar('high H', 'controls', 179, 179, callback)
#
# cv.createTrackbar('low S', 'controls', 0, 255, callback)
# cv.createTrackbar('high S', 'controls', 255, 255, callback)
#
# cv.createTrackbar('low V', 'controls', 0, 255, callback)
# cv.createTrackbar('high V', 'controls', 255, 255, callback)


mon = {'left': 362, 'top': 184, 'width': 350, 'height': 350}

with mss() as sct:
    while True:
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB',
            (screenShot.width, screenShot.height),
            screenShot.rgb,
        )
        img_hsv = cv.cvtColor(np.array(img), cv.COLOR_BGR2HSV)
        hsv_low = np.array([H_low, S_low, V_low], np.uint8)
        hsv_high = np.array([H_high, S_high, V_high], np.uint8)
        mask = cv.inRange(img_hsv, hsv_low, hsv_high)
        res = cv.bitwise_and(np.array(img), np.array(img), mask=mask)
        # road_fragment = cv.imread('some.png', cv.IMREAD_UNCHANGED)
        # result = cv.matchTemplate(res, road_fragment, cv.TM_CCOEFF_NORMED)
        # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # road_fragment_w = road_fragment.shape[1]
        # road_fragment_h = road_fragment.shape[0]
        # top_left = max_loc
        # bottom_right = (top_left[0] + road_fragment_w, top_left[1] + road_fragment_h)
        # cv.rectangle(mask, top_left, bottom_right,
        #                 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
        cv.imshow('test', res)
        # print(max_val)
        if cv.waitKey(1) & 0xFF in (
            ord('q'),
            27,
        ):
            break


