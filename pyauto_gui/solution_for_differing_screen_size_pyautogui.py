# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 02:55:55 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

import pyautogui
import os
from pyvirtualdisplay.display import Display
import Xlib.display
#import pyautogui
#pyautogui.size()
# need to set up virtual display for screen differing
#from pyvirtualdisplay import Display
#with Display() as disp:
    # display is active
#    print(disp.is_alive()) # True
# display is stopped
#print(disp.is_alive()) # False


disp = Display(visible=True, size=(1920,1080), backend="xvfb", use_xauth=True)
disp.start()

pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])