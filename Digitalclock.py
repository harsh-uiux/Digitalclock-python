from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")

def get_time():
    timevar = time.strftime("%I:%M:%S %p")
    clock.config(text=timevar)
    clock.after(200,get_time)
    
clock = Label(master, font=("Calibri",90),bg="grey",fg="white")
clock.pack()

get_time()

master.mainloop() 
