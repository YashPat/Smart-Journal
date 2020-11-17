from tkinter import *
import tkinter
from tkinter import messagebox
from manager import manager
import datetime
from textblob import TextBlob
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt


#button(window,text = "Text", width = 12, bg = "black", fg = "white", command = def)
#button.place(x,y)
#tkinter.messagebox.showinfo("Title","Text")


man = manager()

def log(x):
    man.logentry(x)
    rating = str(round(TextBlob(x).polarity,1))
    man.logRating(rating)
    man.logDates(str(datetime.date.today()))

def analyze():
    plt.plot(man.getX(),man.getY())
    plt.xlabel("Entry Dates")
    plt.ylabel("Happiness Rating")
    plt.title("Emotional Analysis")
    plt.show()

def journ():
    #SETUP
    journalWin = Tk()
    journalWin.geometry("+100+100")
    #textbox
    tBox = Text(journalWin,relief = RIDGE, borderwidth = 2)
    tBox.grid(row = 0, column = 0, columnspan = 2, sticky = N)
    saveBut = Button(journalWin,text = "Complete Entry", command = lambda: [log(tBox.get("1.0",END)), journalWin.destroy(), setup()])
    saveBut.grid(row = 1, column = 0, sticky = S)
    menuBut = Button(journalWin,text = "Return to Menu", command = lambda: [journalWin.destroy(), setup()])
    menuBut.grid(row = 1, column = 1, sticky = S)

    #buttons
    #saveBut = Button(journalWin, text = "Complete Entry", width = 12, bg = "white", fg = "black", click = sendtomanager(tBox.get("1.0",END))).grid(row = 1, column = 0, sticky = S)


    journalWin.mainloop()

def test():
    print("TEST")

def sendtomanager(cont):
    man = manager()
    man.logentry(cont)


def readOld():
    reading = Tk()
    reading.geometry("+100+100")
    tBox = Text(reading,relief = RIDGE, borderwidth = 2 )
    tBox.grid(row = 0, column = 0, sticky = N)
    tBox.insert(0.0,man.readEntry())
    menuBut = Button(reading,text = "Return to Menu", command = lambda: [reading.destroy(), setup()])
    menuBut.grid(row = 1, column = 0, sticky = S)
    reading.mainloop()

def setup():

    window = Tk()
    window.geometry("+100+100")

    entry = Button(window, text="New Entry", width=12, bg="white", fg="black", command= lambda: [window.destroy(), journ()])
    entry.grid(row = 0, column = 0, sticky = N)
    old = Button(window, text = "Read Old Entries", width = 12, bg = "white", fg = "black", command = lambda: [window.destroy(), readOld()])
    old.grid(row = 1, column = 0, sticky = N)
    analysis = Button(window, text = "Analysis", width = 12, bg = "white", fg = "black", command = lambda: [window.destroy(),analyze()])
    analysis.grid(row = 2, column = 0, sticky = S)
    window.mainloop()


setup()