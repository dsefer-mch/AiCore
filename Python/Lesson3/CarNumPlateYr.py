'''
- Given the following list of number plates: ["G06 WTR", "WL11 WFL", "QW68 PQR"]

- Extract the last two characters, which represent the year of the car

- Print the type of each of them

- Convert each of these years to an integer type

'''

num_plates = ["G06 WTR", "WL11 WFL", "QW68 PQR"]

print(type(num_plates[0][1:3]))
print(type(num_plates[1][2:4]))
print(type(num_plates[2][2:4]))

f = int(num_plates[0][1:3])
s = int(num_plates[1][2:4])
t = int(num_plates[2][2:4])

print(type(f))
print(type(s))
print(type(t))
