import os, time, random
print(f"Top trumps\n")
n = "Name"
i = "Intelligence"
s = "Speed"
d = "Damage"
characters = {}

def prettyPrint():
    print(f"{n:^15} {i:^15} {s:^15} {d:^15}")
    for key, value in characters.items():
        print(f"----------------------------------------------------------------")
        print(f"{key:^15}|{value["Intelligence"]:^15}|{value["Speed"]:^15}|{value["Damage"]:^15}|")
    print()

def playGame():
    print(f"Select your character: ")
    print(f"----------------------")
    for key in characters.keys():
        print(f"{key}")
    playerone = input(f">>> ").title()
    if playerone in characters.keys():
        print()
        playerTwo = random.choice(list(characters.keys()))
        print(f"{playerone} vs {playerTwo}")
        print()
        print(f"Intelligence, Speed or Damage")
        fightStat = input(f"Choose your best stat:  ").title() 
        print(f"{playerone}: {characters[playerone][fightStat]}")
        print(f"{playerTwo}: {characters[playerTwo][fightStat]}")
        if characters[playerone][fightStat] > characters[playerTwo][fightStat]:
            print()
            print("Player 1 wins")
        elif characters[playerone][fightStat] < characters[playerTwo][fightStat]:
            print()
            print("Computer wins")
        else:
            print()
            print("Draw")

    else:
        print(f"{playerone} is not in the list")
        print()
    time.sleep(2)
    print()



characters = {"Xenomorph":{"Intelligence":2,"Speed":8,"Damage":10}, "Scorpion":{"Intelligence":4,"Speed":8,"Damage":5},
"Terminator":{"Intelligence":6,"Speed":4,"Damage":8}, "Sho Kahn":{"Intelligence":7,"Speed":8,"Damage":9},
"Neo":{"Intelligence":10,"Speed":10,"Damage":6}, "Rocky Bilboa":{"Intelligence":2,"Speed":5,"Damage":5}, 
"Diablo":{"Intelligence":4,"Speed":6,"Damage":9}}

while True:
    menu = input(f"Main menu\n1: Play game\n2: View characters\n3: Add character\n4: Exit game\n>>>")
    if menu == "1":
        os.system("cls")
        playGame()
    elif menu == "2":
        print()
        prettyPrint()
    elif menu == "3":
        name = input(f"Name: ")
        intelligence = int(input(f"Intelligence out of 10: "))
        speed = int(input(f"Speed out of ten: "))
        damage = int(input(f"Damage out of 10: "))
        characters = {name:{intelligence,speed,damage}} # At the moment this overwrites the whole dictionary
    elif menu == "4":
        print(f"You have quit the game")
        exit()



