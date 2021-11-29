"""       You have two variables:
          a = 42
          b = 25
 1. Print the sum of a and b
 2. Print the difference of a and b
 3. Print the product of a and b
 4. Print the division of a by b
    Now a = 4.2
 5. Print the type of a + b. Why does this happen?"""

a = 42
b = 25
 
print(a + b)
print(a - b)
print(a * b)
print(a / b)
a = 4.2
print(type(a + b))   #in Python the result inheritate
                     #the type <float> over <int>
                     #when the operators are mixed 
                