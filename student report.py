from tkinter import*
window=Tk()
window.geometry("800x400")
#listbox
lb=Listbox(window)
lb.grid(row=4,column=1)
#frames
frame=Frame(window)
frame.grid(row=2,column=2)

frame2=Frame(window)
frame2.grid(row=2,column=3)

frame3=Frame(window)
frame3.grid(row=3,column=1)
#labels
title=Label(window,text="Student REPORT LOG.")
title.grid(row=1,column=1)

name=Label(window,text="name: ")
name.grid(row=2,column=1)
rollnum=Label(window,text="Roll number: ")
rollnum.grid(row=3,column=1)

science=Label(frame,text="science marks: ")
science.grid(row=1,column=2,padx=40)

maths=Label(frame,text="maths marks: ")
maths.grid(row=2,column=2,padx=40)

percentage=Label(frame,text="percentage: ")
percentage.grid(row=3,column=2,padx=40)

#entrys

name_ent=Entry(frame2)
name_ent.grid(row=2,column=1,pady=15)

rollnum_ent=Entry(frame2)
rollnum_ent.grid(row=3,column=1,pady=15)

science_ent=Entry(frame2)
science_ent.grid(row=4,column=1,pady=15)

maths_ent=Entry(frame2)
maths_ent.grid(row=5,column=1,pady=15)

per_ent=Entry(frame2)
per_ent.grid(row=6,column=1,pady=15)

#buttons
edit=Button(frame3,text="Edit",padx=10)
edit.grid(row=1,column=1)

delete=Button(frame3,text="Delete",padx=20)
delete.grid(row=1,column=2)

save=Button(window,text="Save")
save.grid(row=4,column=2,pady=30,padx=40)

add=Button(window,text="Add/update")
add.grid(row=3,column=3,padx=40)

open=Button(window,text="open")
open.grid(row=3,column=3,padx=40)



window.mainloop()
