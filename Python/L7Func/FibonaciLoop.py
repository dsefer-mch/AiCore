"""
1. Write a for loop that prints the first 100 Fibonnaci numbers

2. Create a function which returns true if the number is a multiple of 7 and false otherwise

3. Call this function on each number inside your loop

4. Add an elif condition to the loop to call another new function which checks if the number is greater than or equal to 100 OR is less than 50.
   In the case that it is true, format a string that prints the number and either "is larger than 100" or "is less than 50"
"""

def Fib_multiples_of_seven(num):
    if num % 7 == 0:
        return True
    else:
        return False
        



def Range_check(num):
    if num >= 100 or num < 50:
        return True
    else:
        return False




F = [0,1]
for i in range(100):
    F.append(F[-1] + F[-2])
    if Fib_multiples_of_seven(F[-1]) == True and 100 <= Range_check(F[-1]) < 50:
        print(f"{F[-1]} is multiple of 7 and is larger than 100 or is less than 50")
    elif Fib_multiples_of_seven(F[-1]) == True and 100 > Range_check(F[-1]) > 50:
        print(f"{F[-1]} is multiple of 7")
    else:
        print(f"{F[-1]} is NOT multiple of 7")
    


