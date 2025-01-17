from tkinter import*
import speech_recognition as sr
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
#internally uses pyaudio
window=Tk()
window.geometry("400x500")
window.config(bg="teal")

def save():
    asf=asksaveasfile()
    if asf:
        content=textbox.get(1.0,END)
        print(content,file=asf)
    else:
        messagebox.showwarning("Warning!","File not saved")
def translate():
    reco=sr.Recognizer()
    with sr.Microphone() as source:
        audio=reco.listen(source)
        try:
            text=reco.recognize_google(audio)
            textbox.delete(1.0,END)
            textbox.insert(END,text)
        except:
            messagebox.showerror("Error","Sorry,could not recognize your voice")
#lable
heading=Label(window,text="Voice Notepad")
heading.grid(row=1,column=2,columnspan=3)
#buttons
click=Button(window,text="Click me to start recording!",command=translate)
click.grid(row=2,column=1)

save=Button(window,text="Save the text",command=save)
save.grid(row=2,column=3)
#textbox
textbox=Text(window,width=20,height=10)
textbox.grid(row=2,column=2)


window.mainloop()