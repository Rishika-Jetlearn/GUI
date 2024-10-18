from tkinter import*
from time import strftime
def time():
    clock=strftime("%H:%M:%S")
    label.config(text=clock)
    label.after(1000,time)
window=Tk()
window.geometry("500x200")
label=Label(window,foreground="black",background="lightyellow",font=("comicsans",72,"bold"))
label.pack()
time()
window.mainloop()
