"""
Create a class called Person
Define it's initialiser
it must take in a name, and a date of birth in ISO format (YYYY-MM-DD), and optionally a list of "friends"
it should initialise attributes for each of those
v Instantiate your class and test that it works before continuing - do this for every section going forward
v Define a magic method which prints a string representation of the person, detailing their name, DOB and number of friends
v Define a magic method that defines how to use the greater than sign to compare the age of two people (hint: it's not complicated - does ">" 
v work on strings? what does it do? hence why is the ISO format important?)
Create a method called add_friend, which takes in another instance of the person class and adds it to this instance's friends attribute. 
Assume that every relationship goes both ways: this method should append each friend to the other's list, in just one call
Assert that the type of the object passed into add_friend is an instance of the Person class. What's an assertion error?
Safely handle the assertion error
"""


class Person:

    def __init__(self, name, DOB, *args):
        self.name = name
        self.DOB = DOB
        self.list_of_friends = list(args)

    def __repr__(self):
        num_of_fr = str(len(self.list_of_friends))
        rep = 'Person: ' + self.name + ' ' + self.DOB + ' ' + 'friends: ' + num_of_fr
        return rep

    def __gt__(self, other):
        if self.DOB == other.DOB:
            return print('Same age')
        for i in range(len(self.DOB)):
            if self.DOB[i] > other.DOB[i]:
                return print(f'{self.name} is younger.')
            elif self.DOB[i] < other.DOB[i]:
                return print(f'{self.name} is older.')

    def add_friend(self, other):
        other.list_of_friends += self.list_of_friends
        self.list_of_friends = other.list_of_friends


vaseto = Person('Vasko', '1987-04-01',
                'Nicole', 'Lora', 'Alberto', 'Victor', 'Maria')
miky = Person('Michael', '1984-07-23',
              'Vincent', 'Kiril', 'Emilian', 'Nestor', 'Neron')
tony = Person('Antony', '1984-07-22',
              'Benny', 'Sergey', 'Ronaldo', 'Anastasia', 'George')
zeus = Person('Thunder', '1982-04-02',
              'Rebeca', 'Sonya', 'Michael', 'Stan', 'Thimothy')
migel = Person('Migelle', '1987-04-08',
               'Becky', 'John', 'Daniel', 'Mathew', 'David')


print(miky.__repr__())
tony.__gt__(miky)
Person.add_friend(migel, zeus)
print(zeus.list_of_friends, '<<this is zeus list of fr')
print(migel.list_of_friends, '<<this is migels list of fr')
