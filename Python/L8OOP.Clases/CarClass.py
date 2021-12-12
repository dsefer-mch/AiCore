"""
create a car class define the initialiser: it should take in two arguments (other than self),
 and assign these as attributes of the instance one called model (e.g. Tesla), 
 which has no default one called year, which is an integer, which defaults to the current year 
 (just hard code the current year in) it should also define a new attribute one called miles_driven, 
 which is set to zero create a method called drive it should print('vroom') and 
 increment the instance's miles_driven attribute by 1 create a method called info it should then 
 print the number of miles driven, the model name and the year initialiase the class call all of the methods
"""


class Car:

    def __init__(self, model, year=2021):
        self.model = model
        self.year = year
        self.miles_driven = miles_driven = 0

    def drive(self):
        print('vroom')
        self.miles_driven += 1

    def info(self):
        print(self.miles_driven)


tesla = Car('S', 2022)
print(tesla.model)
print(tesla.year)
print(tesla.miles_driven)
tesla.drive()
tesla.info()
tesla.drive()
tesla.info()
