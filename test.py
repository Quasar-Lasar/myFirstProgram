print(f"MokeBeasts")
beasts = {}
def prettyPrint():
    for key, value in beasts.items():
        print(key, value) #"""day 46 : 3:40 bit to drunk to understand this,will try better tomoz, fuck i miss my dad :(

while True:
    menu = input(f"1:Add:\n2:View:\3Remove:\n>>>")
    if menu == "1":
        name = input(f"name your beast: ")
        typeb = input(f"type: ")
        hp = input(f"HP: ")
        mp = input(f"MP: ")
        beasts[name] = {"Type": typeb, "HP":hp, "MP":mp} 
    elif menu == "2":
        prettyPrint() 
    elif menu == "3":
        name = input(f"which Mokebeast do you want to remove? ")
        if name in beasts:
            beasts.re
    
