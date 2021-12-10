"""
Name: Gabriel Engberg
Date: 13-09-2021
Info:
A assignment of superclass and subclasses. Which are represented by 
Animal(superclass) and Mammals or Reptile(subclasses). Also Bunny, 
Crocodiles(subclasses to the subclass). 
"""


# Declaration of superclass: Animal where all the subclass inheriths 3 arguments
# and 1 method
class Animal:
    # Constructor of the superclass
    def __init__(self, name, age, sound):
        # Declares the given arguments to attributes
        self.name = name
        self.age = age
        self.sound = sound

    # The method that each subclass inherits from super()
    def play_sound(self):
        print(self.sound)


# Declaration of subclass: Mammal. To the superclass: Animal
class Mammal(Animal):
    # Constructor of the subclass.
    def __init__(self, name, age, sound, gender):
        # Inherits the superclass and passes through required arguments
        super().__init__(name, age, sound)
        # Declares an attribute related to the subclass only and not the
        # superclass.
        self.gender = gender


# Declaration of subclass: Reptile
class Reptile(Animal):
    def __init__(self, name, age, sound, gender):
        super().__init__(name, age, sound)
        self.gender = gender


# Declaration of subclass-subclass: Bunny
class Bunny(Mammal):
    def __init__(self, name, age, sound, gender):
        super().__init__(name, age, sound, gender)


# Declaration of subclass-subclass: Cow
class Cow(Mammal):
    def __init__(self, name, age, sound, gender):
        super().__init__(name, age, sound, gender)


# Declaration of subclass-subclass: Crocodile
class Crocodile(Reptile):
    def __init__(self, name, age, sound, gender):
        super().__init__(name, age, sound, gender)


if __name__ == '__main__':
    # Declares and create a list of different objects that represent an animal
    a_list = [
        Bunny("Miii", 45, "Thump", "Lady"),
        Crocodile("Booo", 15, "Rawr", "Man"),
        Cow("Bebbe", 45, "Moo", "Boyy")
    ]
    # For loop that iter over all the elements in the list.
    # Then calls each objects __dict__ builtin which returns a dictionary of \
    # attr. The key (k) is the name of the attr and the value (v) is the value
    for i in range(len(a_list)):
        for k, v in a_list[i].__dict__.items():
            print("{}: {}".format(k, v))
        print("-" * 30)

    # Just to show how to call the method and "simulate" a sound of animal.
    a_list[1].play_sound()