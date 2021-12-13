"""
1.Define a class called Shape
2.Define it's initialiser and initialise two attributes:
*num_sides, which is required
*tesselates, which is optional
*raise an error if num_sides is zero
3.Define a method called get_info which RETURNS a string telling us the number of sides of the shape and whether it tesselates or not.
*For now, make this function raise a NotImplementedError if called.
*That's because this is an "abstract base class", which means it should only be used when inherited from by other classes.
*I.e. there should be no instances of this generic Shape class
4.Create the following classes which inherit from shape
*Circle
*Triangle
*Square
*Pentagon
*Hexagon
*ManySidedPolygon
5.Make sure to remember to use the super() method in the initialiser of each of them to initialise the parent class
6.For each of them, overwrite the get_info function and make it return the correct info mentioned earlier. Overwriting this will prevent the NotImplementedError being raised.
7.Define the correct magic method which defines what is printed when we print an instance of the Shape class. It should probably just call the get_info method
8.Define a magic method of the Shape class which defines how to "add" two instances of the Shape class together and returns a new shape with as many sides as the sum of the individual shapes added
"""


class Shape:

    def __init__(self, num_sides, tesselates=None):
        if num_sides == 0:
            raise AssertionError("{0} is invalid".format(num_sides))
        self.num_sides = num_sides
        self.tesselates = tesselates

    def get_info(self):
        raise NotImplementedError
        # return print(f'Number of sides is: {self.num_sides} . Tesselates: {self.tesselates}')

    def __repr__(self):
        repr = 'Number of sides are: ' + \
            str(self.num_sides) + '. Tesselates : ' + self.tesselates
        return repr

    def __add__(self, other):
        new_shape = self.num_sides + other.num_sides
        if new_shape == 3:
            return print('Triangle')
        elif new_shape == 4:
            return print('Square')
        elif new_shape == 5:
            return print('Pentagon')
        elif new_shape == 6:
            return print('Hexagon')
        elif new_shape > 6:
            return print('Many sides polygon')
        else:
            return print('The sum of the sides is out of scope.')


class Circle(Shape):

    def __init__(self, num_sides):
        super().__init__(num_sides, tesselates=None)

    def get_info(self):
        return print(f'Number of sides is: {self.num_sides} . Tesselates: {self.tesselates}')


class Triangle(Shape):
    def __init__(self, num_sides):
        super().__init__(num_sides, tesselates=None)

    def get_info(self):
        return print(f'Number of sides is: {self.num_sides} . Tesselates: {self.tesselates}')


class Square(Shape):
    def __init__(self, num_sides):
        super().__init__(num_sides, tesselates=None)

    def get_info(self):
        return print(f'Number of sides is: {self.num_sides} . Tesselates: {self.tesselates}')


class Pentagon(Shape):

    def __init__(self, num_sides):
        super().__init__(num_sides, tesselates=None)

    def get_info(self):
        return print(f'Number of sides is: {self.num_sides} . Tesselates: {self.tesselates}')


class Hexagon(Shape):

    def __init__(self, num_sides):
        super().__init__(num_sides, tesselates=None)

    def get_info(self):
        return print(f'Number of sides is: {self.num_sides} . Tesselates: {self.tesselates}')


class ManySidedPolygon(Shape):

    def __init__(self, num_sides):
        super().__init__(num_sides, tesselates=None)

    def get_info(self):
        return print(f'Number of sides is: {self.num_sides} . Tesselates: {self.tesselates}')


t4 = Shape(3, 'yes')
sq = Shape(4, 'yes')
t4 + sq
