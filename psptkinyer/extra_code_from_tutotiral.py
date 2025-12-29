# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:17:13 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

print("""
text_box = tk.Text()

#frame.grid(row=i, column=j, padx=5, pady=5)
#btn_decrease = tk.Button(master=frame, text="-", command=decrease)
#btn_decrease.grid(row=0, column=0, sticky="nsew")
#lbl_value = tk.Label(master=frame, text="0")
#lbl_value.grid(row=0, column=1)
#btn_increase = tk.Button(master=frame, text="+", command=increase)
#btn_increase.grid(row=0, column=2, sticky="nsew")
#continue

# example of button
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

#example of label
label = tk.Label(master=frame_b,
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10)



# example application fo command
import tkinter as tk
def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)

btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)

btn_increase.grid(row=0, column=2, sticky="nsew")



# example of bind
def handle_keypress(event):
    Print the character associated to the key pressed
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()

# can bind to any  widget
def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)
""")