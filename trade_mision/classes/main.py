from trade_mision.classes.maps import Maps
from trade_mision.classes.movement import MovementClass
from time import sleep
import pyautogui

search_time = 6


def black():
    global search_time
    while e.black_screen() < 0.8 and search_time > 0:
        print('searching')
        sleep(0.9)
        search_time -= 1

    if search_time < 1:
        print('reset')
        pyautogui.press('r')
        sleep(20)
    if search_time >= 1:
        print('next map')
        sleep(10)
        search_time = 10



m = Maps()
e = MovementClass(0, 1, 6, {'left': 0, 'top': 0, 'width': 1024, 'height': 768}, 0.1, 0.1, 400, 1, 1)

# m.ferndell_exit()
#
# black()
#
# m.willow_wood_exit()
#
# black()
#
# m.spindlewood_exit()
#
# black()
#
# m.longshadow_plain_exit()
#
# black()
#
# m.snapshaft_trough_exit()
#
# black()
#
# m.lazygrass_plain_exit()
#
# black()

m.slowtree_plain_exit_back()

black()

m.lazygrass_plain_back()

black()

m.snapshaft_trough_back()

black()

m.longshadow_plain_back()

black()

m.spindlewood_back()

black()

m.willow_wood_back()

black()

m.ferndell_back()

black()

m.lymhurst_back()