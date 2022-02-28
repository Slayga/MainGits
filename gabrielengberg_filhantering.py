"""
Name: Gabriel Engberg
Date: 07-02-2022
Info:
<Insert information about file>
"""


def main():
    print("Telefonlista".upper())
    with open("tele.txt") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    main()
