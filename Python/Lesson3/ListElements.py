'''
1. Create a list of five elements with a different data type. Name it *list_1*

2. Now create a list with ten zeros, do it using the '*' operator. Name it *list_2*

3. Nest *list_1* and *list_2* into a new list and name it *list_3*

4. Access the fourth element of both lists in *list_3* and store the elements in *list_4*
'''

list_1 = ['True','0.99','green','(5,6)','???']
list_2 = [0] * 10
list_3 = [list_1,list_2]
list_4 = [list_3[0][3],list_3[1][3]]

print(list_1)
print(list_2)
print(list_3)
print(list_4)