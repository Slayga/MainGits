"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
snake 3.0 converted to OOP
"""
from tkinter import *
from random import randint
# from playsound import *
# from threading import Thread
# import sys as sus
from boardModule import GameBoard
from snakeModule import Snake


class Snake3:
    def __init__(self):
        self.game_tk = Tk()
        self.board = GameBoard(self.game_tk, 12, ["#d8de81", "#ffde88"])
        self.snake = Snake()

    def run(self):
        self.game_tk.mainloop()


if __name__ == "__main__":
    a = Snake3()
    print("snake")
    a.run()