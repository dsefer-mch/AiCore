"""
Write a program to check whether each number from 10 to 50 is prime

Your answer should take the following format:

- "x IS a prime number." for primes

- "x IS NOT a prime number because y is a factor of x." for non-primes

CLUE: This is possible using a while loop nested in a for loop or using a nested for loop; if you can, try to find both.
"""

for i in range(10,50):
    if i % 2 == 0:
        print(f'{i} is not a prime number, because 2 is a factor of {i}')
        continue
    if i % 3 == 0:
        print(f'{i} is not a prime number, because 3 is a factor of {i}')
        continue
    if i % 5 == 0:
        print(f'{i} is not a prime number, because 5 is a factor of {i}')
        continue
    if i % 7 == 0:
        print(f'{i} is not a prime number, because 7 is a factor of {i}')
        continue
    else:
        print(f'{i} is a prime number')
        