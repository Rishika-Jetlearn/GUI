from tkinter import*
import random
from time import strftime
digits=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
def colour():
  clr="#"
  for i in range(6):
    hex=random.choice(digits)
    clr=clr+hex
  return clr
def time():
    clock=strftime("%H:%M:%S")
    label.config(text=clock,background=colour())
    label.after(1000,time)
window=Tk()
window.geometry("500x200")
label=Label(window,foreground="black",background=colour(),font=("comicsans",72,"bold"))
label.pack()
time()
window.mainloop()