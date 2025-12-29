# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 23:47:23 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
#Decorators don’t have to wrap the function they’re decorating. 
#They can also simply register that a function exists and return it unwrapped.
#This can be used, for instance, to create a light-weight plug-in architecture:
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
#The @register decorator simply stores a reference to the decorated function in the 
#global PLUGINS dict. Note that you do not have to write an inner function or 
#use @functools.wraps in this example because you are returning the original function unmodified.
#The randomly_greet() function randomly chooses one of the registered functions to use. 
#Note that the PLUGINS dictionary already contains references to each function object that is registered as a plugin:
#>>> PLUGINS
#{'say_hello': <function say_hello at 0x7f768eae6730>,
# 'be_awesome': <function be_awesome at 0x7f768eae67b8>}

#>>> randomly_greet("Alice")
#Using 'say_hello'
#'Hello Alice'

#The main benefit of this simple plugin architecture is that you do not need to maintain a list of which plugins exist.
#That list is created when the plugins register themselves. 
#This makes it trivial to add a new plugin: just define the function and decorate it with @register.

#If you are familiar with globals() in Python, you might see some similarities to how the plugin architecture works.
#globals() gives access to all global variables in the current scope, including your plugins:

