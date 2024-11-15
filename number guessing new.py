from tkinter import*
from tkinter import messagebox
import random
com=random.randint(1,20)

def computer():
    num=int(user.get())
    if num<com:
        messagebox.showinfo("Low","Your guess is too low")
    elif num>com:
        messagebox.showinfo("High","Your guess is too high")
    elif num==com:
        messagebox.showinfo("Congrats!","You are correct!")

def restart():
    global com
    com=random.randint(1,20)
    branch.pack_forget()
    root.pack()

def start():
    messagebox.showinfo("Name",f"Hi! Welcome to the game {name.get()}...so i am thinking of a number from 1-20 and it's up to you to guess it.")
    root.pack_forget()
    branch.pack()


window=Tk()
window.geometry("300x400")
window.title("Number guessing game")
window. configure(bg="#afedd3")

#frame
root=Frame(window,bg="#afedd3")
root.pack()

welcome=Label(root,text="Welcome to the game!")
welcome.grid(row=1,column=1,pady=100)

ask=Label(root,text="What is your name?")
ask.grid(row=2,column=1)

name=Entry(root)
name.grid(row=3,column=1)

go=Button(root,text="Go!",command=start)
go.grid(row=4,column=1)

#frame2
branch=Frame(window)
#labels
guess=Label(branch,text="Guess:  ")
guess.grid(row=1,column=1)

#Entry
user=Entry(branch)
user.grid(row=1,column=2)

#button
Enter=Button(branch,text="enter",background="black",foreground="green",command=computer)
Enter.grid(row=2,column=1)

new=Button(branch,text="Restart",command=restart)
new.grid(row=2,column=2)


window.mainloop()