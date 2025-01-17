from tkinter import *
import random
word_dict = {"go": "og", "Apple": "elapp", "Chair": "haric", "River": "revir", "Book": "kobo", "Cloud": "ldcou", "Tree": "eert", "Car": "rac", "Star": "arts", "House": "hesuo", "Smile": "ielsmi", "Water": "retaw", "Door": "rodo", "Grass": "ssagr", "Light": "thgil", "Bird": "dibr", "Flower": "oewflr", "Road": "doar", "Friend": "dnreif", "Rain": "nair", "Moon": "onmo"}
window = Tk()
window.geometry("200x300")
window.config(bg="light green")
def choose():
    scrambled_word = random.choice(list(word_dict.values()))
    word.config(text=scrambled_word)
#label
word=Label(window)
word.pack()
#Entrys 
ent=Entry(window)
ent.pack()
#button
bu=Button(window,text="Go",command=choose)
bu.pack()
window.mainloop()