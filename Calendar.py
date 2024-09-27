from tkinter import*
import calendar
def cal():
    win=Tk()
    win.title("Calendar")
    win.geometry("600x800")
    win.config(background="lightgreen")

    year=int(type.get())
    info=calendar.calendar(year)
    txt=Text(win,height=700)
    txt.insert(END,info)
    txt.pack(padx=0,pady=50)
    window.mainloop()
window=Tk()
window.geometry("500x400")
window.title("Calendar")
window.config(background="#d3ded6")
lab=Label(window,text="Calendar",font=("comicsans",24,"bold"))
lab.grid(row=0,column=0,pady=25,columnspan=2)
us=Label(window,text="Enter year: ",padx=30)
us.grid(row=1,column=0)
type=Entry(window)
type.grid(row=1,column=1,padx=20)
button=Button(window,text="show",bg="lightgreen",fg="black",command=cal)
button.grid(row=2,column=0,pady=30)
close=Button(window,text="Close",command=exit,bg="lightgreen",fg="black")
close.grid(row=2,column=1,pady=30)

window.mainloop()