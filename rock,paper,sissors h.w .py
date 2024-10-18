from tkinter import*
import random

def roc():

window=Tk()
window.geometry("300x400")
window.title("Rock,paper,sissors")

#label
lab=Label(window,text="Rock,Paper,Sissors",foreground="grey",font="Comicsans")
lab.grid(row=1,column=3)

your_options=Label(window,text="Your options")
your_options.grid(row=2,column=2)

#buttons
rock=Button(text="rock")
rock.grid(row=3,column=3)

paper=Button(text="paper")
paper.grid(row=4,column=3)

sissors=Button(text="sissors")
sissors.grid(row=5,column=3)

#score
score=Label(text="Score: ")
score.grid(row=6,column=2)

youselec=Label(text="You selected: ")
youselec.grid(row=8,column=3)

comselec=Label(text="Computer selected: ")
comselec.grid(row=9,column=3,pady=30)

playersc=Label(text="Player score",pady=30)
playersc.grid(row=10,column=3)

comsc=Label(text="computer score")
comsc.grid(row=11,column=3)



window.mainloop()