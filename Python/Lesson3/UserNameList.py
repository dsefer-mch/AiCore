'''
- Create a list of usernames

- Print the type of the list

- print the length of the list

- Print the type of the first list item

- Find the length of the last name
'''

user_name_list = ['Mileti','Basil','Martin','Harry','Anton','Anatoly','Ed','Ewan']
print('The user name list type is: ',type(user_name_list))
print('The lenght of the user name list is ',len(user_name_list),'names long')
print('The first name in the list is: ',user_name_list[0])
last_name_len = len(user_name_list[-1])
print("In case you want the lenght of the last user's name. It's: ",last_name_len)