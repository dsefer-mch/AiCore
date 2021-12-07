"""
Define a recursive function called "factorial" that returns the factorial of a given number.
"""

def Factorial(number):
    f = 1
    for i in range(1,number+1):
        f *= i
    return print(f)

Factorial(34)