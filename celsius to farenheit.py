from tkinter import*
def convert():
    celsius=float(type.get())
    farenheit=celsius*9/5+32
    ans.config(text=farenheit)
window=Tk()
window.geometry("600x800")
window.title("Celsius to Farenheit")
window.config(background="#d3ded6")

lab=Label(window,text="Enter temperature in celsius",font=("comicsans",24,"bold"))
lab.grid(row=1,column=0)
type=Entry(window)
type.grid(row=1,column=1)


button=Button(window,text="Convert",bg="lightgreen",fg="black",command=convert)
button.grid(row=2,column=0,padx=50,pady=200)
close=Button(window,text="Close",command=exit,bg="lightgreen",fg="black")
close.grid(row=2,column=1,padx=50,pady=250)

ans=Label(window)
ans.grid(row=3,column=0)



window.mainloop()