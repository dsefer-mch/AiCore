""""
iterate through each of the following generators to test them 
create generator and iterate through it to infinitely cycle through a list of items in order cast it to a list to print it 
create a generator that generates random numbers 
create a generator that takes in two numbers and generates all multiples of 3 between the two of them 
create a generator that generates the square of every number up to 100, if that number is even or is a multiple of 3 turn the above generator into a generator 
comprehension 
create a generator that generates generators which each generate ranges up to a random number passed to them as an argument :o 
create a double nested for loop the outer loop should iterate through the outer generator the inner loop should iterate through the range generated by the 
inner generator
"""


def gene(n):
    while True:
        for i in range(n):
            yield i

g = gene(15)
for g in range(100):
    next(g)