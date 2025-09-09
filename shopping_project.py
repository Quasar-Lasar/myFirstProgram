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

def prettyPrint(shopping_list):
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
            print(f"{quantity:<5}|{ingredient:<15}")
        print("\033[0m")

def go_shopping(recipes):
    print("Available recipes:")
    for recipe in recipes.keys():
        print(f"- {recipe}")

    selected_meals_input = input("\nEnter the meals you want (comma-separated): ").lower().split(",") 
    selected_meals = [meal.strip() for meal in selected_meals_input if meal.strip() in recipes]
    invalid_meals = [meal.strip() for meal in selected_meals_input if meal.strip() and meal.strip() not in recipes]

    if invalid_meals:
        print(f"\nI don't recognize these meals: {', '.join(invalid_meals)}\n")

    if not selected_meals:
        print("No valid meals selected, try again:\n")
        return None
        
    selected_recipes = [recipes[meal] for meal in selected_meals]
    shopping_list = shopping_list_accumulator(*selected_recipes)

    prettyPrint(shopping_list)
    return shopping_list

def edit_recipe(recipes, csv_filename='recipes.csv'):
    recipe_to_edit = input("Enter the recipe name to edit: ")
    if recipe_to_edit not in recipes:
        print("Recipe not found.")
        return
    print(f"Ingredients in '{recipe_to_edit}':")
    for ingredient, quantity in recipes[recipe_to_edit].items():
        print(f"- {ingredient}: {quantity}")
    action = input("Type 'edit' to change quantity, 'add' to add ingredient, 'remove' to delete ingredient: ").lower()
    if action == "edit":
        ingredient_to_edit = input("Enter the ingredient to edit: ")
        if ingredient_to_edit in recipes[recipe_to_edit]:
            new_quantity = input(f"Enter new quantity for {ingredient_to_edit}: ")
            try:
                recipes[recipe_to_edit][ingredient_to_edit] = int(new_quantity)
                print(f"{ingredient_to_edit} updated.")
            except ValueError:
                print("Invalid quantity.")
        else:
            print("Ingredient not found in recipe.")
    elif action == "add":
        new_ingredient = input("Enter new ingredient name: ")
        new_quantity = input(f"Enter quantity for {new_ingredient}: ")
        try:
            recipes[recipe_to_edit][new_ingredient] = int(new_quantity)
            print(f"{new_ingredient} added.")
        except ValueError:
            print("Invalid quantity.")
    elif action == "remove":
        ingredient_to_remove = input("Enter the ingredient to remove: ")
        if ingredient_to_remove in recipes[recipe_to_edit]:
            del recipes[recipe_to_edit][ingredient_to_remove]
            print(f"{ingredient_to_remove} removed.")
        else:
            print("Ingredient not found in recipe.")
    else:
        print("Unknown action.")

    # Save all recipes back to recipes.csv
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['recipe', 'ingredient', 'quantity'])
        writer.writeheader()
        for recipe_name, ingredients in recipes.items():
            for ingredient, quantity in ingredients.items():
                writer.writerow({'recipe': recipe_name, 'ingredient': ingredient, 'quantity': quantity})
    print(f"Recipe '{recipe_to_edit}' updated in {csv_filename}.")

def add_new_recipe(recipes, csv_filename='recipes.csv'):
    new_recipe = input("Enter new recipe name: ")
    if new_recipe in recipes:
        print("Recipe already exists.")
        return
    recipes[new_recipe] = {}
    new_rows = []
    while True:
        ingredient = input("Add ingredient (or type 'done'): ")
        if ingredient.lower() == 'done':
            break
        quantity = input(f"Enter quantity for {ingredient}: ")
        try:
            recipes[new_recipe][ingredient] = int(quantity)
            new_rows.append({'recipe': new_recipe, 'ingredient': ingredient, 'quantity': int(quantity)})
        except ValueError:
            print("Invalid quantity, try again.")
    if new_rows:
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['recipe', 'ingredient', 'quantity'])
            for row in new_rows:
                writer.writerow(row)
    print(f"Recipe '{new_recipe}' added and saved to {csv_filename}.")

shopping_list = {}

while True:
    print("\nMenu:")
    print("1: Go shopping")
    print("2: Check out ingredients in shopping list")
    print("3: Edit ingredients")
    print("4: Add a new recipe")
    print("5: Exit")
    menu = input(">>> ")

    if menu == "1":
        shopping_list = go_shopping(recipes)

    elif menu == "2":
        print("Available recipes:")
        for recipe in recipes.keys():
            print(f"- {recipe}")                                

    elif menu == "3":
        edit_recipe(recipes)

    elif menu == "4":
        add_new_recipe(recipes)

    elif menu == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option, please try again.")