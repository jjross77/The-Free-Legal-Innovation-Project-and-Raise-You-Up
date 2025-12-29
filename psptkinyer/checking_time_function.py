# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:28:31 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


    
#example usage
#@timer
#def waste_some_time(num_times):
#    for _ in range(num_times):
#        sum([i**2 for i in range(10000)])

#@repeat(num_times=4)
#def greet(name):
#    print(f"Hello {name}")
#can add arguments to decorators

# need to learn decorators
# need to learn about type hints
# could wrap functions with mutliprocessing wrapper

# need to keep a place to find all pieces of code i should remember like the __ thing to find the location of a 
#def time_counter():

#def my_decorator(func):
#    @functools.wraps(func)
#    def wrapper(*args, **kwargs):
#        print("Something is happening before the function is called.")
#        func(*args, **kwargs)
#        return func(*args, **kwargs)
#        print("Something is happening after the function is called.")
#    return wrapper

#@my_decorator
#def say_whee():
#    print("Whee!")
#print(say_whee())

#from decorators import my_decorator
#@my_decorator
#def say_whee():
#    print("Whee!")   
#print(say_whee())
    

#import functools
# good boiler plate template for building more complex decorators
#def decorator(func):
#    @functools.wraps(func)
#    def wrapper_decorator(*args, **kwargs):
        # Do something before
#        value = func(*args, **kwargs)
        # Do something after
#        return value
#    return wrapper_decorator