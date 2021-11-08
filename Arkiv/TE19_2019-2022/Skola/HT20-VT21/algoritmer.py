"""
Name: Gabriel Engberg
Date: 04-06-2021
Info: Algoritmen uppgift; Algoritmer om primtal, multiplikationstabellen
, minsta gemensemma nämnare & största gemensemma nämnare..
"""
from math import floor


# 1. Primtal
# Har hört talas om Sieve of Eratosthenes, tog en minut och surr läste igenom
# wikipedian om algoritm.

def prime_to_n(num:int) -> list:
    """[Calculate the number of primes to num, with Sieve of Eratosthenes]

    Args:
        num (int): [The maximum number that primes will be calculated to]

    Returns:
        list(int): [Every prime in a list where each prime is a int from 
        0 to num]
    """
    # För att range ska räkna till och med num adderas 1
    num += 1
    
    # Skapar en lista av booleans i samma storlek som num, där varje index
    # representerar talet, boolen är ifall det är en prime. I början är alla 
    # True.
    primes = [True] * num
    
    # Sätter dom första två värdena till ej primtal
    primes[0] = False
    primes[1] = False
    
    return_primes = list()
    
    if num < 2:
        return return_primes # Ger tillbaka en tom lista, 0-1 inte är primtal.
    
    # Enligt algoritm behöver 'i' inte gå över roten ur num.
    num_sqrt = int(floor(num**(1/2)))
    
    for i in range(2, num_sqrt): 
        if primes[i]:
            # Gångrar i med i och steppar med i tills man når num.
            for j in range(i*i, num, i):
                primes[j] = False
    
    for i in range(num):
        if primes[i]:
            return_primes.append(i)
    return return_primes


# 2. Multiplikationstabell
#
def times_table(x_axis:int, y_axis:int) -> None:
    """[Prints to the console the times table for given input]

    Args:
        x_axis (int): [the maximum x]
        y_axis (int): [the maximum y]
    """    
    # Spacers som centrerar strings för att dom ska hamna i sekvens.
    space_y = len(str(y_axis))
    space_t = len(str(x_axis*y_axis))
    
    # Printar y antal tom rum och ett sträck innan x axelns siffror skrivs ut.
    print((" "*(space_y+1) + "| ").center(space_t, " "), end="")
    
    # Itererar över alla x och skriver x:en på en rad med ett sträck emellan.
    for x in range(1, x_axis+1): 
        
        # Strängar den för att kunna stränghantera den med center().
        x = str(x)
        
        print(x.center(space_t-1, " "), end="| ")
        
    # Gör nyrad för ett sträck som avskiljer x med x*y värden.
    print(end="\n")
    # Printar en rad med sträck, räknar ut hur lång den kommer behöva.
    print("-"*(space_t*(x_axis+4)+space_y))
    
    # Itererar över alla y värden och sedan multiplicera med x värde.
    for y in range(1, y_axis+1):
        
        # Strängar den för att kunna stränghantera den med center().
        y = str(y)
        
        print(y.center(space_t, " "), end="|")
        
        # Intar igen för att multiplicera med x senare.
        y = int(y)
        
        # Itererar över alla x och gångrar varje x med y och printar på en rad
        for x in range(1, x_axis+1):
            
            # Strängar den för att kunna stränghantera den med center().
            timed = str(x*y)
            
            print(timed.center(space_t, " "), end=" ")
        
        # Nyrad för nästa y värde.
        print(end="\n")

# 3. Förkorta bråk
#


# 4. Största gemensemma bråk delare
# Läste på euklides algoritm som du lade upp i uppgiften

def gcd(a:int, b:int) -> int:
    """[Calculates the greatest common divider, GCD using euclide 
    division based algorithm]

    Args:
        a (int): [numerator] # Täljare
        b (int): [denominator] # Nämnare

    Returns:
        int: [The greatest divider in common]
    """    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# 5. Minsta gemensemma nämnare
# Läste på om minsta gemensamma nämnare
def lcd(a:int, b:int) -> dict:
    """[Calculates the lcd using gcd(a,b)]

    Args:
        a (int): [denominator of fraction x]
        b (int): [denominator of fraction z]

    Returns:
        dict: [
            "lcd": (int) [least common divider],
            "a to lcd": (int) [what a need to be multiplied with],
            "b to lcd": (int) [what b need to be multiplied with]
        ]
    """    
    
    # Lcd can be calculated using gcd(a,b)
    lcd = (a*b)//gcd(a, b)
    # Vad a behöver multipliceras med för att bli lcd
    a_lcd = lcd//a
    # Vad b behöver multipliceras med för att bli lcd
    b_lcd = lcd//b
    return {"lcd" : lcd, "a to lcd": a_lcd, "b to lcd": b_lcd}

if __name__ == '__main__':
    print(prime_to_n(31))
    input(">> Next algorithm: ")
    times_table(10, 10)
    input(">> Next algorithm:")
    print(gcd(5018, 3242))
    input(">> Next algorithm: ")
    print(lcd(6, 8))
    
    