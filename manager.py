from tkinter import *
import datetime

class manager:

    def __init__(self):
        pass

    def logentry(self,content):
        count = 0
        dateCalc = str(datetime.date.today())
        output = ""
        f = open("testEntry.txt","a+")
        f.write(dateCalc+": \n")
        for char in content:
            output += char
            count += 1
            if count % 80 == 0:
                output += "\n"
        f.write(output)
        f.write("--------------------------------------------------------------------------------\n")
        f.close()

    def readEntry(self):
        f = open("testEntry.txt","r")
        retVal = ""
        for x in f.readlines():
            retVal += x

        return retVal

    def logRating(self,rate):
        f = open("ratings.txt","a+")
        f.write(rate+"\n")

    def logDates(self,date):
        f = open("dates.txt","a+")
        f.write(date+"\n")

    def getX(self):
        f = open("dates.txt","r")
        retVal = []
        for x in f.readlines():
            retVal.append(x.strip())
        return retVal

    def getY(self):
        f = open("ratings.txt","r")
        retVal = []
        for x in f.readlines():
            retVal.append(float(x.strip()))
        return retVal