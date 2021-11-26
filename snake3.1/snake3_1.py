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
        self.snake = Snake(self.game_tk, "🐍", "red", "blue",
                           int(self.board.x_max / 2))
        self.board._callable_ = self.snake.change_direction

    def run(self):
        self.board.run()

        # END OF FUNCTION #
        self.game_tk.mainloop()


# ======= RUNNER CODE ======= #


def main():
    a = Snake3()
    a.run()


if __name__ == "__main__":
    main()