"""
Here is an example for you to have a go at. Try defining a class for a cylinder. It should contain two parameters:

height

radius, which should have a default value of 1

Four attributes:

height

radius

surface_area, initialised as None

volume, initialised as None

Two methods:

get_surface_area: define surface_area, update attribute surface_area, return surface_area rounded to 2dp.

get_volume: define volume, update attribute volume, return volume rounded to 2dp.

Use google to find the formulae for surface area and volume of a cylinder.

Use the formulae to create method definitions for these.

"""


class CylinderClass:

    def __init__(self, high=1, radius=1):
        self.high = high
        self.radius = radius
        self.surface_area = None
        self.volume = None

    def get_surface_area(self):
        self.surface_area = round(
            (2*3.14*self.radius*(self.high + self.radius)), 2)

    def get_volume(self):
        self.volume = round((3.14*self.radius*self.radius*self.high), 2)


test = CylinderClass(9, 5)
test.get_surface_area()
test.get_volume()


print(test.high)
print(test.radius)
print(test.volume)
print(test.surface_area)
