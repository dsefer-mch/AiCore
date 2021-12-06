'''
Create a function which checks whether a word is a palindrome or not

- there are several ways to implement this. some require less code, but some are more efficient; which is yours, and can you think of how to implement the other way?
'''

def PalindromeChecker(word):
    if word[::-1] == word:
        return True
    else:
        return False


word = str(input('Enter   a word >>'))
print(PalindromeChecker(word))