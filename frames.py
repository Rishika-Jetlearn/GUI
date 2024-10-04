from  tkinter import*
import tkinter.font as f
window=Tk()
window.geometry("300x400")
window.title("Frames")
hf=f.Font(family="Courier",size=24,weight="bold")
icecream=Label(window,text="chocos and Ice cream",font=hf)
icecream.pack()

topfrme=Frame(window)
topfrme.pack()
button1=Button(topfrme,text="Choco")
button1.pack()
button2=Button(topfrme,text="Vinilla")
button2.pack(side="left")
button3=Button(topfrme,text="Mango")
button3.pack(side="right")


bottomframe=Frame(window)
bottomframe.pack(side="bottom")
but1=Button(bottomframe,text="White choco")
but1.pack()

but2=Button(bottomframe,text="almound")
but2.pack(side="bottom")

but3=Button(bottomframe,text="rasins")
but3.pack(side="bottom")
window.mainloop()