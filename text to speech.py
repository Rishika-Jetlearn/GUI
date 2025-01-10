from tkinter import*
from gtts import gTTS
import os
window=Tk()
window.geometry("100x200")
window.configure(bg="lightgreen")

def speech():
    text=ent.get()
    txt_sp=gTTS(text=text,lang="gu")
    txt_sp.save("audio.wav")
    os.system("audio.wav")
#Labels
enter=Label(window,text="Enter your text")
enter.pack()
#ENtrys 
ent=Entry(window)
ent.pack()

#button
bu=Button(window,text="Go",command=speech)
bu.pack()
window.mainloop()