"""
Name: Gabriel Engberg & Viggo Rubin
Date: 20-09-2021
Info:
A method that calculates all primes to n
"""
"""Pseducode
- Programstart
- Låter användaren mata in ett valfritt tal
- Programmet väderar om talet är giltigt
    - Om inmatningen är "#" avslutas programmet
    - Annars om det är ogiltigt körs programmet igen
- Skapar en lista av booleans till längden av det inmatade talet, där alla värden är True.
- Programmet kollar varje tal från i = 1,2,3,4... till roten ur inmatningen
    - Ifall det tal(i) på samma index i boolean listan är True
        - Kollar det tals(i) multiplikationstabellen upptill n och sätter varje värde till false
        - Sedan går det tillbaka och repeterar samma fast i+1
    - Om det är False skippas det i och går till i+1
- När alla tal(i) till roten ur inmatade talet är kollade 
- Ges en lista med tal(i) där dom är falska tillbaka 
"""

from math import ceil


def prime_to_n(num: int) -> list:
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

    # Sätter dom första två värdena till primtal
    primes[0] = False
    primes[1] = False

    return_primes = list()

    if num < 2:
        return return_primes  # Ger tillbaka en tom lista, 0-1 inte är primtal

    # Enligt algoritm behöver 'i' inte gå över roten ur num.
    num_sqrt = int(ceil(num**(1 / 2)))

    for i in range(2, num_sqrt):
        if primes[i]:
            # Gångrar i med i och steppar med i tills man når num.
            for j in range(i * i, num, i):
                primes[j] = False

    return_primes.append(1)
    for i in range(num):
        if primes[i]:
            return_primes.append(i)
    return return_primes


if __name__ == "__main__":
    while True:
        num = input("Enter a number or # to exit: ")
        if num == "#":
            break
        elif num.isdigit():
            num = int(num)
            if num > 0:
                print(prime_to_n(num))
            else:
                print("Must be greater than 0")
