from colorama import Fore, Style, init
import os
os.system('cls')
print("Shopping List Acumulator")
print()
stew = {'diced beef(m)':1, 'carrots(v)':3, 'celery(v)':2, 'onion(v)':1, 'red wine(r)':1, 
        'plain flour(r)':1, 'rosemary(s)':1, 'bay leaves(s)':1, 'suet(r)':1, 'self raising flour(r)':1,
         'potatoes(v)   KG>':1.5}
spagbol = {'mince(m)':1, 'tinned chopped tomatoes(r)':1, 'garlic(s)':4, 'mixed herbs(s)':1, 'worcestershire sauce(r)':1, 
           'onion(v)':1, 'carrots(v)':1, 'spaghetti(r)':1, 'garlic bread(r)':1,}
meatballs = {'meatballs(m)':1, 'tinned chopped tomatoes(r)':1, 'garlic(s)':4, 'mixed herbs(s)':1, 
            'worcestershire sauce(r)':1, 'onion(v)':1, 'carrots(v)':1, 'spaghetti(r)':1, 'garlic bread(r)':1,}
lasagne = {'mince(m)':1, 'tinned chopped tomatoes(r)':1, 'garlic(r)':4, 'oregano(s)':1, 'worcestershire sauce(r)':1, 
            'onion(v)':1, 'carrots(v)':1, 'lasagne sheets(r)':1, 'bacon(m)':1}
chicken_curry = {'chicken breasts(m)':2, 'tinned chopped tomatoes(r)':1, 'garam masala(s)':1, 'cumin(s)':1, 
                'chillis(s)':1, 'tumeric(s)':1, 'onion(v)':1, 'garlic(v)':4, 'chilli powder(s)':1, 'rice(r)':1, 
                'naan bread(r)':1, 'poppadoms(r)':1}
chilli = {'mince(m)':1, 'tinned chopped tomatoes(r)':1, 'garlic(s)':4, 'kidney beans(r)':1, 'beef stock(s)':1, 
          'cumin(s)':1, 'mild chilli powder(s)':1, 'paprika(s)':1, 'chillis(s)':1, 'mixed peppers(v)':1, 'onion(v)':1}
def shopping_list_accumulator(*args):
    shopping_list = {}
    for recipe in args:
        for ingredient, quantity in recipe.items():
            if ingredient in shopping_list:
                shopping_list[ingredient] += quantity
            else:
                shopping_list[ingredient] = quantity
    return shopping_list
shopping_list = shopping_list_accumulator(stew, spagbol, meatballs, lasagne, chicken_curry, chilli)
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
for i, (ingredient, quantity) in enumerate(shopping_list.items()):
    color = colors[i % len(colors)]
    print(f"{color}{ingredient:<26}{quantity:>26}\033[0m")
print()
print("Happy Shopping!")
print()
print()
search_text = "(m)"
matching_keys ={key: value for key, value in shopping_list.items() if search_text in key}
print("\t\033[31m Meat:\n")
for i, (ingredient, quantity) in enumerate(matching_keys.items()):
    print(f"{ingredient:<26}{quantity:>26}")
print()
print()

search_text = "(v)"
matching_keys ={key: value for key, value in shopping_list.items() if search_text in key}
print("\t\033[32m Vegetables:\n")
for i, (ingredient, quantity) in enumerate(matching_keys.items()):
    print(f"{ingredient:<26}{quantity:>26}")
print()
print()

search_text = "(s)"
matching_keys ={key: value for key, value in shopping_list.items() if search_text in key}
print("\t\033[36m Spice:\n")
for i, (ingredient, quantity) in enumerate(matching_keys.items()):
    print(f"{ingredient:<26}{quantity:>26}")
print()
print()

search_text = "(r)"
matching_keys ={key: value for key, value in shopping_list.items() if search_text in key}
print("\t\033[35m Random shit:\n")
for i, (ingredient, quantity) in enumerate(matching_keys.items()):
    print(f"{ingredient:<26}{quantity:>26}")

print("\033[0m")