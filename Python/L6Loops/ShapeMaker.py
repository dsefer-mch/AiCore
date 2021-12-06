"""
Write a program to produce the following pattern.

CLUE: Use nested for loops, using one nested loop to increase in size and another to decrease.

Start with n=5

*

* *

* * *

* * * *

* * * * *

* * * *

* * *

* *

*
"""
j = 4
for i in range(10):
    if i <= 5:
        print(i*'*')
    else:
        print(j*'*')
        j = j -1
        
        
