# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 05:15:42 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""

import tkinter as tk
root = tk.Tk() # create a Tk root window

w = 500 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/4) - (w/4)
y = (hs/3) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.mainloop() # starts the mainloop
 def open_psp_window_in_specific_location(self,problem_window_name,location=[]):
     """ """
     import tkinter as tk
     root = tk.Tk() # create a Tk root window

     w = 800 # width for the Tk root
     h = 650 # height for the Tk root

     # get screen width and height
     ws = root.winfo_screenwidth() # width of the screen
     hs = root.winfo_screenheight() # height of the screen

     # calculate x and y coordinates for the Tk root window
     x = (ws/2) - (w/2)
     y = (hs/2) - (h/2)

     # set the dimensions of the screen 
     # and where it is placed
     root.geometry('%dx%d+%d+%d' % (w, h, x, y))

     root.mainloop() # starts the mainloop

