from tkinter import*
from tkinter.filedialog import askopenfile,asksaveasfile

def open_file():
    files = [('Text Document', '*.txt')]
    aof=askopenfile(filetypes=files)
    lb.delete(0,END)

    items=aof.readlines()
    print(items)
    for i in items:
        lb.insert(END,i)

def save_file():
    files = [('Text Document', '*.txt')]
    asf=asksaveasfile(filetypes=files)
    for item in lb.get(0,END):
        print(item.strip(),file=asf)
    lb.delete(0,END)

def add():
    user=ent.get()
    lb.insert(END,user)
    ent.delete(0,END)

def dele():
    op=lb.curselection()
    if op:
        lb.delete(op)

window=Tk()
window.geometry("200x300")
window.config(bg="#d1e8e7")
#buttons
save=Button(window,text="save",command=save_file)
save.grid(row=1,column=2)

add=Button(window,text="add",command=add)
add.grid(row=3,column=2)

delete=Button(window,text="delete",command=dele)
delete.grid(row=4,column=3)

open=Button(window,text="open",command=open_file)
open.grid(row=4,column=1)
#Entry
ent=Entry(window)
ent.grid(row=2,column=2)
#list box
lb=Listbox(window)
lb.grid(row=4,column=2)
window.mainloop()