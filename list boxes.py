from tkinter import*

def show():
    select=lb.curselection()

    print(select)
    print(lb.get(select))

window=Tk()
window.geometry("500x500")
lb=Listbox(window)
lb.pack()


lb.insert(0,"phone")
lb.insert(1,"ipad")
lb.insert(2,"monitor")
lb.insert(3,"tv")

b=Button(window,text="go",command=show)
b.pack()




window.mainloop()