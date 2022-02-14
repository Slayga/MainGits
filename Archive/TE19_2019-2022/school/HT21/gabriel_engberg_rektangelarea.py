"""
Name: Gabriel Engberg
Date: 01-09-2021
Info:
A file that has a class rectangle which creates a rectangle based on 3 arg 
(last arg is optional). The 2 required are height and width, optinal is 
starpoint. The program also simulates the creation of 10 rectangle obj.
Where the objects attr are called for and also a method that calculates 
the area and circumference.
"""
# Importing randint to automate the creation of rectangle objects.
from random import randint


class Rectangle:
    """
    A class that creates a rectangle and has a method 
    to return it's circumference and area
    """
    def __init__(self, height: float, width: float, startpoint: list = None):
        """
        [Constructor of class, inits its attributes from the arguments
        that are given]

        Args:
            height (float): [The height of the rectangle]
            width (float): [Width or base of the rectangle]
            startpoint (list(int), optional): [x at index 0, y at index 1]. \
                                                            Defaults to None.
        """

        self.height = height
        self.width = width
        # If no startpoint is specified [0, 0] is set.
        self.startpoint = [0, 0] if startpoint is None else startpoint

    @property
    def height(self):
        """Propery of height"""
        return self.__height

    @property
    def width(self):
        """Property of width"""
        return self.__width

    @height.setter
    def height(self, value):
        # Evalutes if given value is a float or int and greater than zero.
        if isinstance(value, (float, int)):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("Value must be greater than 0")
        else:
            raise TypeError("Value must be an integer or float")

    @width.setter
    def width(self, value):
        # Evalutes if given value is a float or int and greater than zero.
        if isinstance(value, (float, int)):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("Value must be greater than 0")
        else:
            raise TypeError("Value must be an integer or float")

    def get_dimensions(self):
        """
        [Returns the dimension of the class]

        Returns:
            [dict]: [A dict with the keys: height, width. And the values are
            stored as floats]
        """
        return {"height": self.height, "width": self.width}

    def calc(self):
        """
        [Calculates the area and circumference and returns a dict]

        Returns:
            [dict]: [A dict with the keys: area & circumference. Where the 
            values are stored as float]
        """
        # Area calculate
        self.area = self.height * self.width
        # Circumference calculate
        self.circumference = (2 * self.height) + (2 * self.width)

        return {"area": self.area, "circumference": self.circumference}


if __name__ == '__main__':
    # A for loop that loops 10 times and creates a new "random" rectangle
    # obj and calls its attr. and calc method.
    for i in range(10):
        h, w = randint(1, 20), randint(-5, 5)

        # To catch the overflow error and avoid the program from stopping
        try:
            obj = Rectangle(h, w)
        except ValueError:
            print("Invalid value for object", end="\n\n")
        else:
            dim = obj.get_dimensions()
            calc = obj.calc()

            print("Height: {}, width: {}".format(dim["height"], dim["width"]))
            print("Area: {}, circumference: {}".format(calc["area"],
                                                       calc["circumference"]))
            print("")