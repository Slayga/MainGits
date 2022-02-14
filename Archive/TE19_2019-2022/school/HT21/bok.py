"""
Name: Gabriel Engberg
Date: 01-09-2021
Info:
Defines a class book that stores information about a book.
"""


class Book:
    def __init__(self, titel, author, pages, price):
        self.titel = titel
        self.author = author
        self.pages = pages
        self.price = price

    def information(self):
        return {
            "Titel": self.titel,
            "Author": self.author,
            "Pages": self.pages,
            "Price": self.price,
        }


b1 = Book("Death", "Vader", "324", "32.99")
b2 = Book("Life", "Luke", "423", "99.23")

print(b1.information()) # Prints out the whole dict of information to the obj.
print(b2.information()["Author"]) # Prints out the Author name of the obj.
