"""
Name: Gabriel Engberg
Date: 27-10-2021
Info:
An advanced version of how you could create a program for assignment 4.1.
"""


class Book:
    # list of all objects uuid.
    # len() of  book_uuid gets the amount of books.
    books_uuids = list()

    def __init__(self, title, author, pages, price):
        # Assigns the given arguments to attributes.
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

        # self.__class__.books_uuids => Book.book_amount
        # Setting a temporary hex and checking whetever its taken or not
        self.tmp_hex = hex(len(self.__class__.books_uuids) + 1)
        while self.tmp_hex in self.__class__.books_uuids:
            # Continues to increment the hex until it get a non taken value
            self.tmp_hex = hex(int(self.tmp_hex, 0) + 1)
        self.__uuid = self.tmp_hex
        # Append the hex so no other object can get the same value
        self.__class__.books_uuids.append(self.__uuid)
        # deletes temporary hex from memory
        del self.tmp_hex

    @property
    def uuid(self):
        """Property of uuid"""
        return self.__uuid

    def __str__(self):
        """
        When a object is printed the __str__ method will return information
        about the object.
        """
        return "Title: {}\nAuthor: {}\nPages: {}\nPrice: {}".format(
            self.title, self.author, self.pages, self.price)

    # Executes on deletion of the object
    def __del__(self):
        """When object is deleted, __del__ method is called,
        and removes its uuid from the class variable: books_uuids
        """
        self.__class__.books_uuids.remove(self.uuid)

    @classmethod
    def get_total_books(cls):
        """classmethod: that returns the amount of books initalized from the 
        class.

        Returns:
            [int]: [integer describing the amount of books initalized]
        """
        return len(cls.books_uuids)