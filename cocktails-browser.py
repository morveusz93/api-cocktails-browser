import requests
import json


def ask_name():
    print("Type name of coctail to search: :")
    name = input()
    response = requests.get(f'http://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}').json()
    # print(json.dumps(response, indent=4))
    return response


def print_drink_info(drinks):
    for drink in drinks:
        print("\n")
        print("Name: " + drink['strDrink'])
        print("Category: " + drink['strCategory'])
        ingredients = ''
        for i in  range(1,10):
            if drink[f'strIngredient{i}'] != None:
                ingredients = ingredients + drink[f'strIngredient{i}'] + ', '
        print("Ingredients: " + ingredients)
        print("Instructions: " + drink['strInstructions'])
        print("Picture: " + drink['strDrinkThumb'])
        print("\n")


def random_cocktail():
    response = requests.get('http://www.thecocktaildb.com/api/json/v1/1/random.php').json()
    # print(json.dumps(response, indent=4))
    return response


def menu():
    print("[1] - Search by coctail name")
    print("[2] - Random coctail")
    print("[0] - Leave")
    return input()


def main():
    print("Welcome to Coctail Browser!\n")
    user_choice = 'm'
    while True:
        # print menu
        if user_choice == 'm':
            user_choice = menu()
        elif user_choice == '1':
            # search coctail by name
            drinks = ask_name()["drinks"]
            if drinks != None:
                print_drink_info(drinks)    
            else:
                # there is no result with this name
                print("\nWe found nothing. Try somthing else\n")
            user_choice = menu()
        elif user_choice == '2':
            random_drink = random_cocktail()["drinks"]
            if random_drink != None:
                print_drink_info(random_drink)    
            else:
                # there is no result with this name
                print("We found nothing. Try somthing else\n")
            user_choice = menu()
        elif user_choice == '0':
            break
        else:
            print("Wrong choice")
            user_choice = menu()


if __name__ == '__main__':
    main()