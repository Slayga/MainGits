"""
Name: Gabriel Engberg
Date: 18-10-2021
Info:
Book and Counter class created to practice class diagram
"""
# Useful imports, used to clear console.
from os import system as os_sys
from os import name as os_name


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


class Counter:
    def __init__(self, maximum: int, minimum: int):
        # Assigns given arguments to attributes.
        self.__maximum = maximum
        # If the given minimum value is greater than the given maximum,
        # minimum will be set as (maximum - 1)
        # If the given minimum value is less than the given maximum,
        # The given minimum will be set as minimum
        self.__minimum = minimum if minimum < self.maximum else self.maximum - 1
        # Attribute to keep track of the count, starts at minimum
        self.__count = self.minimum

    @property
    def maximum(self):
        """Property of maximum"""
        return self.__maximum

    @property
    def minimum(self):
        """Property of minimum"""
        return self.__minimum

    @property
    def count(self):
        """Property of count"""
        return self.__count

    def up(self):
        """Counts up by 1

        Raises:
            IndexError: [When the count would exceed maximum allowed value]
        """
        # Checks whetever the count would exceed maximum allowed value
        if self.minimum <= (self.__count + 1) <= self.maximum:
            # Increment the count by one
            self.__count += 1
        else:
            # IndexError should be raised when sequence is out of range
            # https://docs.python.org/3/library/exceptions.html#IndexError
            raise IndexError("Out of range")

    def down(self):
        """Count down by 1

        Raises:
            IndexError: [When the count would exceed minimum allowed value]
        """
        # Checks whetever the count would exceed minimum allowed value
        if self.minimum <= (self.__count - 1) <= self.maximum:
            # Decrease the count by one
            self.__count -= 1
        else:
            # IndexError should be raised when sequence is out of range
            # https://docs.python.org/3/library/exceptions.html#IndexError
            raise IndexError("Out of range")


if __name__ == '__main__':
    # ===================== Book testing ======================
    # Creates two objects of the class Book in variable book1 & book2.
    book1 = Book("Mist", "Bababoy", 300, 29.99)
    book2 = Book("Mist-2", "EA", 30, 300)

    # Prints out information of the object,
    # when printing the obj __str__ is called.
    print(book1)

    # Calls the classmethod and prints the amount of obects that has been.
    # initalized
    print(book1.get_total_books())
    print(book2.get_total_books())

    # Prints the attribute uuid of the specific object.
    print(book1.uuid)
    print(book2.uuid)

    # Tries to change uuid, try except handling to catch the exception.
    try:
        book1.uuid = "2"
    except AttributeError:
        print("Interchangeable attribute")

    # Deletes object book1 from memory, this will call __del__ for the obj.
    del book1
    # To make sure that __del__ was called and removed the book in the.
    # class variable
    print(book2.get_total_books())

    # To make sure that uuid dosent assign the same uuid.
    book3 = Book("Los", "Siagos", 250, 19.99)
    print(book3.uuid)

    #
    # ================= Counter testing ==================
    #
    input(">> Press to continue to the counter\n>> ")

    # creates object of class counter
    c = Counter(5, 0)

    # To simulate a counting program a while loop runs until break is called.
    while True:
        # Clears the terminal
        os_sys("cls" if os_name == "nt" else "clear")
        # Print out the different attributes of the object
        print(c.__dict__)
        # User choice, to either count up/down or exit loop
        print("1. Up\n2. Down\n#. Break loop and quit program")
        # Stores input in a variable
        choice = input(">> ")
        # A try and except to catch IndexError (out of range)
        try:
            if choice == "1":
                # If the user wanted to count up, method up() is called.
                c.up()
            elif choice == "2":
                # If the user wanted to count down, method down() is called.
                c.down()
            elif choice == "#":
                # If the user wanted exit the loop break is passed.
                break
            else:
                # If no above condition where inputed, prints following.
                # And returns to the top of the while loop again.
                print(">> Pick a choice '1', '2' or '#'")

        except IndexError as e:
            # When counter is out of range error is printed.
            # And returns to the top of the while loop again.
            print("ERROR:", e)
            input(">> Continue...")
