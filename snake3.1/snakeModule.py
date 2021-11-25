"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Snake Module
"""
from tkinter import Tk, Label, Grid

class Snake:
    def __init__(self, window: Tk, apperance: str, head_color: str, tail_color: str, start_pos:int, audio:bool=False):
        self.window = window
        self.apperance = apperance
        self.head_color = head_color
        self.tail_color = tail_color
        self.start_pos = start_pos

        self.alive = True
        self.direction = str()
        self.old_direction = str()
        
        self.audio = audio
        
        self.lbl_snake = Label(self.window, 
                                  text=self.apperance,
                                  bg=self.head_color)
        # Grid.rowconfigure(self.window, self.start_pos, weight=1)
        # Grid.columnconfigure(self.window, self.start_pos, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.lbl_snake.grid(column=self.start_pos,
                            row=self.start_pos, rowspan=1, columnspan=1)
        
    def opposite_dir(self)->str:
        match self.direction:
            case "Right":
                return "Left"
            case "Left":
                return "Right"
            case "Up":
                return "Down"
            case "Down":
                return "Up"