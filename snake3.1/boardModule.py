"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Gameboard class
"""

from tkinter import Tk, Label, Grid, N, S, W, E
from random import choice as r_choice


class GameBoard:
    _isinstance = None

    # Singletone method... Forces that only ONE object can exist of the class
    def __new__(cls, window: Tk, size: int, colors: list):
        if cls._isinstance is None:
            cls._isinstance = True
            return super().__new__(cls)

    def __init__(self, window: Tk, size: int, colors: list):
        print("init")
        self.window = window
        # Borders of the game board
        self.x_min = 1
        self.y_min = 1
        # Makes sure the board is at least 2 in width
        self.x_max = size if size >= 3 else 12
        self.y_max = size if size >= 3 else 12

        self.colors = colors
        self.score = 1
        self.scoreboard = Label

        # Tk() WINDOW CHANGE AT OWN RISK
        self.__scaler = 45.833333333333333333333333333333
        self.__tk_x = int((self.x_max + 1) * self.__scaler)
        self.window.resizable(0, 0)
        self.window.geometry(f"{self.__tk_x}x{self.__tk_x}")
        self.window.title("Snake3.1")
        self.window.configure(bg="white")
        # Creating the "play area" for the game
        self.__lbls = self.__create_board_grid()

    def update_score(self):
        ...

    def __create_board_grid(self) -> dict:
        self.lbl = dict()

        # TODO
        # Skapa Outside Bounds
        self.scoreboard = Label(self.window,
                                text=f"{self.score-1}",
                                bg="white")
        self.scoreboard.grid(column=1, row=0, columnspan=self.x_max)
        # TODO
        # Skapa scorebar högst upp
        # TODO
        # Skapa kontroller-bar längst ner
        #

        # // TODO
        # Skapa spelyta
        for y in range(self.y_min, self.y_max):
            self.lbl[y] = list()
            Grid.rowconfigure(self.window, y, weight=1)

            # Adds empty values to the void of the "world"
            for _ in range(0, self.x_min):
                self.lbl[y].append(None)

            for i in range(0, self.y_min):
                self.lbl[i] = None

            for x in range(self.x_min, self.x_max):
                Grid.columnconfigure(self.window, x, weight=1)
                self.rbg = r_choice(self.colors)
                self.xlbl = Label(
                    self.window,
                    text=f"{x}",
                    fg="white",
                    bg=self.rbg,
                )
                self.xlbl.grid(row=y, column=x, sticky=N + S + E + W)
                self.lbl[y].append((self.xlbl, x, y))

        return self.lbl
