from  tkinter import*
import tkinter.font as f
window=Tk()
window.geometry("300x400")
window.title("Facts")
hf=f.Font(family="Courier",size=24,weight="bold")


burger=Button(text="rock")
burger.grid(row=3,column=3)

pizza=Button(text="paper")
pizza.grid(row=4,column=3)

chips=Button(text="sissors")
chips.grid(row=5,column=3)
window.mainloop