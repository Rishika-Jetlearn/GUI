from tkinter import*
import random
def computer():
    com=random.randint(1,20)

    if user<com:
        low.config(text="Your guess is too low")
    elif user<com:
        high.config(text="Your guess is too high")
    elif user==com:
        right.config(text="You are correct!")
    else:
        error.config(text="Please enter a number from 1-20")





window=Tk()
window.geometry("300x400")
window.title("Number guessing game")
window. configure(bg="#afedd3")

#labels
guess=Label(window,text="Guess:  ")
guess.grid(row=1,column=1)

#Entry
user=Entry(window)
user.grid(row=1,column=2)

#button
Enter=Button(window,text="enter",background="black",foreground="green")
Enter.grid(row=2,column=1)


#ans
high=Label(window)
high.grid(row=3,column=1)
low=Label(window)
low.grid(row=3,column=1)
right=Label(window)
right.grid(row=3,column=1)


window.mainloop()
