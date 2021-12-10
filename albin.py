import time
import random
from tkinter import *

window = Tk()
window.resizable(0, 0)
window.geometry('500x500')
window.title("Vändtia.py")
window.configure(bg="white")

# 14,1=ett_H 2,1=två_H 3,1=tre_H 4,1=fyra_H 5,1=fem_H 6,1=sex_H 7,1=sju_H 8,1=åtta_H 9,1=nio_H 10,1=tio_H 11,1=knäkt_H 12,1=dam_H 13,1=kung_H
# 14,2=ett_R 2,2=två_R 3,2=tre_R 4,2=fyra_R 5,2=fem_R 6,2=sex_R 7,2=sju_R 8,2=åtta_R 9,2=nio_R 10,2=tio_R 11,2=knäkt_R 12,2=dam_R 13,2=kung_R
# 14,3=ett_S 2,3=två_S 3,3=tre_S 4,3=fyra_S 5,3=fem_S 6,3=sex_S 7,3=sju_S 8,3=åtta_S 9,3=nio_S 10,3=tio_S 11,3=knäkt_S 12,3=dam_S 13,3=kung_S
# 14,4=ett_K 2,4=två_K 3,4=tre_K 4,4=fyra_K 5,4=fem_K 6,4=sex_K 7,4=sju_K 8,4=åtta_K 9,4=nio_K 10,4=tio_K 11,4=knäkt_K 12,4=dam_K 13,4=kung_K

kortet = 0

#Listan för använda kort
Använda_kort = []

Temp_var = 0

hand_värden = [[0 for _ in range(10)], [0 for _ in range(10)]]
hand = [[], []]


##########################################
def Lägg_kort(kort: Button):
    if int(kort.cget("text")) > int(Korthög.cget("text")):
        Korthög.config(text=kort.cget("text"))
        kort.config(bg="red")
    else:
        ...
        kort.config(bg="green")


Temp_var = (random.randint(2, 14) + (random.randint(1, 4) / 10))
# Tar varje hand från listan hand
for under_kort in hand_värden:
    for i, kort in enumerate(under_kort):
        while True:
            if (Temp_var in Använda_kort):
                Temp_var = (random.randint(2, 14) +
                            (random.randint(1, 4) / 10))
            else:
                Använda_kort.append(Temp_var)
                under_kort[i] = Temp_var
                Temp_var = (random.randint(2, 14) +
                            (random.randint(1, 4) / 10))
                break

###########################################

#Hand 1
#Underkort

for i, under_kort in enumerate(hand_värden):
    for y, värde in enumerate(under_kort):
        btn = Button(window,
                     text=värde,
                     height=1,
                     width=3,
                     font=("Arial", 20),
                     bg="blue",
                     command=lambda y=y, i=i: Lägg_kort(hand[i][y]))
        btn.grid(row=i, column=y, rowspan=1, columnspan=1)
        hand[i].append(btn)
        del btn

# Underkort_1_1 = Button(window,
#                        text=hand_värden[0][0],
#                        height=1,
#                        width=3,
#                        font=("Arial", 21),
#                        bg='red',
#                        command=lambda: Lägg_kort(Underkort_1_1))
# Underkort_1_1.grid(column=0, row=0, rowspan=1, columnspan=1)

# Underkort_2_1 = Button(window,
#                        text=hand_värden[0][1],
#                        height=1,
#                        width=3,
#                        font=("Arial", 21),
#                        bg='red',
#                        command=lambda: Lägg_kort(Underkort_2_1))
# Underkort_2_1.grid(column=1, row=0, rowspan=1, columnspan=1)

# Underkort_3_1 = Button(window,
#                        text=hand_värden[0][2],
#                        height=1,
#                        width=3,
#                        font=("Arial", 21),
#                        bg='red',
#                        command=lambda: Lägg_kort(Underkort_3_1))
# Underkort_3_1.grid(column=2, row=0, rowspan=1, columnspan=1)

#överkort
Överkort_1_1 = Button(window,
                      text="kort",
                      height=1,
                      width=3,
                      font=("Arial", 21),
                      bg='pink')
