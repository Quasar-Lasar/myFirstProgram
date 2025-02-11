import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)+rollDice(8))/2)
  return strengthStat
counter = 1
while counter <= 2:
  print()
  print(" Create fighter \n")
  if counter == 1:
    name = input("Name of fighter 1: ")
    player1 = "\033[31m" + name + "\033[0m"
    player1Health = health()
    player1strength = strength()
    counter += 1
  elif counter == 2:
    name = input("Name of fighter 2: ")
    player2 = "\033[34m" + name + "\033[0m"
    player2Health = health()
    player2strength = strength()  
    counter += 1

os.system('cls')
print('player_1:', player1,'\n' "health:", player1Health,'\n' "strength:", player1strength)
print()
print('player_2:', player2,'\n' "health:", player2Health,'\n' "strength:", player2strength)
print()
time.sleep(5)
print(" BATTLE BEGINS ")
print()
counter = 1
while counter <= 3:
  print("\033[35m""Round ",counter," Fight!""\033[0m")
  time.sleep(5)
  attack = rollDice(6) + player1strength
  player2Health = player2Health - attack
  print(player1, 'attacks', player2, 'for', attack, 'damage!')
  print()
  print(player2, 'health:', player2Health)
  print()
  if player2Health <= 0:
    print(player1, 'wins!')
    break
  time.sleep(5)
  attack = rollDice(6) + player2strength
  player1Health = player1Health - attack
  print(player2, 'attacks', player1, 'for', attack, 'damage!')
  print()
  print(player1, 'health:', player1Health)
  print()
  if player1Health <= 0:
    print(player2, 'wins!')
    break
  counter += 1

while counter == 3: 
  if player1Health > player2Health:
    print(player1, 'wins!')
    exit()
  elif player1Health < player2Health: 
    print(player2, 'wins!')
    exit()
  else:
    print('It is a draw!')
    exit()  


