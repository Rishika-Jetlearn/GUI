from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("200x300")
window.title("Messages")

#information
messagebox.showinfo("info","hello.")

#warning
messagebox.showwarning("WARNING!","Low battery")

#error
messagebox.showerror("Error :/","Error")

#ask question
print(messagebox.askquestion("IMPORTANT!","Do you like coding?"))

#askokcancel
print(messagebox.askokcancel("Hi","Hi"))

#askyesorno
print(messagebox.askyesno("Yes","Hello."))
window.mainloop()
