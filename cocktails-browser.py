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



def main():
    # drinks must be the
    drinks = ask_name()["drinks"]
    print_drink_info(drinks)    



if __name__ == '__main__':
    main()