# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:37:55 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

grab_all_variable_command="var all = document.getElementsByTagName('*');"
grab_information_about_each_variable_command="""for (var i = 0, max = all.length; i < max; i++) {
var element = all[i];
var elementName = element.tagName; // This will return the element's tag name in uppercase (e.g., DIV, P, SPAN)
var elementId = element.id; // Get the ID

// Get the position and size of the element using getBoundingClientRect
var rect = element.getBoundingClientRect();

// Extract the values from the rect object
var x = rect.left;      // x-coordinate (distance from left of the viewport)
var y = rect.top;       // y-coordinate (distance from top of the viewport)
var width = rect.width; // Width of the element
var height = rect.height; // Height of the element

// Get the text content of the element
var textContent = element.textContent.trim();  // .trim() removes extra whitespace

// You can now do something with these values, e.g., log them
console.log("Element " + i + " (" + elementName + ")");
console.log("Element " + i + " position: x=" + x + ", y=" + y + ", width=" + width + ", height=" + height);
console.log("Element " + i + " text: " + textContent);
console.log("Element " + i + " ID: " + elementId); }
"""