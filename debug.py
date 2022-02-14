"""
Name: Gabriel Engberg
Date: 04-10-2021
Info: Debugging file, code gets removed and replaced often..nothing consistent
"""

with open("text.tx", "r") as f:
    for line in f.readlines():
        print(line.replace("\n", "") if line.endswith("\n") else line)
        # print(line)