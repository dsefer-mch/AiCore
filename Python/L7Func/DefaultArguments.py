"""
- Create a function which takes in a dictionary of attributes about a piece of clothing and prints each of the key-value pairs on a line

- Define an input to the function called attributes_to_print with a default value of 'all'

- If a list is passed into the function as the attributes_to_print, print only the key-value pairs of the dictionary which the key appears for in that list

- Print a message to tell the user if a key doesn't exist

- Call your function to test it
"""

def Clothing(attributes_to_print = "all",**kwargs):
    if attributes_to_print == "all":
        print(kwargs.items())
    else:
        for item in attributes_to_print:
            if item in kwargs:
                print(item,'           :', kwargs[item])
            else:
                print(f"key >{item}< doesn't exist")



cloth_dict = {
    'polo' : 23.50 ,
    'jumper' : 29.99,
    'puffer coat' : 42.99,
    'coat' : 66.99,
    'jacket' : 59.99,
    'joggers' : 14.99,
    'cropped top' : 17.99,
    'shirt' : 8.99,
    'jeans' :24.99,
}

#Clothing(**cloth_dict)
clot_list = ['jacket', 'jeans', 'hat', 'coat', 'gloves']
Clothing(clot_list, **cloth_dict)






