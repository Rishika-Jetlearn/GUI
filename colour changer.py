from tkinter import *
import random


window = Tk()
window.geometry("300x400")
window.title("Background Color Changer")

# add  
def add():
    user = ent.get()
    
    lb.insert(END, user)
    ent.delete(0, END)

#  delete 
def dele():
    op = lb.curselection()
    if op:
        lb.delete(op)

"""# Hexadecimal digits 
hex_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

#  change  background color
def colour():
    clr = "#"
    for _ in range(6):
        clr += random.choice(hex_digits)
    window.config(bg=clr)"""
def colour():
    clr=lb.curselection()
    b=lb.get(clr)
    window.config(bg=b)

# Buttons
add_button = Button(window, text="Add", command=add)
add_button.grid(row=3, column=2, padx=100)

delete_button = Button(window, text="Delete", command=dele)
delete_button.grid(row=4, column=2)

background_button = Button(window, text="Change Background Colour",command=colour)
background_button.grid(row=6, column=2, padx=100)

# Entry   
ent = Entry(window)
ent.grid(row=2, column=2)

# Listbox 
lb = Listbox(window)
lb.grid(row=5, column=2)


window.mainloop()
