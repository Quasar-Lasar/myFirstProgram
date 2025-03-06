inventory = []

try:
    f = open("inventory.txt","r")
    inventory = eval(f.read())
    f.close()
except:
    print("File didnt load, new file will be created")

def add():
    addItem = input("Add an item:").capitalize()
    inventory.append(f"{addItem}")
    print(f"{addItem} added")

def view():
    print()
    seen = []
    for item in inventory:
        if item not in seen:
            print(f"{item}: {inventory.count(item)}")
            seen.append(item)
    
def remove():
    removeItem = input("Which item do you want to remove: ").capitalize()
    if removeItem in inventory:
        inventory.remove(removeItem)
        print(f"{removeItem} removed from inventory")
    else:
        print("This item is not in inventory")

while True:
    print()
    print("Inventory")
    print("=========")
    menu = input("\n1: Add\n2: View\n3: Remove\n>>>")
    if menu == '1':
        add()
    elif menu == '2':
        view()      
    elif menu == '3':
        remove()

    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()

#def viewalt():
    #seen = set(inventory)
    #for item in seen:
        #print(f"{item}: {inventory.count(item)}")
