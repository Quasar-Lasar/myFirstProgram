def font_color(color):
    if color == 'red':
        return("\033[31m")
    elif color == 'green':
        return("\033[32m")
    elif color == 'yellow':
        return("\033[33m")  
    elif color == 'blue':   
        return("\033[34m")
    elif color == 'purple':
        return("\033[35m")
    elif color == 'cyan':
        return("\033[36m") 
    elif color == 'reset':
        return("\033[0m")
    else:
        return("Invalid color")
    
def makePin (number):
    import random
    pin = ""
    for i in range(number):
        pin += str(random.randint(0,9))
    return pin

def rollDice(sides):
    import random
    result = random.randint(1 ,sides)
    return result

     
