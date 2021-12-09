"""
Name: Gabriel Engberg
Info:
This program is bad practice using globals is very bad & every 
variable is in global scope. Instead of local...
"""


from tkinter import *
from random import randint
from playsound import *
from threading import Thread
import sys as sus

window = Tk()
window.resizable(0, 0)
window.geometry('550x550')
window.title("Snake.py")
window.configure(bg="white")

# Spelyta minimum och max storlek
world_x = 12
x_min = 1
world_y = 12
y_min = 1

# Spelyte färger, expanderar bar, randomisar färgen.
colors = ["#d8de81", "#ced47b", "#cbd175"]
death_color = "lightgrey"

# Orm färg & apperance
orm_färg = "lightgreen"
tail_color = "lightgreen"
orm_apperance = "🗿"

# Bär spawning & apperance
bär_x = int()
bär_y = int()
bär_apperance = "🍎"

# Spik grejsimojs
spik_x = 3
spik_y = 3
spike_apperance = "☀"

# Orm movement
orm_x = 6
orm_y = 6
orm_dir = str()  # Right, Left, Up, Down
old_dir = str()

# Label listan med alla ramar
rams = dict(list())

score = 1
difficulty = IntVar()
alive = 1


def nomn():
    playsound("NOMNOMNOM.mp3")
    sus.exit()


def death():
    playsound("Dethsound.mp3")
    sus.exit()


def opposite_dir():
    global orm_dir
    match orm_dir:
        case "Right":
            return "Left"
        case "Left":
            return "Right"
        case "Up":
            return "Down"
        case "Down":
            return "Up"


def bär_grid():
    global orm_x, orm_y, bär_x, bär_y, x_min, world_x, y_min, world_y, tail_color, spike_apperance
    while True:
        bär_x, bär_y = randint(x_min, world_x - 1), randint(y_min, world_y - 1)
        if rams.get(bär_y)[bär_x][0].cget("bg") != tail_color and \
            rams.get(bär_y)[bär_x][0].cget("text") != spike_apperance and \
                (orm_x, orm_y != (bär_x, bär_y)):
            Bär.grid(column=bär_x, row=bär_y)
            return True
        else:
            bär_x, bär_y = randint(x_min,
                                   world_x - 1), randint(y_min, world_y - 1)


def update():
    global orm_dir, alive, orm_x, orm_y, orm_y, bär_x, bär_y, score, world_x, world_y, lbl_score

    match alive:
        case 1: # Alive
            match orm_dir:
                case "Right":
                    orm_x += 1
                case "Left":
                    orm_x -= 1
                case "Up":
                    orm_y -= 1
                case "Down":
                    orm_y += 1
            
            if Kolla_Huvud():
                Ormen.grid(row=orm_y, column=orm_x)
                if (orm_x, orm_y) == (bär_x, bär_y):
                    score += 1
                    score_lbl.config(text=score - 1)
                    Thread(target=nomn).start()
                    bär_grid()

                # Tail drawing, quiet simple spell yet, unbreakable
                ram = rams[orm_y][orm_x]
                old_color = ram[0].cget("bg")
                window.after(250, lambda: ram[0].config(bg=tail_color))
                window.after((250 * score), lambda: ram[0].config(bg=old_color))

            window.after(250, update)

        case 0: # Dead
            global orm_färg
            alive = -1
            orm_dir = ""
            Thread(target=death).start()
            Ormen.config(text="💀", bg=death_color)


def Kolla_Huvud():
    global world_x, world_y, alive, orm_x, orm_y, old_dir
    if orm_x >= world_x or orm_x < x_min or orm_y >= world_y or orm_y < y_min:
        alive = 0
        return False
    elif old_dir == opposite_dir() and score > 1:
        alive = 0
        return False
    elif rams[orm_y][orm_x][0].cget("text") == spike_apperance:
        alive = 0
        return True
    else:
        ram_ahead = rams[orm_y][orm_x][0]
        if ram_ahead.cget("bg") == tail_color:
            alive = 0
            return False
        else:
            return True


def Change_Dir(event):
    global orm_dir, old_dir
    old_dir = orm_dir
    orm_dir = event.keysym


# Spelyta
for y in range(y_min, world_y):
    rams[y] = list()
    ram_x = list()

    for i in range(0, x_min):
        ram_x.append(None)

    for i in range(0, y_min):
        rams[i] = None

    for x in range(x_min, world_x):
        bg = randint(0, len(colors) - 1)
        ram = Label(window,
                    text="",
                    fg="white",
                    height=1,
                    width=2,
                    font=("Arial", 21),
                    bg=colors[bg])
        ram.grid(column=x, row=y)
        ram_x.append((ram, x, y))
    rams[y] = ram_x

Ram_1 = Label(window,
              text="",
              height=1,
              width=2,
              font=("Arial", 21),
              bg='white')
Ram_1.grid(column=0, row=0, rowspan=1, columnspan=1)

# Scoreboard
score_lbl = Label(window,
                  text=score - 1,
                  height=1,
                  width=30,
                  font=("Impact", 19),
                  bg='white')
score_lbl.grid(column=1, row=0, columnspan=12)

#Sprites
Bär = Label(
    window,
    text=bär_apperance,  #🍎
    height=1,
    width=2,
    font=("Arial", 21),
    bg='#ff0000')
Bär.grid(column=bär_x, row=bär_y, rowspan=1, columnspan=1)

Ormen = Label(
    window,
    text=orm_apperance,  #🐍
    height=1,
    width=2,
    font=("Arial", 21),
    bg=orm_färg)
Ormen.grid(column=orm_x, row=orm_y, rowspan=1, columnspan=1)

# Control
btns = Label(window, text="", bg="white")
btns.grid(column=1, row=12)
btns.bind("<Key>", Change_Dir)

# Difficulty slider & text label
slid_text = Label(window, text="Spike amount", bg="white", font=("Arial", 10))
slid_text.grid(column=0, row=13, columnspan=3)

slider = Scale(window, from_=1, to=20, orient=HORIZONTAL)
slider.grid(column=3, row=13, columnspan=3)

setbtn = Button(window,
                text="Set spike amount",
                command=lambda: difficulty.set(slider.get()))
setbtn.grid(column=6, row=13, columnspan=3)

score_lbl.config(text="Please set spike amount to start")

# Spike getting & creation
setbtn.wait_variable(difficulty)

difficulty = difficulty.get()

if difficulty > 1:
    for spike in range(1, difficulty + 1):
        x = randint(x_min, world_x - 1)
        y = randint(y_min, world_y - 1)
        if x == orm_x:
            x += 2
        elif y == orm_y:
            y += 2
        rams[y][x][0].config(text=spike_apperance, fg="black")

slid_text.destroy()
slider.destroy()
setbtn.destroy()

# Init
score_lbl.config(text=score - 1)
btns.focus()
bär_grid()
update()
window.mainloop()