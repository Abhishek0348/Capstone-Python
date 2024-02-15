import tkinter as tk
from tkinter import messagebox
import random

# Creating the main window
root=tk.Tk()
root.geometry("400x400")
root.title("Guess The Number")

#Generating a randomm no.
secretno = random.randint(1,20)

#Creating a fun for the game 
def check_Guess():
    guess = int(guess_entry.get())
    if(guess == secretno):
        messagebox.showinfo(title="Result!",message="Congratulations You Guessed it Right.")
    elif(guess < secretno):
        messagebox.showinfo(title="Result!",message="Your Guess is too Low.\nTry Again.")
    elif(guess > secretno):
        messagebox.showinfo(title="Result!",message="Your Guess is too High.\nTry Again")

    
guess_Label = tk.Label(root, text="Guess The no. between 1 to 20\nEnter Your Guess : ")
guess_Label.pack()
guess_entry = tk.Entry(root)
guess_entry.pack()

check_button = tk.Button(root, text="Check", command=check_Guess)
check_button.pack()


root.mainloop()


