"""
1. Create a dictionary with 3 keys

- name: a string of your name

- skills: a list of strings

2. Make another one of these and put both of them in a list

3. Now index that list of dictionaries to find the last letter of the first skill of the last dictionary

4. Create a list comprehension which maps that list to a list of the length of names

5. Add that list together to get the total number of characters in all of the names
"""

the_dict_one = {
    "name" : "Ziben",
    "skills" : ["Doing Nothing","swimming","mooning"]
}

the_dict_two = {
    "name" : "Bayo",
    "skills" : ["building","watching","reading"]
}


list_of_dict = [the_dict_one, the_dict_two]

print(list_of_dict)
print(list_of_dict[-1]["skills"][0][-1])
list_of_lenght_of_names = [len(the_dict_one["name"]), len(the_dict_two["name"])]
list_compreh = [[i, o] for i in list_of_dict for o in list_of_lenght_of_names]
print(list_compreh)