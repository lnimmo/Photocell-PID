from tkinter import *
import serial

# Work in progress

mySerial = serial.Serial('COM6', 9600, timeout=1)
root = Tk()

def leftClick(event):
    print("Running Arduino")
    data = mySerial.readline().decode('ascii')
    print(data)


frame = Frame(root, width=300, height=250)

frame.bind("<Button-1>", leftClick)
frame.pack()
root.mainloop() 
