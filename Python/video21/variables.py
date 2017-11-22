from tkinter import *
from tkinter import messagebox

def get_data(event=None):
    print("string: ", strVar.get())
    print("integer: ", intVar.get())
    print("double: ", dblVar.get())
    print("boolean: ", boolVar.get())

def bind_button(event=None):
    if boolVar.get():
        getDataButton.unbind('<Button-1>')
    else:
        getDataButton.bind('<Button-1>', get_data)

root = Tk()

strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set('Enter String here')
intVar.set('Enter Integer here')
dblVar.set('Enter Double here')
boolVar.set(True)

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

theChechBut = Checkbutton(root, text='on/off', variable=boolVar)
theChechBut.bind('<Button-1>', bind_button)
theChechBut.pack(side=LEFT)

getDataButton = Button(root, text='Get Data')
getDataButton.bind('<Button-1>', get_data)
getDataButton.pack(side=LEFT)

root.mainloop()



