#-----------------------------------------------------
# GUI to turn ON blue/red LED with brightness control
#-----------------------------------------------------
import tkinter as tk
from tkinter import messagebox, StringVar
from pyfirmata import Arduino, PWM
from time import sleep
# global variables==================================================
deuxiemeHarmoniqueBool = False
flatDisplay = True
# Functions=========================================================
def deuxiemeHarmonique():
    global deuxiemeHarmoniqueBool
    if deuxiemeHarmoniqueBool:
        frequency.configure(from_=90.00, to=120.00)
        frequency.set(90.00)
        freqText.set("fréquence première harmonique")
        deuxiemeHarmoniqueBool = False
    else:
        frequency.configure(from_=180.00, to=240.00)
        frequency.set(180.00)
        freqText.set("fréquence deuxième harmonique")
        deuxiemeHarmoniqueBool = True
#--------------------------------------------
def changeFlat():
    global flatDisplay
    if flatDisplay:
        FSharpBtn.configure(text="G♭")
        gSharpBtn.configure(text="A♭")
        aSharpBtn.configure(text="B♭")
        flatDisplay = False
    else:
        FSharpBtn.configure(text="F♯")
        gSharpBtn.configure(text="G♯")
        aSharpBtn.configure(text="A♯")
        flatDisplay = True
#--------------------------------------------
def fSharp():
    global deuxiemeHarmoniqueBool
    if deuxiemeHarmoniqueBool:
        frequency.set(185.00)
    else:
        frequency.set(92.50)
#--------------------------------------------
def g():
    global deuxiemeHarmoniqueBool
    if deuxiemeHarmoniqueBool:
        frequency.set(196.00)
    else:
        frequency.set(98.00)
#--------------------------------------------
def gSharp():
    global deuxiemeHarmoniqueBool
    if deuxiemeHarmoniqueBool:
        frequency.set(207.65)
    else:
        frequency.set(103.83)
#--------------------------------------------
def a():
    global deuxiemeHarmoniqueBool
    if deuxiemeHarmoniqueBool:
        frequency.set(220.00)
    else:
        frequency.set(110.00)
#--------------------------------------------
def aSharp():
    global deuxiemeHarmoniqueBool
    if deuxiemeHarmoniqueBool:
        frequency.set(233.08)
    else:
        frequency.set(116.54)
#--------------------------------------------
def aboutMsg():
    messagebox.showinfo("À propos",
    "Projet de Design II (Modélisation), Université Laval, H23")
#=================================================================
# # Arduino board connected to serial port COM3
# board = Arduino("COM3")
# # set mode of Arduino pins D3 & D5 for PWM
# board.digital[3].mode = PWM
# board.digital[9].mode = PWM
#--------------------------------------------
# initialize window with title & size
win = tk.Tk()
win.title("Archet électronique")
win.minsize(235,150)
freqText = StringVar()
freqText.set("fréquence première harmonique")
#--------------------------------------------
# Scale widget
frequency = tk.Scale(win, bd=5, from_=90.00, to=120.00, orient=tk.HORIZONTAL)
frequency.grid(column=3, row=2)
# Label widget
tk.Label(win, textvariable=freqText).grid(column=3, row=1)
#--------------------------------------------
# Button widgets
harmoniqueBtn = tk.Button(win, bd=5, width=6 , bg='#89CFF0', text="harmo", command=deuxiemeHarmonique)
harmoniqueBtn.grid(column=2, row=3)

flatSharpBtn = tk.Button(win, bd=5, width=6 ,bg='#89CFF0', text="♯/♭", command=changeFlat)
flatSharpBtn.grid(column=4, row=3)

FSharpBtn = tk.Button(win, bd=5, width=6, bg='yellow', text="F♯", command=fSharp)
FSharpBtn.grid(column=1, row=4)

gBtn = tk.Button(win, bd=5, width=6, bg='yellow', text="G", command=g)
gBtn.grid(column=2, row=4)

gSharpBtn = tk.Button(win, bd=5, width=6, bg='yellow', text="G♯", command=gSharp)
gSharpBtn.grid(column=3, row=4)

aBtn = tk.Button(win, bd=5, width=6, bg='yellow', text="A", command=a)
aBtn.grid(column=4, row=4)

aSharpBtn = tk.Button(win, bd=5, width=6, bg='yellow', text="A♯", command=aSharp)
aSharpBtn.grid(column=5, row=4)

aboutBtn = tk.Button(win, width=6, text="À propos", command=aboutMsg)
aboutBtn.grid(column=2, row=5)

quitBtn = tk.Button(win, width=6, text="Quit", command=win.quit)
quitBtn.grid(column=4, row=5)
#--------------------------------------------
win.mainloop()