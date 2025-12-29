# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:57:49 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""

import tkinter as tk
window = tk.Tk()

#greeting.pack()
#label = tk.Label(text="Hello, Tkinter", background="#34A2FE")
#label = tk.Label(text="Hello, Tkinter", fg="white", bg="black")
frame = tk.Frame()
frame.pack()

frame_a = tk.Frame()
frame_b = tk.Frame()


label = tk.Label(master=frame_b,
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
entry = tk.Entry(fg="yellow", bg="blue", width=50)
name = entry.get()
text_box = tk.Text(master=frame_a)
text_box.pack()
frame_a.pack()

frame_b.pack()
#Up until now, you’ve been adding widgets to windows and Frame widgets using
# .pack(),
#but you haven’t learned what exactly this method does.
#Let’s clear things up! 
#Application layout in Tkinter is controlled with geometry managers.
#While .pack() is an example of a geometry manager, it isn’t the only one.
#Tkinter has two others:
#.place()
#.grid()
#The .pack() geometry manager uses a packing algorithm to place widgets in a Frame or window in a specified order. 
#For a given widget, the packing algorithm has two primary steps:
#Compute a rectangular area called a parcel that’s just tall (or wide) enough to hold the widget 
#and fills the remaining width (or height) in the window with blank space.
#Center the widget in the parcel unless a different location is specified.
#.pack() is powerful, but it can be difficult to visualize.
window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


#The geometry manager you’ll likely use most often is .grid(), 
#which provides all the power of .pack() in a format that’s easier to understand and maintain.




#window = tk.Tk()


for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

#.pack() also has padx and pady parameters.
#The following code is nearly identical to the previous code, 
#except that you add five pixels of additional padding around each label in both the x and y directions:
#Each grid cell is 250 pixels wide and 100 pixels tall.
#The labels are placed in the center of each cell, as you can see in the following figure:    
    
    
#By using .columnconfigure() and .rowconfigure() on the window object, 
#you can adjust how the rows and columns of the grid grow as the window is resized.
#Remember, the grid is attached to window, even though you’re calling .grid() on each Frame widget.
#Both .columnconfigure() and .rowconfigure() take three essential arguments:    
#Index: The index of the grid column or row that you want to configure or a list of indices to configure multiple rows or columns at the same time
#Weight: A keyword argument called weight that determines how the column or row should respond to window resizing, relative to the other columns and rows
#Minimum Size: A keyword argument called minsize that sets the minimum size of the row height or column width in pixels
    
    
    
    
    
#The important thing to realize here is that even though .grid()
#is called on each Frame object, the geometry manager applies to the window object. 
#Similarly, the layout of each frame is controlled with the .pack() geometry manager.
#The frames in the previous example are placed tightly next to one another.
#To add some space around each frame, 
#you can set the padding of each cell in the grid. 
#Padding is just some blank space that surrounds a widget and visually sets its content apart.











#window.mainloop()
#The side keyword argument of .pack() specifies on which side of the window the widget should be placed. 
#These are the available options:
#tk.TOP
#tk.BOTTOM
#tk.LEFT
#tk.RIGHT
#If you don’t set side, then .pack() will automatically use tk.TOP 
#To make the layout truly responsive,
#you can set an initial size for your frames using the width and height attributes.
#Then, set the fill keyword argument of .pack() to tk.BOTH and set the expand keyword argument to True:

#You can use .place() to control the precise location that a widget should occupy in a window or Frame.
#You must provide two keyword arguments, x and y,
#which specify the x- and y-coordinates for the top-left corner of the widget. 
#Both x and y are measured in pixels, not text units.









#Now label_b is on top. 
#Since label_b is assigned to frame_b, it moves to wherever frame_b is positioned.
#text_box.get() # to get text from the text box

#An empty Frame widget is practically invisible. 
#Frames are best thought of as containers for other widgets.
# You can assign a widget to a frame by setting the widget’s master attribute:

#Frame widgets can be configured with a relief attribute that creates a border around the frame.
#You can set relief to be any of the following values:
#tk.FLAT: Has no border effect (the default value)
#tk.SUNKEN: Creates a sunken effect
#tk.RAISED: Creates a raised effect
#tk.GROOVE: Creates a grooved border effect
#tk.RIDGE: Creates a ridged effect




#Frame widgets are important for organizing the layout of your widgets in an application.





#To retrieve several characters, you need to pass a start index and an end index.
#The line number of a character
#The position of a character on that line
#Line numbers start with 1, and character positions start with 0.
#To make an index, you create a string of the form "<line>.<char>",
#replacing <line> with the line number and <char> with the character number. 
#For example, "1.0" represents the first character on the first line,
#and "2.3" represents the fourth character on the second line.
#Use the index "1.0" to get the first letter from the text box that you created earlier:
#text_box.get("1.0")
#text_box.get("2.0", "2.5")'World'
#text_box.get("1.0", tk.END) 'Hello\nWorld\n'
#Notice that text returned by .get() includes any newline characters.
# You can also see from this example that every line in a Text widget has a newline character at the end, including the last line of text in the text box.
#Text widgets are used for entering text, just like Entry widgets. 
#The difference is that Text widgets may contain multiple lines of text.
#Retrieve text with .get()
#Delete text with .delete()
#Insert text with .insert()














#entry.delete(0)


#The interesting bit about Entry widgets isn’t how to style them, though.
#It’s how to use them to get input from a user.
#There are three main operations that you can perform with Entry widgets:
#Retrieving text with .get()
#Deleting text with .delete()
#Inserting text with .insert()

#DELTE

#If you need to remove several characters from an Entry, then pass a second integer argument to .delete()
#indicating the index of the character where deletion should stop.
#For example, the following code deletes the first four letters in Entry:
#entry.delete(0, 4)
#Entry.delete() works just like string slicing. 
#The first argument determines the starting index,
#and the deletion continues up to but not including the index passed as the second argument. 
#Use the special constant tk.END for the second argument of .delete() to remove all text in Entry:
#entry.delete(0, tk.END)  
#entry.insert(0, "Python")
entry.pack()

#The window you created earlier doesn’t change. You just created a Label widget,
#but you haven’t added it to the window yet.
# There are several ways to add widgets to a window. Right now, you can use the Label widget’s .pack() method:
label.pack()
button.pack()
window.mainloop()
