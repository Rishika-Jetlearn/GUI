from tkinter import*
window=Tk()
window.geometry("300x400")

#listbox
lb=Listbox(window)
lb.grid(row=2,column=1)


#frame
frame=Frame(window)
frame.grid(row=2,column=2)
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



window.mainloop()