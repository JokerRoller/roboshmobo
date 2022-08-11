import pyautogui
import random
from time import sleep
import math
from mss import mss
import cv2 as cv
import numpy as np

# sleep_time2 = 0
# break_point = 1
# i = 1
# mon = {'left': 0, 'top': 0, 'width': 1024, 'height': 768}
# mouse = 0.1
# mouse2 = 0.1
# speed = 460 # or 420 or 470
# gallop1 = 1
# scale = 1


class MovementClass:

    def __init__(self, sleep_time2, break_point, i, mon, mouse, mouse2, speed, gallop1, scale):
        self.sleep_time2 = sleep_time2
        self.break_point = break_point
        self.i = i
        self.mon = mon
        self.mouse = mouse
        self.mouse2 = mouse2
        self.speed = speed  # or 420 or 470
        self.gallop1 = gallop1
        self.scale = scale

    def gallop(self):
        with mss() as sct:
            while True:
                mon2 = {'left': 30, 'top': 50, 'width': 200, 'height': 100}
                cv.imwrite('../picture_variables/gallop.jpg', np.array(sct.grab(mon2)))
                haystack_img2 = cv.imread('../picture_variables/gallop.jpg', cv.IMREAD_UNCHANGED)
                needle_img2 = cv.imread('../pictures/gallop_icon.png', cv.IMREAD_UNCHANGED)
                result = cv.matchTemplate(haystack_img2, needle_img2, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                needle_w2 = needle_img2.shape[1]
                needle_h2 = needle_img2.shape[0]
                top_left = max_loc
                bottom_right = (top_left[0] + needle_w2, top_left[1] + needle_h2)
                cv.rectangle(haystack_img2, top_left, bottom_right,
                             color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
                return max_val
                break

    def black_screen(self):
        with mss() as sct:
            while True:
                mon2 = {'left': 0, 'top': 0, 'width': 1024, 'height': 768}
                cv.imwrite('../picture_variables/screen.jpg', np.array(sct.grab(mon2)))
                haystack_img2 = cv.imread('../picture_variables/screen.jpg', cv.IMREAD_UNCHANGED)
                needle_img2 = cv.imread('../pictures/black_screen.png', cv.IMREAD_UNCHANGED)
                result = cv.matchTemplate(haystack_img2, needle_img2, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                needle_w2 = needle_img2.shape[1]
                needle_h2 = needle_img2.shape[0]
                top_left = max_loc
                bottom_right = (top_left[0] + needle_w2, top_left[1] + needle_h2)
                cv.rectangle(haystack_img2, top_left, bottom_right,
                             color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
                return max_val
                break

    def alt_tab(self):
        pyautogui.keyDown('alt')
        pyautogui.keyDown('tab')
        pyautogui.keyUp('alt')
        pyautogui.keyUp('tab')

    def screen_shot(self, par):
        with mss() as sct:
            while True:
                cv.imwrite('../picture_variables/screen.jpg', np.array(sct.grab(self.mon)))
                haystack_img = cv.imread('../picture_variables/screen.jpg', cv.IMREAD_UNCHANGED)
                needle_img = cv.imread(par, cv.IMREAD_UNCHANGED)
                result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                needle_w = needle_img.shape[1]
                needle_h = needle_img.shape[0]
                top_left = max_loc
                bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
                cv.rectangle(haystack_img, top_left, bottom_right,
                             color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
                print(max_val)
                if max_val > 0.60:
                    pyautogui.press('s')
                    cv.imwrite('../picture_variables/screen.jpg', np.array(sct.grab(self.mon)))
                    haystack_img = cv.imread('../picture_variables/screen.jpg', cv.IMREAD_UNCHANGED)
                    needle_img = cv.imread(par, cv.IMREAD_UNCHANGED)
                    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                    self.sleep_time2 = 0
                    self.break_point = 0
                    pyautogui.moveTo(max_loc[0] + needle_w / 2, max_loc[1] + needle_h / 2, 0.3)
                    pyautogui.click(button='right')
                    distance = math.sqrt(
                        math.pow(max_loc[0] + needle_w / 2 - 515, 2) + math.pow(max_loc[1] + needle_h / 2 - 345, 2))
                    sleep_time = distance / self.speed * self.scale
                    sleep(sleep_time + 0.5)
                break

    def screen_shot2(self, par):
        with mss() as sct:
            while True:
                cv.imwrite('../picture_variables/screen.jpg', np.array(sct.grab(self.mon)))
                haystack_img = cv.imread('../picture_variables/screen.jpg', cv.IMREAD_UNCHANGED)
                needle_img = cv.imread(par, cv.IMREAD_UNCHANGED)
                result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                needle_w = needle_img.shape[1]
                needle_h = needle_img.shape[0]
                top_left = max_loc
                bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
                cv.rectangle(haystack_img, top_left, bottom_right,
                             color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
                print(max_val)
                if max_val > 0.79:
                    pyautogui.press('s')
                    cv.imwrite('../picture_variables/screen.jpg', np.array(sct.grab(self.mon)))
                    haystack_img = cv.imread('../picture_variables/screen.jpg', cv.IMREAD_UNCHANGED)
                    needle_img = cv.imread(par, cv.IMREAD_UNCHANGED)
                    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                    self.sleep_time2 = 0
                    self.break_point = 0
                    pyautogui.moveTo(max_loc[0] + needle_w / 2, max_loc[1] + needle_h / 2, 0.3)
                    pyautogui.click(button='left')
                    distance = math.sqrt(
                        math.pow(max_loc[0] + needle_w / 2 - 515, 2) + math.pow(max_loc[1] + needle_h / 2 - 345, 2))
                    sleep_time = distance / self.speed * self.scale
                    sleep(sleep_time + 0.5)
                break

    def screen_shot_night(self, par):
        with mss() as sct:
            while True:
                cv.imwrite('../picture_variables/screen.jpg', np.array(sct.grab(self.mon)))
                haystack_img = cv.imread('../picture_variables/screen.jpg', cv.IMREAD_UNCHANGED)
                needle_img = cv.imread(par, cv.IMREAD_UNCHANGED)
                result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                needle_w = needle_img.shape[1]
                needle_h = needle_img.shape[0]
                top_left = max_loc
                bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
                cv.rectangle(haystack_img, top_left, bottom_right,
                             color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
                print(max_val)
                if max_val > 0.60:
                    pyautogui.press('s')
                    cv.imwrite('../picture_variables/screen.jpg', np.array(sct.grab(self.mon)))
                    haystack_img = cv.imread('../picture_variables/screen.jpg', cv.IMREAD_UNCHANGED)
                    needle_img = cv.imread(par, cv.IMREAD_UNCHANGED)
                    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                    self.sleep_time2 = 0
                    self.break_point = 0
                    pyautogui.moveTo(max_loc[0] + needle_w / 2, max_loc[1] + needle_h / 2, 0.3)
                    pyautogui.click(button='right')
                    distance = math.sqrt(math.pow(max_loc[0] + needle_w / 2 - 515, 2) + math.pow(max_loc[1] + needle_h / 2 - 345, 2))
                    sleep_time = distance / self.speed * self.scale
                    sleep(sleep_time + 0.5)
                break

    def screen_shot_night2(self, par):
        with mss() as sct:
            while True:
                cv.imwrite('../picture_variables/screen.jpg', np.array(sct.grab(self.mon)))
                haystack_img = cv.imread('../picture_variables/screen.jpg', cv.IMREAD_UNCHANGED)
                needle_img = cv.imread(par, cv.IMREAD_UNCHANGED)
                result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                needle_w = needle_img.shape[1]
                needle_h = needle_img.shape[0]
                top_left = max_loc
                bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
                cv.rectangle(haystack_img, top_left, bottom_right,
                             color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
                print(max_val)
                if max_val > 0.60:
                    pyautogui.press('s')
                    cv.imwrite('../picture_variables/screen.jpg', np.array(sct.grab(self.mon)))
                    haystack_img = cv.imread('../picture_variables/screen.jpg', cv.IMREAD_UNCHANGED)
                    needle_img = cv.imread(par, cv.IMREAD_UNCHANGED)
                    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                    self.sleep_time2 = 0
                    self.break_point = 0
                    pyautogui.moveTo(max_loc[0] + needle_w / 2, max_loc[1] + needle_h / 2, 0.3)
                    pyautogui.click(button='left')
                    distance = math.sqrt(math.pow(max_loc[0] + needle_w / 2 - 515, 2) + math.pow(max_loc[1] + needle_h / 2 - 345, 2))
                    sleep_time = distance / self.speed * self.scale
                    sleep(sleep_time + 0.5)
                break


    def movement(self, z, a):
        # x = random.randint(z - 0, z + 0)
        # y = random.randint(a - 0, a + 0)
        pyautogui.moveTo(z, a, self.mouse)
        pyautogui.click(button='right')
        distance = math.sqrt(math.pow(z - 515, 2) + math.pow(a - 345, 2))
        self.sector(z, a)
        sleep_time = distance / self.speed * self.scale
        sleep(sleep_time - self.mouse2)
        print(self.i)
        if self.gallop() < 0.55 and self.gallop1 == 1:
            self.speed /= 1.5
            self.gallop1 = 0
            print(f'Slowed {self.gallop()}')
            sleep(sleep_time)
        if self.gallop() > 0.55 and self.gallop1 == 0:
            print(f'Fast {self.gallop()}')
            self.speed *= 1.5
            self.gallop1 = 1
        self.i += 1
        self.scale = 1

    def sector(self, x, y):
        if x < 515 and x > 295 and y < 345 and y > 125 and 515-x > 345 - y:
            # A
            self.scale = 1.75
            print('A')
        elif x < 515 and x > 295 and y < 345 and y > 125 and 515 - x < 345 - y:
            # B
            self.scale = 2
            print('B')
        elif x > 515 and x < 735 and y < 345 and y > 125 and x - 515 < 345 - y:
            # C
            self.scale = 2.2
            print('C')
        elif x > 515 and x < 735 and y < 345 and y > 125 and x - 515 > 345 - y:
            # D
            self.scale = 1.55
            print('D')
        elif x > 515 and x < 735 and y > 345 and y < 565 and x - 515 > y - 345:
            # E
            self.scale = 1.2
            print('E')
        elif x > 515 and x < 735 and y > 345 and y < 565 and x - 515 < y - 345:
            # F
            self.scale = 1.2
            print('F')
        elif x < 515 and x > 295 and y > 345 and y < 565 and 515 - x < y - 345:
            # G
            self.scale = 1.2
            print('G')
        elif x < 515 and x > 295 and y > 345 and y < 565 and 515 - x > y - 345:
            # L
            self.scale = 1.2
            print('L')
        else:
            self.scale = 1
            self.scale = 1

    def movement2(self, z, a, par3, par4):
        # x = random.randint(z - 0, z + 0)
        # y = random.randint(a - 0, a + 0)
        pyautogui.moveTo(z, a, self.mouse)
        pyautogui.click(button='right')
        distance = math.sqrt(math.pow(z - 515, 2) + math.pow(a - 345, 2))
        self.sleep_time2 = distance / self.speed * self.scale
        while self.sleep_time2 > 0:
            self.screen_shot(par3)
            self.screen_shot_night(par4)
            self.sleep_time2 -= 0.5
        print(z, a)

    def movement3(self, z, a, par3, par4):
        # x = random.randint(z - 0, z + 0)
        # y = random.randint(a - 0, a + 0)
        pyautogui.moveTo(z, a, self.mouse)
        pyautogui.click(button='right')
        distance = math.sqrt(math.pow(z - 515, 2) + math.pow(a - 345, 2))
        self.sleep_time2 = distance / self.speed * self.scale
        while self.sleep_time2 > 0:
            self.screen_shot2(par3)
            self.screen_shot_night2(par4)
            self.sleep_time2 -= 1.5
        print(z, a)


    def search_move(self, par2, par_night):
        self.screen_shot(par2)
        if self.break_point > 0:
            self.screen_shot_night(par_night)
        if self.break_point > 0:
            self.movement2(406, 424, par2, par_night)
        if self.break_point > 0:
            self.movement2(414, 419, par2, par_night)
        if self.break_point > 0:
            self.movement2(427, 402, par2, par_night)
        if self.break_point > 0:
            self.movement2(442, 293, par2, par_night)
        if self.break_point > 0:
            self.movement2(432, 277, par2, par_night)
        if self.break_point > 0:
            self.movement2(619, 306, par2, par_night)
        if self.break_point > 0:
            self.movement2(625, 298, par2, par_night)
        if self.break_point > 0:
            self.movement2(598, 403, par2, par_night)
        if self.break_point > 0:
            self.movement2(602, 442, par2, par_night)
        if self.break_point > 0:
            self.movement2(613, 446, par2, par_night)
        if self.break_point > 0:
            self.movement2(592, 430, par2, par_night)
        if self.break_point > 0:
            self.movement2(424, 421, par2, par_night)
        if self.break_point > 0:
            self.movement2(417, 412, par2, par_night)
        if self.break_point > 0:
            self.movement2(438, 305, par2, par_night)
        if self.break_point > 0:
            self.movement2(424, 290, par2, par_night)
        if self.break_point > 0:
            self.movement2(588, 305, par2, par_night)
        if self.break_point > 0:
            self.movement2(608, 438, par2, par_night)
        self.break_point = 1
        self.i += 1

    def search_move2(self, par2, par_night):
        self.screen_shot2(par2)
        if self.break_point > 0:
            self.screen_shot_night2(par_night)
        if self.break_point > 0:
            self.movement3(406, 424, par2, par_night)
        if self.break_point > 0:
            self.movement3(414, 419, par2, par_night)
        if self.break_point > 0:
            self.movement3(427, 402, par2, par_night)
        if self.break_point > 0:
            self.movement3(442, 293, par2, par_night)
        if self.break_point > 0:
            self.movement3(432, 277, par2, par_night)
        if self.break_point > 0:
            self.movement3(619, 306, par2, par_night)
        if self.break_point > 0:
            self.movement3(625, 298, par2, par_night)
        if self.break_point > 0:
            self.movement3(598, 403, par2, par_night)
        if self.break_point > 0:
            self.movement3(602, 442, par2, par_night)
        if self.break_point > 0:
            self.movement3(613, 446, par2, par_night)
        if self.break_point > 0:
            self.movement3(592, 430, par2, par_night)
        if self.break_point > 0:
            self.movement3(424, 421, par2, par_night)
        if self.break_point > 0:
            self.movement3(417, 412, par2, par_night)
        if self.break_point > 0:
            self.movement3(438, 305, par2, par_night)
        if self.break_point > 0:
            self.movement3(424, 290, par2, par_night)
        if self.break_point > 0:
            self.movement3(588, 305, par2, par_night)
        if self.break_point > 0:
            self.movement3(608, 438, par2, par_night)
        self.break_point = 1

