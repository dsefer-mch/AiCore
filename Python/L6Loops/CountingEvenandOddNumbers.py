'''Write a for loop to count how many even and odd numbers between 1 and 100.'''

even_num = 0
odd_num = 0
i = 1


while i <= 100 :
    if i % 2 == 0 :
        even_num += 1
    else:
        odd_num +=1
    i += 1

print(even_num)
print(odd_num)
