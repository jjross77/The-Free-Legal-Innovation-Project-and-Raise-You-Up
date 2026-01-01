# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:46:28 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""

from pynput import mouse
import pyautogui
import time
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released


# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
print('meow')
time.sleep(0.5)
pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad) 
pyautogui.click()
pyautogui.click()
print('hi')
input()
