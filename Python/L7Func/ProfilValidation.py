"""
- Create a function which takes in the name, age, and email of a user trying to create a new profile on our application

- Check the name does not contain any of "!@£$%^&*()"

- Check the email is valid by making sure it contains "@"

- Check the age > 12

- Turn each step above into a function, so that you have one function, which calls 3 other functions inside

- Print a friendly error to explain the issue to the user if any of these checks does not pass
"""


def Name(name):
    for ch in name:
        if ch in '!@£$%^&*()':
            print('Your name appear to have a forbiden character.Please start all over.')
            return None
    return name



def Age(age):
    if int(age) < 12:
        print('You are under age, buddy :) ')
    else:
        return age



def Mail(email):
    if '@' not in email:
        print('You have typed invallid email-address.Please start all over.')
    else:
        return email



def Validation(name, age, email):
    print(Name(name))
    print(Age(age))
    print(Mail(email))
    if Name(name) == None or Age(age) == None or Mail(email) == None:
        print('Try again!')
    else:
        print('Thanks for login!')




name  = input('Please enter Your name: ')
age   = input('Please enter Your age: ')
email = input('Please enter Your email-address: ')
Validation(name, age, email)