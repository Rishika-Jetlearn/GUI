from tkinter import*
import random
options=["rock","paper","sissors"]
com=0
ply=0
def logic(player):
    global com,ply
    computer=random.choice(options)
    if computer==player:
        result.config(text="Tie")
    elif (computer==rock and player==sissors) or (computer==paper and player==rock) or (computer==sissors and player==paper):
        result.config(text="Computer wins!")
        com=com+1
    else:
        result.config(text="You win!")
        ply=ply+1

    youselec.config(text=f"You selected: {player}")
    comselec.config(text=f"Computer selected: {computer}")
    playersc.config(f"Player score {str(ply)}")
    comsc.config(f"computer score {str(com)}")

window=Tk()
window.geometry("300x400")
window.title("Rock,paper,sissors")

#label
lab=Label(window,text="Rock,Paper,Sissors",foreground="grey",font="Comicsans")
lab.grid(row=1,column=3)

result=Label(window,text="You vs. Computer")
result.grid(row=2,column=3)

your_options=Label(window,text="Your options")
your_options.grid(row=2,column=2)

#buttons
rock=Button(text="rock",command=lambda: logic(options[0]))
rock.grid(row=3,column=3)

paper=Button(text="paper",command=lambda: logic(options[1]))
paper.grid(row=4,column=3)

sissors=Button(text="sissors",command=lambda:logic(options[2]))
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