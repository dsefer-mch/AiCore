"""
Create a function which takes in a list of words and returns the total number of characters in the list, then type the function's inputs and outputs
"""

def char_counter(list):
    count = 0
    for elements in list:
        for ch in elements:
            count +=1
    return count




list_of_str = ['gmd',' kdi','lod-',' ']
result = char_counter(list_of_str)
print(result)
print(type(list_of_str))
print(type(result))


