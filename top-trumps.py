import os, time
toDoList = []

f = open("todolist.txt", "r")   # Once list is created, delete hash tags otherwise it will be overwritten.
toDoList = eval(f.read())	# or comment out these three lines of code when starting a new list 
f.close()

def printList():
  print()
  for items in toDoList:
    print(items)
  print()

while True:
  menu = input("""ToDo List Manager\nDo you want to \n1.view\n2.add\n3.edit\n4.remove\n5.delete the todo list?\n>>>""")
  if menu=="1":
    printList()
  elif menu=="2":
    item = input("What do you want to add?\n").title()
    date = input("Date todo by: ")
    toDoList.append(f"{item}: {date}")
  elif menu=="4":
    item = input("What do you want to remove?\n").title()
    check = input("Are you sure you want to remove this?\n")
    if check[0]=="y":
      if item in toDoList:
        toDoList.remove(item)
  elif menu=="3":
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(toDoList)):
      if toDoList[i]==item:
        toDoList[i]=new
  elif menu=="5":
    toDoList = []

  f = open("todolist.txt", "w")
  f.write(str(f"{toDoList}\n"))
  f.close()

  time.sleep(1)
  os.system('cls')



