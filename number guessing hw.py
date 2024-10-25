from tkinter import*
import random
com=random.randint(1,20)

def restart():
    global com
    com=random.randint(1,20)

def computer():
    num=int(user.get())
    if num<com:
        result.config(text="Your guess is too low")
    elif num>com:
        result.config(text="Your guess is too high")
    elif num==com:
        result.config(text="You are correct!")




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
Enter=Button(window,text="enter",background="black",foreground="green",command=computer)
Enter.grid(row=2,column=1)

new=Button(window,text="Restart",command=restart)
new.grid(row=2,column=2)

#ans
result=Label(window)
result.grid(row=3,column=1)
window.mainloop()
