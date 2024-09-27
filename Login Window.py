#login page
from tkinter import*
#create main window
window=Tk()
#size of window
window.geometry("500x400")
#title
window.title("Login")
#background colour
window.config(background="lightblue")
#labels
us=Label(window,text="User")
#place
us.place(x=50,y=50)
#entry
type=Entry(window)
type.place(x= 100 ,y= 50)
#password
password=Label(window,text="Password")
password.place(x=50,y=100)
ps=Entry(window,show="*")
ps.place(x=150,y=100)
#button
button=Button(window,text="Login")
button.place(x=50,y=150 )
close=Button(window,text="Close",command=window.destroy)
close.place(x=250,y=150)
#display window

window.mainloop()