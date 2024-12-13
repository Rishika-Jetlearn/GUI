from tkinter import*

def show():
    select=lb.curselection()

    print(select)
    print(lb.get(select))

window=Tk()
window.geometry("500x500")

sb=Scrollbar(window,width=30)

lb=Listbox(window,yscrollcommand=sb.set)
lb.pack()
sb.pack(side=LEFT,fill=Y)
sb.config(command=lb.yview)

lb.insert(0,"phone")
lb.insert(1,"ipad")
lb.insert(2,"monitor")
lb.insert(3,"tv")
lb.insert(4,"phone")
lb.insert(5,"ipad")
lb.insert(6,"monitor")
lb.insert(7,"tv")
lb.insert(8,"ipad")
lb.insert(9,"monitor")
lb.insert(10,"tv")

b=Button(window,text="go",command=show)
b.pack()




window.mainloop()