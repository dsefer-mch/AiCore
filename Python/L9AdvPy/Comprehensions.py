"""
for each challenge switch person 
use a list comprehension to capitalise every element in the list ['Hello', 'world'] 
use a list comprehension to filter out every multiple of 5 from a range of numbers up to 100 
use a dictionary comprehension to create a map between every integer up to 15 and it's value squared now, 
use a dictionary comprehension to create a dictionary that does the inverse! (hint: iterate over squares.items(), where squares is the name of the dict you made in the above challenge) 
create a list of dictionaries, each with a key called name, then use a list comprehension to map that list to the names themselves by indexing the dicts 
use the os module to create a nested list comprehension to list every file in the my_lib directory
"""

list = ['Hello', 'world']
capital_list = ([word.upper() for word in list])
print(capital_list)

list_range = [x for x in range(100) if x % 5 == 0]
print(list_range)

dict_comp = {key: key**2 for key in range(1, 16)}
print(dict_comp)

dict_comp_inverse = {key**2: key for key in dict_comp}
print(dict_comp_inverse)

list_of_dict = [{'name': 'Ivan'}, {'name': 'Harry'}, {'name': 'Matin'}, {
    'name': 'Ian'}, {'name': 'Ross'}, {'name': 'Nikol'}]

comp_dict = [ {i : list_of_dict[i-1]['name']} for i in range(1,len(list_of_dict)+1) ]
print(comp_dict)
