import numpy as np
import cv2 as cv
from mss import mss
from PIL import Image
# Position and size of screencapture
mon = {'left': 0, 'top': 0, 'width': 1024, 'height': 768}

# Non stop take screenshot and show-s it as video
# with mss() as sct:
#     while True:
#         screenShot = sct.grab(mon)
#         img = Image.frombytes(
#             'RGB',
#             (screenShot.width, screenShot.height),
#             screenShot.rgb,
#         )
#         cv2.imshow('test', np.array(img))
#         if cv2.waitKey(1) & 0xFF in (
#             ord('q'),
#             27,
#         ):
#             break

# Non stop takes screenshots and save it as a file "screen.jpg"


def testfunction():
    with mss() as sct:
        while True:
            cv.imwrite('screen.jpg', np.array(sct.grab(mon)))
            break

