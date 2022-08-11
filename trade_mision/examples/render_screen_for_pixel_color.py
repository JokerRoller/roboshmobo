import pyautogui

color = (97, 179, 255)

s = pyautogui.screenshot()

for x in range(s.width):
    for y in range(s.height):
        if s.getpixel((x, y)) == color:
            pyautogui.moveTo(x, y)  # do something here
            print(range(s.width))


