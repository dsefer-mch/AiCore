"""
Define a recursive function called "inverse" that returns the inverse of a string
"""
inversed_str = []

def inverse(string):
    if type(string) == str:
        inverse(list(string))
    else:
        if string != []:
            inversed_str.append(string.pop())
            inverse(string)
        elif string == []:
            return print(''.join(inversed_str))




inverse("?ti t'nsI .dohtem )(tnioj.>rts< a fo elpmaxe taerG a s'tahT")


