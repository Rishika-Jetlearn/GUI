from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile,askopenfile
import os
window = Tk()
window.geometry("800x400")




store={}
def add_update():
    n=name_ent.get()
    if n=="":
        messagebox.showerror("Error","Name can not be empty!")
    else:
        if n not in store:
            store[n]=(rollnum_ent.get(),science_ent.get(),maths_ent.get(),per_ent.get())
            lb.insert(END,n)
            clear()
        
        else:
            messagebox.showerror("Error","Same name can not be added again")
            clear()

def reset():
    clear()
    lb.delete(0,END)
    store.clear()
    title.config(text="Adress book")


def clear():
    rollnum_ent.delete(0,END)
    name_ent.delete(0,END)
    science_ent.delete(0,END)
    maths_ent.delete(0,END)
    per_ent.delete(0,END)


def save_info():
    asf=asksaveasfile()
    if asf:
        print(store,file=asf)
    else:
        messagebox.showerror("Error","File not saved :/")

def dele():
    option = lb.curselection()
    print(option)
    if option:
        a=lb.get(option)
        lb.delete(option)
        del store[a]
    else:
        messagebox.showwarning("Warning","Please select an item from the listbox to delete.")

def open_file():
    global store
    reset()
    aof=askopenfile()
    if aof:
        store=eval(aof.read())
        for i in store:
            lb.insert(END,i)
        print(aof.name)
        title.config(text=os.path.basename(aof.name))
    else:
        messagebox.showerror("Error","Something went wrong-please try again")
# Title 
title = Label(window, text="Student REPORT LOG.", font=("Arial", 16, "bold"))
title.grid(row=0, column=0, columnspan=3, pady=10)

# Labels
name = Label(window, text="Name: ")
name.grid(row=1, column=0, padx=10, pady=5)

rollnum = Label(window, text="Roll number: ")
rollnum.grid(row=2, column=0, padx=10, pady=5)

# Entry 
name_ent = Entry(window, width=30)
name_ent.grid(row=1, column=1, pady=5)

rollnum_ent = Entry(window, width=30)
rollnum_ent.grid(row=2, column=1, pady=5)

# Frames
frame = Frame(window)
frame.grid(row=3, column=0, columnspan=2, pady=10)

frame2 = Frame(window)
frame2.grid(row=4, column=0, columnspan=2, pady=10)

frame3 = Frame(window)
frame3.grid(row=5, column=0, columnspan=2, pady=10)

# Subject labels and entry
science = Label(frame, text="Science marks: ")
science.grid(row=0, column=0, padx=10, pady=5)

science_ent = Entry(frame, width=20)
science_ent.grid(row=0, column=1, padx=10, pady=5)

maths = Label(frame, text="Maths marks: ")
maths.grid(row=1, column=0, padx=10, pady=5)

maths_ent = Entry(frame, width=20)
maths_ent.grid(row=1, column=1, padx=10, pady=5)

percentage = Label(frame, text="Percentage: ")
percentage.grid(row=2, column=0, padx=10, pady=5)

per_ent = Entry(frame, width=20)
per_ent.grid(row=2, column=1, padx=10, pady=5)

# Listbox
lb = Listbox(window, height=10, width=50)
lb.grid(row=6, column=0, columnspan=2, pady=10)

# Buttons
add = Button(frame2, text="Add/Update", padx=10,command=add_update)
add.grid(row=0, column=0, padx=10, pady=5)

save = Button(frame2, text="Save", padx=10,command=save_info)
save.grid(row=0, column=1, padx=10, pady=5)

open_btn = Button(frame2, text="Open", padx=10,command=open_file)
open_btn.grid(row=0, column=2, padx=10, pady=5)

edit = Button(frame3, text="Edit", padx=10)
edit.grid(row=0, column=0, padx=10, pady=5)

delete = Button(frame3, text="Delete", padx=10,command=dele)
delete.grid(row=0, column=1, padx=10, pady=5)

# Run the application
window.mainloop()