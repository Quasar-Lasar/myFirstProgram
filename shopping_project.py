import os, csv

print()
print("Shopping List Accumulator")
print()

def load_recipes_from_csv(file_path):
    recipes = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recipe = row['recipe']
            ingredient = row['ingredient']
            quantity = int(row['quantity'])
            if recipe not in recipes:
                recipes[recipe] = {}
            recipes[recipe][ingredient] = quantity
    return recipes

recipes = load_recipes_from_csv('recipes.csv')

def shopping_list_accumulator(*args):
    shopping_list = {}
    for recipe in args:
        for ingredient, quantity in recipe.items():
            if ingredient in shopping_list:
                shopping_list[ingredient] += quantity
            else:
                shopping_list[ingredient] = quantity
    return shopping_list

def prettyPrint():
    print("\nHappy Shopping!\n")
    categories = [
        ("(m)", "\033[31mMeat:"),
        ("(v)", "\033[32mVegetables:"),
        ("(s)", "\033[36mSauce:"),
        ("(r)", "\033[35mRandom items:"),
        ("(sp)", "\033[34mSpice:")
    ]
    for category, color_code in categories:
        print(color_code)
        print("====================================================")
        matching_keys = {key: value for key, value in shopping_list.items() if category in key}
        for ingredient, quantity in matching_keys.items():
            print(f"{ingredient:<26}{quantity:>26}")
        print("\033[0m")

while True:
    print("Available recipes:")
    for recipe in recipes.keys():
        print(f"- {recipe}")

    selected_meals = input("\nEnter the meals you want (comma-separated): ").lower().split(",")
    selected_meals = [meal.strip() for meal in selected_meals if meal.strip() in recipes]

    if not selected_meals:
        print("\nNo valid meals selected, try again: ")
        print()
        continue
        
    selected_recipes = [recipes[meal] for meal in selected_meals]
    shopping_list = shopping_list_accumulator(*selected_recipes)

    prettyPrint()
    break