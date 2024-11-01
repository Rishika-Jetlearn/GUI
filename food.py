from tkinter import*
window=Tk()
window.geometry("400x500")
window.title("Number guessing game")
window. configure(bg="#afedd3")

#buttons
image1=PhotoImage(file="pizzaaa.png")
pizza=Button(window,image=image1)
pizza.grid(row=2,column=2,padx=130,pady=50)

chips=Button(window)
chips.grid(row=3,column=2,padx=130,pady=50)

burger=Button(window)
burger.grid(row=4,column=2,padx=130,pady=50)


#lables
piz=Label(window)


chi=Label(window)


bur=Label(window)



def facts():

    pfacts=piz.config(text="The world’s first pizzeria opened in Naples, Italy, in 1738, but pizza didn’t become popular worldwide until after World War II! American soldiers stationed in Italy developed a love for the local pizza and brought their enthusiasm for it back home, sparking its boom in the U.S,then being known worldwide!")
    cfacts=chi.config(text="Here’s a cool fact about chips on their own: the world record for the largest serving of chips was set in 2020 in Melbourne, Australia. Weighing over 1.5 tons (or about 3,000 pounds), this mega-portion used thousands of potatoes and took a team of chefs to pull off. Now that’s a serious chip craving!")
    bfacts=bur.config(text="Did you know that in the early 2000s, a burger chain called Burger King launched a promotion called the “Left-Handed Whopper”? They claimed it was designed specifically for left-handed people, with all the ingredients rotated 180 degrees. It was an April Fools' joke, but many people believed it and even requested it! The fun part? They made a whole marketing campaign around it, and it became a legendary prank in the fast food world!Talk about flipping the script on burgers! 🍔🤣")

window.mainloop()