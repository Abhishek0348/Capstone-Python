import pyshorteners
import tkinter as tk


root=tk.Tk()
root.geometry("400x400")
root.title("URL SHORTNER")

def urlshorner():
    url = input()
    print(url.tinyurl.short())

root.mainloop()

