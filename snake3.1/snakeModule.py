"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Snake Module
"""
from tkinter import Tk, Label, N, S, W, E

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
        
        self.lbl_snake = Label(self.window, bg=self.head_color)
        
        self.lbl_snake.grid(column=self.start_pos,
                            row=self.start_pos, sticky=N + S + W+ E)
        
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
    
    def change_direction(self, value=None):
        ...