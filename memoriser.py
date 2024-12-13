from tkinter import*
window=Tk()
window.geometry("200x300")
window.config(bg="#d1e8e7")
#buttons
save=Button(window,text="save")
save.grid(row=1,column=2)

add=Button(window,text="add")
add.grid(row=3,column=2)

delete=Button(window,text="delete")
delete.grid(row=4,column=3)

open=Button(window,text="open")
open.grid(row=4,column=1)
#Entry
ent=Entry(window)
ent.grid(row=2,column=2)
#list box
lb=Listbox(window)
lb.grid(row=4,column=2)
window.mainloop()