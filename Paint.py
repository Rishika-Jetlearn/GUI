from tkinter import*

class Paint():
    def __init__(self):
        self.window=Tk()
        self.pen=Button(self.window,text="pen")
        self.pen.grid(row=1,column=1)

        self.colour=Button(self.window,text="colour")
        self.colour.grid(row=1,column=2)

        self.eraser=Button(self.window,text="eraser")
        self.eraser.grid(row=1,column=3)

        self.scale=Scale(self.window,from_=1,to=5,orient="horizontal")
        self.scale.grid(row=1,column=4)

        self.canvas=Canvas(self.window,width=500,height=600,background="white")
        self.canvas.grid(row=2,column=1,columnspan=4)

        self.window.mainloop()

    def draw(self):
        self.oldx=None
        self.oldy=None
        self.col="black"
        self.width=1
        self.eraseron=False
        self.activebutton=self.pen
    def activate_button(self,button,erasermode=False):
        self.activebutton.config(relief=RAISED)
        self.activebutton=button
        self.activebutton.config(relif=SUNKEN)
        self.eraseron=erasermode


        
       
object=Paint()