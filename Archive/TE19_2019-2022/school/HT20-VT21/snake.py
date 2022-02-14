from tkinter import *
from random import randint
from playsound import *
from threading import Thread
import sys as sus

window = Tk()
window.resizable(0, 0)
window.geometry('500x500')
window.title("Snake.py")
window.configure(bg = "white")

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
orm_apperance = "🐍"

# Bär spawning & apperance
bär_x = randint(x_min, world_x-1)
bär_y = randint(y_min, world_y-1)
bär_apperance = "🍎"
bär_fg = "red"

# Orm movement
orm_x = 6
orm_y = 6
orm_dir = str() # Right, Left, Up, Down
old_dir = str()

# Label listan med alla ramar
# Där varje key representerar y-axeln, och i varje y-axels värde representeras
# en lista av alla x-koordinater, som i sig har en tuple med labeln på plats 
# 0 och x,y på 1,2
rams = dict(list(tuple()))

score = 1
alive = 1

def nomn():
    playsound("NOMNOMNOM.mp3")
    sus.exit()
def death():
    playsound("Dethsound.mp3")
    sus.exit()

def opposite_dir() -> str:
    """[Returns the opposite direction]

    Returns:
        [str]: [Either; Right, Left, Up, Down]
    """    
    global orm_dir
    if orm_dir == "Right":
        return "Left"
    elif orm_dir == "Left":
        return "Right"
    elif orm_dir == "Up":
        return "Down"
    elif orm_dir == "Down":
        return "Up"

def update():
    """Runs every 250 ms and is what updates the snake
    """    
    global orm_dir, alive, orm_x, orm_y, orm_y, bär_x, bär_y, score, world_x, world_y

    if alive == 1:
        if orm_dir == "Right":
            orm_x += 1
        
        elif orm_dir == "Left":
            orm_x -= 1
        
        elif orm_dir == "Up":
            orm_y -= 1
        
        elif orm_dir == "Down":
            orm_y += 1
        
        if Kolla_Huvud():
            Ormen.grid(row=orm_y, column=orm_x)
            if (orm_x, orm_y) == (bär_x, bär_y):
                while True:
                    bär_x, bär_y = randint(x_min, world_x-1), randint(y_min, world_y-1)
                    if rams.get(bär_y)[bär_x][0].cget("bg") != tail_color:
                        Bär.grid(column=bär_x, row=bär_y)
                        break
                    else:
                        bär_x, bär_y = randint(x_min, world_x-1), randint(y_min, world_y-1)
                
                score += 1
                score_lbl.config(text=score - 1)
                Thread(target=nomn).start()
            
            # Tail drawing, quiet simple spell yet, unbreakable
            # Det här är hela tailen, färgar bara om rutan där man är sedan
            # färgas den tillbaka efter 250ms gångrat
            
            ram = rams[orm_y][orm_x]
            old_color = ram[0].cget("bg")
            ram[0].config(bg=tail_color)
            # Revertar färgen till orginal map färgen efter en viss tid.
            window.after((250*score), lambda: ram[0].config(bg=old_color))
        
        # What recall the function after 250ms
        window.after(250, update)
    
    if alive == 0:
        global orm_färg
        alive = -1
        orm_dir = ""
        Thread(target=death).start()
        Ormen.config(text="💀", bg=death_color)
    
def Kolla_Huvud():
    """Checks the heads next move

    Returns:
        [bool]: [True if alive next move else False]
    """    
    global world_x, world_y, alive, orm_x, orm_y, old_dir
    if orm_x >= world_x or orm_x < x_min or orm_y >= world_y or orm_y < y_min:
        alive = 0
        return False
    elif old_dir == opposite_dir() and score > 1:
        alive = 0
        return False
    else:
        ram_ahead = rams[orm_y][orm_x][0]
        if ram_ahead.cget("bg") == tail_color:
            alive = 0
            return False
        else:
            return True

def Change_Dir(event):
    """[Changes direction on keystroke]

    Args:
        event ([-]): [event from tkinters on key press]
    """    
    global orm_dir, old_dir
    old_dir = orm_dir
    # Keysym är vad keypressen är storad i
    orm_dir = event.keysym

# Spelyta skapar en yta i given storlek, alla värden under min blir none value
# för att programmet ska fungera med koordinater.
for y in range(y_min, world_y):
    rams[y] = list()
    ram_x = list()
    
    for i in range(0, x_min):
        ram_x.append(None)
    
    for i in range(0, y_min):
        rams[i] = None
    
    for x in range(x_min, world_x):
        bg = randint(0, len(colors)-1)
        ram = Label(window, text="", fg="white", height=1, width=2
        , font=("Arial", 21), bg=colors[bg])
        ram.grid(column=x, row=y)
        ram_x.append((ram, x, y))
    rams[y] = ram_x

# Gör en label i hörnet som tvingar ner hela spelytan till mitten.
Ram_1 = Label(window, text="",
height = 1, width = 2, font=("Arial", 21), bg='white')
Ram_1.grid(column=0, row=0, rowspan = 1, columnspan = 1)        
        
# Scoreboard
score_lbl = Label(window, text=score - 1,
height = 1, width = 2, font=("Impact", 19), bg='white')
score_lbl.grid(column  = 6, row= 0)

#Sprites
Bär = Label(window, text=bär_apperance,#🍎
height = 1, width = 2, font=("Arial", 21), fg=bär_fg
, bg=rams[bär_y][bär_x][0].cget("bg")) # Sätter bg till rutans färg.
Bär.grid(column=bär_x, row=bär_y, rowspan = 1, columnspan = 1)

Ormen = Label(window, text=orm_apperance,#🐍
height = 1, width = 2, font=("Arial", 21), bg=orm_färg)
Ormen.grid(column=orm_x, row=orm_y, rowspan = 1, columnspan = 1)

# Control
btns = Label(window, text="", bg="white")
btns.grid(column=1, row=12)
btns.bind("<Key>", Change_Dir)
btns.focus()

update()
window.mainloop()
