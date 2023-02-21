#-----------------------------------------------------
# GUI to turn ON blue/red LED with brightness control
#-----------------------------------------------------
import tkinter as tk
from tkinter import messagebox
from pyfirmata import Arduino, PWM
from time import sleep

deuxiemeHarmoniqueBool = 0

# Functions=========================================================
def blueLED():
    delay = float(LEDtime.get())
    brightness = float(LEDbright.get())
    blueBtn.config(state = tk.DISABLED)
    board.digital[3].write(brightness/100.0)
    sleep(delay)
    board.digital[3].write(0)
    blueBtn.config(state = tk.ACTIVE)
#--------------------------------------------
def redLED():
    delay = float(LEDtime.get())
    brightness = float(LEDbright.get())
    redBtn.config(state = tk.DISABLED)
    board.digital[9].write(brightness/100.0)
    sleep(delay)
    board.digital[9].write(0)
    redBtn.config(state = tk.ACTIVE)
#--------------------------------------------
def deuxiemeHarmonique():
    global deuxiemeHarmoniqueBool
    if deuxiemeHarmoniqueBool:
        LEDbright.configure(from_=90, to=120)
        deuxiemeHarmoniqueBool = False
    else:
        LEDbright.configure(from_=180, to=240)
        deuxiemeHarmoniqueBool = True
#--------------------------------------------
def aboutMsg():
    messagebox.showinfo("About",
    "Logic Don't Care Software\nLED Control Ver 1.0\nAugust 2022")
#=================================================================
# Arduino board connected to serial port COM3
board = Arduino("COM3")
# set mode of Arduino pins D3 & D5 for PWM
board.digital[3].mode = PWM
board.digital[9].mode = PWM
#--------------------------------------------
# initialize window with title & size
win = tk.Tk()
win.title("LED Control")
win.minsize(235,150)
#--------------------------------------------
# Entry widget
LEDtime = tk.Entry(win, bd=6, width=8)
LEDtime.grid(column=1, row=1)
# Label widget
tk.Label(win, text="LED ON Time (sec)").grid(column=2, row=1)
#--------------------------------------------
# Scale widget
LEDbright = tk.Scale(win, bd=5, from_=90, to=120, orient=tk.HORIZONTAL)
LEDbright.grid(column=1, row=2)
# Label widget
tk.Label(win, text="fréquence").grid(column=2, row=2)
#--------------------------------------------
# Button widgets
blueBtn = tk.Button(win, bd=5, bg='#89CFF0', text="Harmo", command=deuxiemeHarmonique)
blueBtn.grid(column=1, row=3)

redBtn = tk.Button(win, bd=5, bg='red', text="LED ON", command=redLED)
redBtn.grid(column=2, row=3)

aboutBtn = tk.Button(win, text="About", command=aboutMsg)
aboutBtn.grid(column=1, row=4)

quitBtn = tk.Button(win, text="Quit", command=win.quit)
quitBtn.grid(column=2, row=4)
#--------------------------------------------
win.mainloop()