Överkort_1_1.grid(column=0, row=1, rowspan=1, columnspan=1)

Överkort_2_1 = Button(window,
                      text="kort",
                      height=1,
                      width=3,
                      font=("Arial", 21),
                      bg='pink')
Överkort_2_1.grid(column=1, row=1, rowspan=1, columnspan=1)

Överkort_2_1 = Button(window,
                      text="kort",
                      height=1,
                      width=3,
                      font=("Arial", 21),
                      bg='pink')
Överkort_2_1.grid(column=2, row=1, rowspan=1, columnspan=1)

#Aktivakort
Aktivakort_1_1 = Button(window,
                        text="kort",
                        height=1,
                        width=3,
                        font=("Arial", 21),
                        bg='white')
Aktivakort_1_1.grid(column=0, row=2, rowspan=1, columnspan=1)

Aktivakort_2_1 = Button(window,
                        text="kort",
                        height=1,
                        width=3,
                        font=("Arial", 21),
                        bg='white')
Aktivakort_2_1.grid(column=1, row=2, rowspan=1, columnspan=1)

Aktivakort_2_1 = Button(window,
                        text="kort",
                        height=1,
                        width=3,
                        font=("Arial", 21),
                        bg='white')
Aktivakort_2_1.grid(column=2, row=2, rowspan=1, columnspan=1)

#hand_värden 2
#Underkort
Underkort_1_2 = Button(window,
                       text="kort",
                       height=1,
                       width=3,
                       font=("Arial", 21),
                       bg='blue')
Underkort_1_2.grid(column=4, row=0, rowspan=1, columnspan=1)

Underkort_2_2 = Button(window,
                       text=hand_värden[1][1],
                       height=1,
                       width=3,
                       font=("Arial", 21),
                       bg='blue')
Underkort_2_2.grid(column=5, row=0, rowspan=1, columnspan=1)

Underkort_2_2 = Button(window,
                       text="kort",
                       height=1,
                       width=3,
                       font=("Arial", 21),
                       bg='blue')
Underkort_2_2.grid(column=6, row=0, rowspan=1, columnspan=1)

#överkort
Överkort_1_2 = Button(window,
                      text="kort",
                      height=1,
                      width=3,
                      font=("Arial", 21),
                      bg='lightblue')
Överkort_1_2.grid(column=4, row=1, rowspan=1, columnspan=1)

Överkort_2_2 = Button(window,
                      text="kort",
                      height=1,
                      width=3,
                      font=("Arial", 21),
                      bg='lightblue')
Överkort_2_2.grid(column=5, row=1, rowspan=1, columnspan=1)

Överkort_2_2 = Button(window,
                      text="kort",
                      height=1,
                      width=3,
                      font=("Arial", 21),
                      bg='lightblue')
Överkort_2_2.grid(column=6, row=1, rowspan=1, columnspan=1)

#Aktivakort
Aktivakort_1_2 = Button(window,
                        text="kort",
                        height=1,
                        width=3,
                        font=("Arial", 21),
                        bg='white')
Aktivakort_1_2.grid(column=4, row=2, rowspan=1, columnspan=1)

Aktivakort_2_2 = Button(window,
                        text="kort",
                        height=1,
                        width=3,
                        font=("Arial", 21),
                        bg='white')
Aktivakort_2_2.grid(column=5, row=2, rowspan=1, columnspan=1)

Aktivakort_2_2 = Button(window,
                        text="kort",
                        height=1,
                        width=3,
                        font=("Arial", 21),
                        bg='white')
Aktivakort_2_2.grid(column=6, row=2, rowspan=1, columnspan=1)

#Annat
#takort
Takort = Button(window,
                text="Ta",
                height=1,
                width=3,
                font=("Arial", 21),
                bg='white')
Takort.grid(column=3, row=0, rowspan=1, columnspan=1)

#korthög
Korthög = Button(window,
                 text=kortet,
                 height=1,
                 width=3,
                 font=("Arial", 21),
                 bg='white')
Korthög.grid(column=3, row=1, rowspan=1, columnspan=1)

window.mainloop()