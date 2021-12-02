'''
- Create a list with two names

- Find the characters which appear in every name
'''

list_of_names = ['Simon','Neron']

new_list = [ch for ch in list_of_names[0] if ch in list_of_names[1]]
print(new_list)