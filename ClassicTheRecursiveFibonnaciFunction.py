"""
Create a function which takes in an integer n, and when called, returns a list of the first n Fibonnaci numbers. 
It should be a recursive function which calls itself inside the function body.
"""
#import sys
#print(sys.getrecursionlimit())


F = [0, 1]

def FibonnaciSeries(number):
    if number > 1:
        if F[-1] < number > F[-1] + F[-2]:
            F.append(F[-1] + F[-2])
            FibonnaciSeries(number)
        else:
            return F
    elif number == 0:
        return F.append(0)
    elif number == 1:
        return F.append([0,1])    
    



number = int(input('Please enter a positive number: '))
FibonnaciSeries(number)
print(F)