from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile,askopenfile
import os
window=Tk()


#dictionary
store={}
def add_update():
    n=name_ent.get()
    print(n,"hi")
    if n=="":
        messagebox.showerror("Error","Name can not be empty!")
    else:
        if n not in store:
            store[n]=(birthday_ent.get(),adress_ent.get(),mobile_ent.get(),email_ent.get())
            lb.insert(END,n)
            clear()
        
        else:
            messagebox.showerror("Error","Same name can not be added again")

def clear():
    birthday_ent.delete(0,END)
    name_ent.delete(0,END)
    adress_ent.delete(0,END)
    mobile_ent.delete(0,END)
    email_ent.delete(0,END)

def reset():
    clear()
    lb.delete(0,END)
    store.clear()
    title.config(text="Adress book")


def save_info():
    asf=asksaveasfile()
    if asf:
        print(store,file=asf)
        reset()
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
#window.geometry("200x350")
#listbox
lb=Listbox(window)
lb.grid(row=2,column=1)
#frames
frame=Frame(window)
frame.grid(row=2,column=2)

frame2=Frame(window)
frame2.grid(row=2,column=3)

frame3=Frame(window)
frame3.grid(row=3,column=1)
#labels
title=Label(window,text="Adress book")
title.grid(row=1,column=1)

name=Label(frame,text="name: ")
name.grid(row=2,column=1,pady=15)

adress=Label(frame,text="adress: ")
adress.grid(row=3,column=1,pady=15)

mobile=Label(frame,text="mobile: ")
mobile.grid(row=4,column=1,pady=15)

email=Label(frame,text="email: ")
email.grid(row=5,column=1,pady=15)

birthday=Label(frame,text="birthday: ")
birthday.grid(row=6,column=1,pady=15)

#entrys

name_ent=Entry(frame2)
name_ent.grid(row=2,column=1,pady=15)

adress_ent=Entry(frame2)
adress_ent.grid(row=3,column=1,pady=15)

mobile_ent=Entry(frame2)
mobile_ent.grid(row=4,column=1,pady=15)

email_ent=Entry(frame2)
email_ent.grid(row=5,column=1,pady=15)

birthday_ent=Entry(frame2)
birthday_ent.grid(row=6,column=1,pady=15)

#buttons
edit=Button(frame3,text="Edit",padx=10)
edit.grid(row=1,column=1)

delete=Button(frame3,text="Delete",padx=20,command=dele)
delete.grid(row=1,column=2)

save=Button(window,text="Save",command=save_info)
save.grid(row=4,column=1,pady=30,padx=40,columnspan=2)

add=Button(window,text="Add/update",command=add_update)
add.grid(row=3,column=3,padx=40)

open=Button(window,text="Open",command=open_file)
open.grid(row=1,column=2)



window.mainloop()
