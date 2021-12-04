'''
- You have one variable x = 10.

- Use the function input() to ask the user to introduce a number and store it into n.

- Print n is greater than 10 if the introduced number is greater than x
'''

x = 10
n = input('Please introduce a number: ')
if int(n) > x:
    print(n,'is greater than 10')
