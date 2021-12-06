'''
- Create a list comprehension that squares even arguments, and adds 1 to and squares odd arguments

- Test on my_list

my_list = [34,52,71,39,22,73,92]
'''
my_list = [34,52,71,39,22,73,92]

list_compreh_even = [i**2 for i in my_list if i % 2 == 0]
list_compreh_odd = [(i**2 + 1) for i in my_list if i % 2 != 0]
print(list_compreh_even)
print(list_compreh_odd)

list_compreh = [i**2 for i in my_list if i % 2 == 0] + [(i**2 + 1) for i in my_list if i % 2 != 0]
print(list_compreh)    #concatinating the two comprehension list looks the best approach to get the task done,
                       #as list comprehension can only take one condition ==> newlist = [expression for item in iterable if condition == True]














