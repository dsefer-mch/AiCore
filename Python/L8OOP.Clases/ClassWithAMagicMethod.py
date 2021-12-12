"""
create a class called Vector define its initialiser which takes in a list of numbers
create an instance of the vector use the __repr__ method to define what is printed when we print the object
create another vector instance define how you add two vectors together define how you index an item in the vector
(bonus) define how you measure whether it is greater than another vector (use Pythagoras theorem)
use the function you defined in the question above
"""


class Vector:
    def __init__(self, *args):
        self.vector = list(args)
        self.offset = 0

    # this func transforms a class instance into a list type
    def __getitem__(self):
        for i in range(len(self.vector)):
            return self.vector

    def __repr__(self):
        return str(self.vector)

    def __add__(self, another_vector):
        sum_vector = []
        another_vector = another_vector.__getitem__()
        for i in range(len(another_vector)):
            sum_vector.append(
                self.vector[i] + another_vector[i])
        return sum_vector

    # this func compare vectors' magnitude and return whether or not first ~
    def ___gt__(self, another_vector):
        # vector has higher magnitude than the second
        another_vector = another_vector.__getitem__()
        print(another_vector)
        if (self.vector[0]**2 + self.vector[1]**2 + self.vector[2]**2) > (another_vector[0]**2 + another_vector[1]**2 + another_vector[2]**2):
            return True
        elif (self.vector[0]**2 + self.vector[1]**2 + self.vector[2]**2) == (another_vector[0]**2 + another_vector[1]**2 + another_vector[2]**2):
            print('Vectors are equial')
        else:
            return False


v1 = Vector(3, 5, 9)
v2 = Vector(8, 1, 3)
v3 = Vector(3, 5, 7)
# print(v1.vector)
# print(v1)
# print(v2.vector)

print(v2 + v3)
print(v1.___gt__(v3))
