"""
- Write a function called in_range which takes in a lower bound, an upper bound, and a number

- If it is, return "<number> is between <lower bound> and <upper bound>."

- If it isn't, return "<number> is NOT between <lower bound> and <upper bound>."

- Call your function to test it
"""

def in_range(lower_bond, upper_bond, number):
    if lower_bond < number <upper_bond:
        return print(f"{number} is between {lower_bond} and {upper_bond}")
    else:
        return print(f"{number} is NOT between {lower_bond} and {upper_bond}")



in_range(9,15,8)


