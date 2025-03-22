import tkinter as tk

window = tk.Tk()
window.title("Graphic Noval")
window.geometry("960x540")

def openDoor():
    buttonTwo.pack()
    button.pack_forget()
    buttonOne.pack_forget()
    canvas.itemconfig(container,image=bImage)
    label["text"] = f"Shoot to kill the boss"
    blabel.pack_forget()

def boss():
    canvas.itemconfig(container,image=tImage)
    buttonTwo.pack_forget()
    label["text"] = f"YOU KILLED THE BOSS AND FOUND THE TREASURE"
    buttonThree.pack()

def goBack():
    button.pack_forget()
    buttonOne.pack_forget()
    canvas.itemconfig(container,image=dImage)
    label["text"] = f"YOUR DEAD, Hitler came up behind and killed you"
    blabel.pack_forget()
    buttonThree.pack()

def restart():
    label["text"] = f"You are inside wolfenstein castle. Choose wisely which way you go 🫡"
    canvas.itemconfig(container,image=stImage)
    buttonThree.pack_forget()
    button.pack()
    buttonOne.pack()
    blabel["text"] = f"Which way do you want to go"
    
label = tk.Label(text= f"You are inside wolfenstein castle. Choose wisely which way you go 🫡")
label.pack()

canvas = tk.Canvas(window, width=820, height=505)
canvas.pack()

blabel = tk.Label(text= f"Which way do you want to go")
blabel.pack()

button = tk.Button(text="Open the door",command=openDoor )
button.pack()
buttonOne = tk.Button(text="Go back",command=goBack)
buttonOne.pack()
buttonTwo = tk.Button(text="Shoot for your life",command=boss)
buttonThree = tk.Button(text="Restart",command=restart)

stImage = tk.PhotoImage(file="wolfStart.png")
stImage = stImage.subsample(1)
bImage = tk.PhotoImage(file="wolfBoss.png")
bImage = bImage.subsample(1)
dImage = tk.PhotoImage(file="wolfDead.png")
dImage = dImage.subsample(1)
tImage = tk.PhotoImage(file="wolfTreasure.png")
tImage = tImage.subsample(1)
container = canvas.create_image(410,260,image= stImage)

tk.mainloop()