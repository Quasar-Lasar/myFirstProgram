import tkinter as tk

window = tk.Tk()
window.title("Graphic Novel")
window.geometry("960x540")

shotsFired = 0

def shotCounter():
    global shotsFired 
    shotsFired += 1
    blabel["text"] = f"PEW  "*shotsFired
    blabel.pack()
    if shotsFired == 5:
        shotsFired = 0
        blabel.pack_forget()
        bossDead()

def openDoor():
    buttonTwo.pack()
    button.pack_forget()
    buttonOne.pack_forget()
    canvas.itemconfig(container,image=bImage)
    label["text"] = f"Shoot to kill the boss"
    blabel.pack_forget()

def goBack():
    button.pack_forget()
    buttonOne.pack_forget()
    canvas.itemconfig(container,image=lImage)
    label["text"] = f"You have left the castle, The nazi's won the war!!!"
    blabel.pack_forget()
    buttonThree.pack()

def bossDead():
    canvas.itemconfig(container,image=dImage)
    buttonTwo.pack_forget()
    buttonFour.pack()
    label["text"] = f"You killed the boss"

def finish():
    canvas.itemconfig(container,image=tImage)
    buttonTwo.pack_forget()
    label["text"] = f"YOU KILLED THE BOSS AND FOUND THE TREASURE"
    buttonFour.pack_forget()
    buttonThree.pack()

def restart():
    label["text"] = f"You are inside castle wolfenstein. Choose wisely which way you go 🫡"
    canvas.itemconfig(container,image=stImage)
    buttonThree.pack_forget()
    button.pack()
    buttonOne.pack()
    blabel["text"] = f"Which way do you want to go"
    
label = tk.Label(text= f"You are inside castle wolfenstein. Choose wisely which way you go 🫡")
label.pack()

canvas = tk.Canvas(window, width=820, height=505)
canvas.pack()

blabel = tk.Label(text= f"Which way do you want to go")
blabel.pack()

button = tk.Button(text="Open the door",command=openDoor )
button.pack()
buttonOne = tk.Button(text="Go back",command=goBack)
buttonOne.pack()
buttonTwo = tk.Button(text="Shoot for your life",command=shotCounter)
buttonThree = tk.Button(text="Restart",command=restart)
buttonFour = tk.Button(text="Continue",command=finish)

stImage = tk.PhotoImage(file="wolfStart.png")
stImage = stImage.subsample(1)
bImage = tk.PhotoImage(file="wolfBoss.png")
bImage = bImage.subsample(1)
dImage = tk.PhotoImage(file="wolfDead.png")
dImage = dImage.subsample(1)
tImage = tk.PhotoImage(file="wolfTreasure.png")
tImage = tImage.subsample(1)
lImage = tk.PhotoImage(file="wolfLift.png")
lImage = lImage.subsample(1)
container = canvas.create_image(410,260,image= stImage)

tk.mainloop()