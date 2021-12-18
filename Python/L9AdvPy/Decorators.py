"""
to start with, create a simple function which we will decorate that loops over the numbers 1 to 3 and prints them 
create a decorator that prints "start" and "end" at the start and end of a function call 
create a decorator to time how long a function takes to run and print the duration 
change your function so that it takes in an argument, which is the upper bound of the range which it iterates to 
create a decorator that takes in a word as an argument, and prints this word before running 
now make it take in a second argument word, which it prints after running the decorated function
"""

def simple_func():

    @start_end
    print('start')