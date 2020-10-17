from tkinter import Tk, Frame, Text, Label, Button, END
from funtions import *

def addInfo():        
    sentence = analice_Sentence(commandBox.get(1.0, END))


root = Tk()
root.title("Ingreso de datos")

principalFrame = Frame(root)
principalFrame.pack()

intructionLabel = Label(principalFrame, text = "Ingrese su sentencia: ")
intructionLabel.grid(row = 0, column = 0, padx = 10, pady = 10)

commandBox = Text(principalFrame, width = 40, height = 10)
commandBox.grid(row = 1, column = 0, sticky = "nsew")

controlFrame = Frame(principalFrame)
controlFrame.grid(row = 2, column = 0)

ButtonAdd = Button(controlFrame, text = "Añadir", width = 20, command = addInfo)
ButtonAdd.grid(row = 0, column = 0)

ButtonClear = Button(controlFrame, text = "Limpiar", width = 20)
ButtonClear.grid(row = 0, column = 1)

root.mainloop()