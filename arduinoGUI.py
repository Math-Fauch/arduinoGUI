#-----------------------------------------------------
# GUI to control the frequency with an arduino
#-----------------------------------------------------
import tkinter as tk
from tkinter import messagebox, StringVar, PhotoImage
import serial
import numpy as np
# global variables==================================================
deuxiemeHarmoniqueBool = False
flatDisplayBool = True
testUIBool = False
ledValue = b'L'
servoPos = b'f'
# Setup connection Arduino==========================================
ser = serial.Serial('COM7', 9800, timeout=1)
# Functions=========================================================
def LEDBlink():
    while ser.read() != b"o":
        ser.write(str(frequency.get()).encode())
#--------------------------------------------
def partirAsservissement():
    global testUIBool
    if testUIBool:
        times = np.empty([5])
        # test f#
        accordText.set("F♯")
        ser.write("f#TestStart\n")
        time = ser.read_until(" f#TestDone\n")
        times[0] = time
        entretienText.set(str(time) + "sec")
        # test g
        accordText.set("G")
        ser.write("gTestStart\n")
        time = ser.read_until(" gTestDone\n")
        times[1] = time
        entretienText.set(str(time) + "sec")
        # test g#
        accordText.set("G♯")
        ser.write("g#TestStart\n")
        time = ser.read_until(" g#TestDone\n")
        times[2] = time
        entretienText.set(str(time) + "sec")
        # test a
        accordText.set("A")
        ser.write("aTestStart\n")
        time = ser.read_until(" aTestDone\n")
        times[3] = time
        entretienText.set(str(time) + "sec")
        # test a#
        accordText.set("A♯")
        ser.write("aTestStart\n")
        time = ser.read_until(" aTestDone\n")
        times[4] = time
        entretienText.set(str(time) + "sec")
        # temps moyen
        accordText.set("temps moyen:")
        entretienText.set(str(np.mean(times)) + "sec")
    else:
        freqString = frequency.get()
        freqText.set(f"{freqString} Hz")
#--------------------------------------------
# def servoChange():
#     global servoPos
#     if servoPos == b'f':
#         ser.write(b'F')
#         servoPos = b'F'
#     else:
#         ser.write(b'f')
#         servoPos = b'f'
#--------------------------------------------
def testUI():
    global testUIBool
    if testUIBool:
        # change text
        harmoText.set("première\nharmonique")
        accordText.set("0 Hz")
        freqText.set("auto-accordé")
        entretienText.set("auto-entretenu")
        entretienLabel.configure(bg="red")
        accordLabel.configure(bg="red")
        # enable buttons/scale
        fSharpBtn.configure(state="normal")
        gBtn.configure(state="normal")
        gSharpBtn.configure(state="normal")
        aBtn.configure(state="normal")
        aSharpBtn.configure(state="normal")
        frequency.configure(state="normal")
        # change bool
        testUIBool = False
    else:
        # change text
        harmoText.set("Mode Test")
        accordText.set("")
        freqText.set("temps d'accord:")
        entretienText.set("0 sec")
        entretienLabel.configure(bg="#F0F0F0")
        accordLabel.configure(bg="#F0F0F0")
        # disable buttons/scale
        fSharpBtn.configure(state="disabled")
        gBtn.configure(state="disabled")
        gSharpBtn.configure(state="disabled")
        aBtn.configure(state="disabled")
        aSharpBtn.configure(state="disabled")
        frequency.configure(state="disabled")
        # change bool
        testUIBool = True
#--------------------------------------------
def deuxiemeHarmonique():
    global deuxiemeHarmoniqueBool
    if deuxiemeHarmoniqueBool:
        frequency.configure(from_=90.00, to=120.00)
        frequency.set(90.00)
        harmoText.set("première\nharmonique")
        deuxiemeHarmoniqueBool = False
    else:
        frequency.configure(from_=180.00, to=240.00)
        frequency.set(180.00)
        harmoText.set("deuxième\nharmonique")
        deuxiemeHarmoniqueBool = True
#--------------------------------------------
def changeFlat():
    global flatDisplayBool
    if flatDisplayBool:
        fSharpBtn.configure(text="G♭")
        gSharpBtn.configure(text="A♭")
        aSharpBtn.configure(text="B♭")
        flatDisplayBool = False
    else:
        fSharpBtn.configure(text="F♯")
        gSharpBtn.configure(text="G♯")
        aSharpBtn.configure(text="A♯")
        flatDisplayBool = True
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
win.resizable(False, False)
win.configure(bg="#F0F0F0")
harmoText = StringVar()
harmoText.set("première\nharmonique")
freqText = StringVar()
freqText.set("0 Hz")
accordText = StringVar()
accordText.set("auto-accordé")
entretienText = StringVar()
entretienText.set("auto-entretenu")
#--------------------------------------------
# Scale widget
frequency = tk.Scale(win, bd=5, resolution=0.01, from_=90.00, to=120.00, length=220, orient=tk.VERTICAL)
frequency.grid(column=6, row=1, rowspan=5)

# Label widget
harmoLabel = tk.Label(win, textvariable=harmoText)
harmoLabel.grid(column=3, row=1, rowspan=2)

freqLabel = tk.Label(win, textvariable=freqText)
freqLabel.grid(column=3, row=3)

accordLabel = tk.Label(win, textvariable=accordText, bg="red")
accordLabel.grid(column=4, row=1, rowspan=2)

entretienLabel = tk.Label(win, textvariable=entretienText, bg="red")
entretienLabel.grid(column=4, row=3)

# Image widget
img = PhotoImage(file=r"logo.png")
img1 = img.subsample(6, 7)
tk.Label(win, image=img1).grid(column=3, row=4, rowspan=2, columnspan=2)

# Button widgets
# ----------------------- ARDUINO TEST  -----------------------------------------------------------------
LEDBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6 , bg='red', text="LED", command=LEDBlink)
LEDBtn.grid(column=9, row=1)

# servoBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6 , bg='red', text="servo", command=servoChange)
# servoBtn.grid(column=9, row=2)
# ----------------------- ARDUINO TEST  -----------------------------------------------------------------

harmoniqueBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6 , bg='#89CFF0', text="harmo", command=deuxiemeHarmonique)
harmoniqueBtn.grid(column=1, row=3)

flatSharpBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6 ,bg='#89CFF0', text="♯/♭", command=changeFlat)
flatSharpBtn.grid(column=1, row=4)

fSharpBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg='yellow', text="F♯", command=fSharp)
fSharpBtn.grid(column=2, row=1)

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

startBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg='green', text="Partir", command=partirAsservissement)
startBtn.grid(column=1, row=5)

testBtn = tk.Button(win, bd=10, padx=5, pady=5, width=6, bg="white", text="Test", command=testUI)
testBtn.grid(column=1, row=1)
#--------------------------------------------
win.mainloop()