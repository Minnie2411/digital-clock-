#importing whole module
from tkinter import *
from tkinter.ttk  import *

#importing strftime function to retrieve system's time
from time import strftime

#creating tkinter window
root=Tk()
root.title( 'Clock' )

#this function is used to display time on the label
def time():
    string=strftime('%H:%M:%S %p %A   %B')
    lbl.config(text=string)
    lbl.after(1000,time)


lbl = Label(root, font = ('chiller', 40, 'bold'), background = 'purple',foreground = 'white')

#placing clock at the centre of the tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()
