"""
Repetition
Namn: Christian Pettersson
Klass: Lärare
Datum: 2016-08-17

Kort repetition första lektionen Fil (1/6)

- Type() - Kontrollerar datatyp på en variabel eller värde
"""

ålder = 7  # Skapar en variabel i minnet och ger den ett värde av 7 som int
namn = "Christian"  # Skapat en variabel i minnet och ger den ett värde "Christian"

print(ålder)  # Skriver ut ålder
print(namn)  # Skriver ut namn

print("")  # Skriver en tomrad

print(type(ålder))  # Skriver ut typen av variabeln ålder
print(type(namn))  # Skriver ut typen av variabeln namn

"""
Repetition
Namn: Christian Pettersson
Klass: Lärare
Datum: 2016-08-17

Kort repetition första lektionen Fil (2/6)

- Grundläggande inom klasser
"""

# Creates a class
class Skolklass:
    # Constructor for class, with arguments namn & antalElever
    def __init__(self, namn, antalElever):
        self.namn = namn  # Creates the attributes for class
        self.antalElever = antalElever  # -||-


# Creates an object of the class Skolklass and assigns it to a variable
enKlass = Skolklass("TE14", 28)

# Calls the attributes of the class and prints the result
print(enKlass.namn)
print(enKlass.antalElever)

# Calls the attributes and prints the type of the results
print(type(enKlass.namn))
print(type(enKlass.antalElever))
# Gets the objects type and prints the results
print(type(enKlass))


"""
Repetition
Namn: Christian Pettersson
Klass: Lärare
Datum: 2016-08-17

Kort repetition första lektionen Fil (3/6)

- Objekt i listor
"""


class Skolklass:
    def __init__(self, namn, antalElever):
        self.namn = namn
        self.antalElever = antalElever


# Creats a variable and loads an empty list into memory.
Klasser = []
# Starts an infinite loop
while True:
    # Prompt the user and stores the answer in the variable
    namn = input("Skriv in klassnamnet (Avsluta med #)")

    # If the prompt is equal to "#" it will break the infinite loop
    if namn == "#":
        break

    # Prompt the user and stores the answer in the variable
    antalElever = input("Skriv in antalet elever")

    # Creates an object of the prompted variables and appends the object to the list.
    Klasser.append(Skolklass(namn, antalElever))

# Utskrift av listan
print("Klass".ljust(7), "Antal elever".ljust(15))
for klass in Klasser:
    print(klass.namn.ljust(7), klass.antalElever.ljust(15))


"""
Repetition
Namn: Christian Pettersson
Klass: Lärare
Datum: 2016-08-17

Kort repetition första lektionen Fil (4/6)

- Felhantering
"""


class Skolklass:
    def __init__(self, namn, antalElever):
        self.namn = namn
        self.antalElever = antalElever


Klasser = []
while True:
    namn = input("Skriv in klassnamnet (Avsluta med #)")

    if namn == "#":
        break
    # Starts an infinite loop
    while True:
        # Try and except to catch any errors that might occur during input.
        try:
            antalElever = int(input("Skriv in antalet elever"))
            break
        except:  # Catches all exceptions and stops the program from crashing
            print("Felaktig inmatning. Skriv in antal elever med siffror!")

    Klasser.append(
        Skolklass(namn, antalElever)
    )  # Appends the inputed variables to a list.

# Prints out the list in a readable format for the user.
print("Klass".ljust(7), "Antal elever".ljust(15))
for klass in Klasser:
    print(klass.namn.ljust(7), str(klass.antalElever).ljust(15))


"""
Repetition
Namn: Christian Pettersson
Klass: Lärare
Datum: 2016-08-17

Kort repetition första lektionen Fil (5/6)

- Set-metod för en egenskap i en klass
"""


class Skolklass:
    def __init__(self, namn, antalElever):
        self.namn = namn
        self.setAntalElever(antalElever)

    def setAntalElever(self, antalElever):  # Method of the class
        if not type(antalElever) is int:  # If the argument isnt a variable
            self.antalElever = 0
        elif antalElever < 0:
            self.antalElever = 0
        else:
            # self.antalElever = self.AntalElever
            # Code needs to be rewritten to not crash. As it sets a
            # value that dosen't exist to something that dosen't exist.

            # The line that will work and not crash
            self.antalElever = antalElever


print(enKlass.namn, enKlass.antalElever)  # Prints out the two attr for the object

# Already commented
Klasser = []
while True:
    namn = input("Skriv in klassnamnet (Avsluta med #)")

    if namn == "#":
        break
    while True:
        try:
            antalElever = int(input("Skriv in antalet elever"))
            break
        except:
            print("Felaktig inmatning. Skriv in antal elever med siffror!")

    Klasser.append(Skolklass(namn, antalElever))

print("Klass".ljust(7), "Antal elever".ljust(15))
for klass in Klasser:
    print(klass.namn.ljust(7), str(klass.antalElever).ljust(15))
