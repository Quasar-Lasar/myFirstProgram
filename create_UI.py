import os
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
os.system('cls')
title = f"{font_color('red')}={font_color('reset')}={font_color('blue')}={font_color('yellow')} Music App {font_color('blue')}={font_color('reset')}={font_color('red')}={font_color('reset')}" 
prev = 'Prev'
next = 'Next'
pause = 'Pause'
print(f"{title:^80}")
print()
print(f"\tRadio Gaga")
print(f"\t{font_color('yellow')}Queen{font_color('reset')}")
print()
print(f"{prev:<40}")
print(f"{font_color('green')}{next:^40}")
print(f"{font_color('purple')}{pause:>40}{font_color('reset')}")
print()
Welcome = 'Welcome to'
armbook = '--    Armbook    --'
bio = "Definitely not a rip off of"
bio1 = "a certain other social"
bio2 = "networking site."
Honest = 'Honest.'
user = 'Username:'
passw = 'Password:'
print(f"{Welcome:^80}")
print(f"{font_color('blue')}{armbook:^80}")
print()
print(f"{font_color('yellow')}{bio:>80}")
print(f"{bio1:>80}")
print(f"{bio2:>80}")
print()
print(f"{font_color('red')}{Honest:^80}{font_color('reset')}")
print()
print(f"{user:^80}")
print(f"{passw:^80}")
print()





    


