"""
Filter shop_dict using list comprehension to find only items with values of over 1.00

Assign them to a list called filtered_shop by their full names, not their codes, using names_dict.

"""

shop_dict = {
    "tom":0.87,
    "sug":1.09,
    "ws":0.29,
    "cc":1.89,
    "ccz":1.29
    }

names_dict = {
    "tom":"Tomatoes",
    "sug":"Sugar",
    "ws":"Washing Sponges",
    "cc":"Coca-Cola",
    "ccz":"Coca-Cola Zero"
    }

list_compreh = [key for key in shop_dict if shop_dict[key] > 1.00]
print(list_compreh)
filtered_shop = [names_dict[item] for item in names_dict and list_compreh]
print(filtered_shop)