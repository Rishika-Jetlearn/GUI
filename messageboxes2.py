from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("200x300")
window.title("Messages")

#information
messagebox.showinfo("info","Battery low.")

#warning
messagebox.showwarning("WARNING!","Low battery")

#error
messagebox.showerror("Error :/","Error")


#askokcancel
print(messagebox.askokcancel("!","Turn on battry saver?"))

#askyesorno
print(messagebox.askyesno("Battery saver","No battery saver found,try again?"))


#ask question
print(messagebox.askquestion("IMPORTANT!","Do you like coding?"))
window.mainloop()