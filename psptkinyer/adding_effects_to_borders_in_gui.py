# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:25:13 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    # can put pack on the same line as the variable to pack it onto the screen
    # ex. frame = tk.Frame(master=window, relief=relief, borderwidth=5).pack()

    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()