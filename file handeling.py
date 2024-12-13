from tkinter import* 
from tkinter.filedialog import askopenfile,asksaveasfile

def open_file():
    aof=askopenfile()
    content=aof.read()
    print(content)
def save_file():
    files = [('All Files', '*.*'),
            ('Python Files', '*.py'),
            ('Text Document', '*.txt')]
    asf=asksaveasfile(filetypes=files)

window=Tk()
b1=Button(window,text="open",command=open_file)
b1.pack()
b2=Button(window,text="save",command=save_file)
b2.pack()

window.mainloop()