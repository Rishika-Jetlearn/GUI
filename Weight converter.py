from tkinter import*

#coverting
def convert():
    kg=float(ent.get())
    ans1=kg*1000

    ans2=kg*2.20462

    ans3=kg*35.274

    gra.config(text=ans1)
    pou.config(text=ans2)
    oun.config(text=ans3)
window=Tk()
window.geometry("300x400")
window.title("Weight converter")


#label
lab=Label(window,text="Enter weight in kg")
lab.grid(row=0,column=0)
#entry
ent=Entry(window)
ent.grid(row=0,column=1)

#button
conv=Button(window,text="convert",command=convert)
conv.grid(row=1,column=1)

#gram
g=Label(window,text="gram")
g.grid(row=2,column=0)

#pounds
p=Label(window,text="pounds")
p.grid(row=2,column=1)

#ounce
o=Label(window,text="ounce")
o.grid(row=2,column=2)

#ans1
gra=Label(window)
gra.grid(row=3,column=0)
#ans2
pou=Label(window)
pou.grid(row=3,column=1)
#ans3
oun=Label(window)
oun.grid(row=3,column=2)



window.mainloop()