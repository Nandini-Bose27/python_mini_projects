import random
from tkinter import *
root=Tk()
root.geometry("700x500")
l1=Label(root,font=("Times",200))
def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()
    
b1=Button(root,text="let's roll",command=roll)
b1.place(x=350,y=0)


root.mainloop()
