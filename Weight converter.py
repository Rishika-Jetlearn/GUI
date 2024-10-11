from tkinter import*
window=Tk()
window.geometry("300x400")
window.title("Weight converter")


#coverting to grams
def covert_gram():
    gr=float(ent.get())
    ans1=gr*1000

#coverting to pounds
def covert_pounds():
    po=float(ent.get)
    ans2=po*2.20462

#coverting to ounce
def convert_ounce():
    ou=float(ent.get)
    ans3=ou*35.274


#label
lab=Label(window,text="Enter weight in kg")
lab.grid(row=0,column=0)
#entry
ent=Entry(window)
ent.grid(row=1,column=0)

#button
conv=Button(window,text="convert")
conv.grid(row=2,column=0)

#gram
g=Label(window,text="gram")
lab.grid(row=1,column=0)

#pounds
p=Label(window,text="pounds")
lab.grid(row=1,column=1)

#ounce
o=Label(window,text="ounce")
lab.grid(row=1,column=2)




window.mainloop()