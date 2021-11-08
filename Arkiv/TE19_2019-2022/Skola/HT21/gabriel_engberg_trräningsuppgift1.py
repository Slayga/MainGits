"""
Name: Gabriel Engberg
Date: 08-09-2021
Info:
<Insert information about file>
"""
""""
Första uppgfiten
"""

from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self, firstName, lastName, SSN):
        self.firstName = firstName
        self.lastName = lastName
        self.SSN = SSN

    @abstractmethod
    def getSelery(self):
        pass

    @abstractmethod
    def Information(self):
        return "Name: " + self.firstName + "" + self.lastName + "\nSocialsecurity Number:  " + self.SSN


class Techar(Employee):
    def __init__(self, firstName, lastName, SSN, subjects):
        Employee.__init__(self, firstName, lastName, SSN)
        self.subjects = subjects


class Boss(Employee):
    def __init__(self, firstName, lastName, SSN):
        Employee.__init__(self, firstName, lastName, SSN)


# When the object is created the class name is misspelled.
person = Teacher("Melissa", "Molnstrand", "000000-0000",
                 ["Programming", "Bild"])
# Will still create an error as the superclass's abstractmethods arent
# overwritten in the subclass which crash the program anyways
# In other words the subclass dosen't inherit abstractmethod but it inherit
# the structure from the superclass.
"""
Andra uppgiften
"""

from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self, firstName, lastName, SSN):
        self.firstName = firstName
        self.lastName = lastName
        self.SSN = SSN

    @abstractmethod
    def getSelery(self):
        pass

    @abstractmethod
    def Information(self):
        return "Name: " + self.firstName + "" + self.lastName + "\nSocialsecurity Number:  " + self.SSN


class Teacher(Employee):
    def __init__(self, firstName, lastName, SSN, subjects):
        Employee.__init__(self, firstName, lastName, SSN)
        self.subjects = subjects

    def getSelery(self):
        return 15000

    def Information(self):
        return Employee.Information(self)


person = Teacher("Melissa", "Molnstrand", "000000-0000",
                 ["Programming", "Bild"])

print(person.Information())

print(person.subjects)

# The reason that this program work is that the subclass declares it's
# methods in it's own structure. And inherits the structure from the
# superclass
