from tkinter import*
from tkinter.colorchooser import askcolor

class Paint():
    def __init__(self):
        self.window=Tk()
        self.pen=Button(self.window,text="pen",command=self.use_pen)
        self.pen.grid(row=1,column=1)

        self.colour=Button(self.window,text="colour",command=self.use_colour)
        self.colour.grid(row=1,column=2)

        self.eraser=Button(self.window,text="eraser",command=self.use_earaser)
        self.eraser.grid(row=1,column=3)

        self.scale=Scale(self.window,from_=1,to=10,orient="horizontal")
        self.scale.grid(row=1,column=4)

        self.canvas=Canvas(self.window,width=500,height=600,background="white")
        self.canvas.grid(row=2,column=1,columnspan=4)

        self.draw()
        self.window.mainloop()

    def draw(self):
        self.oldx=None
        self.oldy=None
        self.col="black"
        self.width=1
        self.scale.set(self.width)
        self.eraseron=False
        self.activebutton=self.pen
        self.activebutton.config(relief=SUNKEN)
        self.canvas.bind("<B1-Motion>",self.painting)
        self.canvas.bind("<ButtonRelease-1>",self.reset)



    def painting(self,event):
        self.width=self.scale.get()
        c="white" if self.eraseron else self.col
        if self.oldx and self.oldy:
            self.canvas.create_line(self.oldx,self.oldy,event.x,event.y,width=self.width,fill=c,smooth=True,capstyle="round",splinesteps=50)

        self.oldx=event.x
        self.oldy=event.y
    

    def activate_button(self,button,erasermode=False):
        self.activebutton.config(relief=RAISED)
        self.activebutton=button
        self.activebutton.config(relief=SUNKEN)
        self.eraseron=erasermode
        
    def use_pen(self):
        self.activate_button(self.pen)

    def use_colour(self):
        self.col=askcolor(color=self.col)[1]
        print(self.col)

    def use_earaser(self):
        self.activate_button(self.eraser,True)

    def reset(self,event):
        self.oldx=None
        self.oldy=None
        
       
object=Paint()