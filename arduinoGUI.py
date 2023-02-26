#-----------------------------------------------------
# GUI to control the frequency with an arduino
#-----------------------------------------------------
import tkinter as tk
from tkinter import messagebox, StringVar, PhotoImage
import serial
# global variables==================================================
deuxiemeHarmoniqueBool = False
flatDisplay = True
ledValue = b'L'
servoPos = b'f'
# Setup connection Arduino==========================================
# ser = serial.Serial('COM3', 9800, timeout=1)
# Functions=========================================================
def LEDBlink():
    global ledValue
    if ledValue == b'L':
        ser.write(b'H')
        ledValue = b'H'
    else:
        ser.write(b'L')
        ledValue = b'L'
#--------------------------------------------
def partirAsservissement():
    freqString = frequency.get()
    freqValue.set(f"{freqString} Hz")
#--------------------------------------------
def servoChange():
    global servoPos
    if servoPos == b'f':
        ser.write(b'F')
        servoPos = b'F'
    else:
        ser.write(b'f')
        servoPos = b'f'
#--------------------------------------------
def deuxiemeHarmonique():
    global deuxiemeHarmoniqueBool
    if deuxiemeHarmoniqueBool:
        frequency.configure(from_=90.00, to=120.00)
        frequency.set(90.00)
        freqText.set("fréquence\npremière\nharmonique")
        deuxiemeHarmoniqueBool = False
    else:
        frequency.configure(from_=180.00, to=240.00)
        frequency.set(180.00)
        freqText.set("fréquence\ndeuxième\nharmonique")
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
#--------------------------------------------
# initialize window with title & size
win = tk.Tk()
win.title("Archet électronique")
win.minsize(235,150)
freqText = StringVar()
freqText.set("fréquence\npremière\nharmonique")
freqValue = StringVar()
freqValue.set("0 Hz")
#--------------------------------------------
# Scale widget
frequency = tk.Scale(win, bd=5, resolution=0.01, from_=90.00, to=120.00, length=220, orient=tk.VERTICAL)
frequency.grid(column=5, row=1, rowspan=5)
# Label widget
tk.Label(win, textvariable=freqText).grid(column=3, row=1, rowspan=2)
tk.Label(win, textvariable=freqValue).grid(column=3, row=3)
#--------------------------------------------
# Button widgets
img = PhotoImage(file=r"logo.png")
img1 = img.subsample(6, 7)
tk.Label(win, image=img1).grid(column=3, row=4, rowspan=2)

LEDBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6 , bg='red', text="LED", command=LEDBlink)
LEDBtn.grid(column=9, row=1)

servoBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6 , bg='red', text="servo", command=servoChange)
servoBtn.grid(column=9, row=2)

harmoniqueBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6 , bg='#89CFF0', text="harmo", command=deuxiemeHarmonique)
harmoniqueBtn.grid(column=1, row=3)

flatSharpBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6 ,bg='#89CFF0', text="♯/♭", command=changeFlat)
flatSharpBtn.grid(column=1, row=4)

FSharpBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg='yellow', text="F♯", command=fSharp)
FSharpBtn.grid(column=2, row=1)

gBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg='yellow', text="G", command=g)
gBtn.grid(column=2, row=2)

gSharpBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg='yellow', text="G♯", command=gSharp)
gSharpBtn.grid(column=2, row=3)

aBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg='yellow', text="A", command=a)
aBtn.grid(column=2, row=4)

aSharpBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg='yellow', text="A♯", command=aSharp)
aSharpBtn.grid(column=2, row=5)

aboutBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg='white', text="À propos", command=aboutMsg)
aboutBtn.grid(column=1, row=2)

# quitBtn = tk.Button(win, bd=5, width=6, bg='white', text="Quit", command=win.quit)
# quitBtn.grid(column=1, row=1)

startBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg='green', text="Partir", command=partirAsservissement)
startBtn.grid(column=1, row=5)
#--------------------------------------------
win.mainloop()