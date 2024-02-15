
from tkinter import *
import random
 
#create tkinter instance
root=Tk()
#define geometry
root.geometry("400x400")
root.title("Dice Rool")
 

l1=Label(root,font=("Helvetica",260))
 
def roll():
    
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(dice)}')
    l1.pack()
     
b1=Button(root,text="Roll the Dice!",foreground='black',command=roll,bg='yellow')
b1.place(x=350,y=0)
b1.pack()
 
root.mainloop()