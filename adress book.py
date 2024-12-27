from tkinter import*
window=Tk()
window.geometry("500x400")
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

delete=Button(frame3,text="Delete",padx=20)
delete.grid(row=1,column=2)

save=Button(window,text="Save")
save.grid(row=4,column=2,pady=30,padx=40)

add=Button(window,text="Add/update")
add.grid(row=3,column=3,padx=40)



window.mainloop()text="email: ")
email.grid(row=5,column=1,pady=15)

birthday=Label(frame,text="birthday: ")
birthday.grid(row=6,column=1,pady=15)



window.mainloop()
