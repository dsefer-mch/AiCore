"""
#1. Print the length of the word:

#long_word = 'Pneumonoultramicroscopicsilicovolcanoconiosis'

"""

long_word = 'Pneumonoultramicroscopicsilicovolcanoconiosis' 
print(len(long_word))                              #len() - counts the characters within the string

"""
#2. Access the first letter of long_word by indexing the variable and assign it to first_c. 
#Access the last letter of long_word and assign it to last_c. 
#Use an arithmetic operator to append last_c to first_c and print the result.
"""

first_c = long_word[0]
last_c = long_word[-1]

print(first_c + last_c)                   #concatination
