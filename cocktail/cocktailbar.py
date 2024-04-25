import requests

def get_cocktail_recipe(cocktail_name):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_name}"
    response = requests.get(url)
    data = response.json()

    if data["drinks"]:
        drink = data["drinks"][0]
        print(f"{cocktail_name} Recipe:")
        print("Ingredients:")
        print("-" * 40)
        for i in range(1, 16):
            ingredient = drink.get(f"strIngredient{i}")
            measure = drink.get(f"strMeasure{i}")
            if ingredient:
                print(f"{ingredient}: {measure}")
        print("-" * 40)
        print("\nInstructions:")
        print(drink["strInstructions"])
    else:
        print(f"{cocktail_name} recipe not found.")

def get_cocktail_suggestions():
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a"
    response = requests.get(url)
    data = response.json()

    if data["drinks"]:
        print("Cocktail Suggestions:")
        for index, drink in enumerate(data["drinks"], start=1):
            print(f"{index}. {drink['strDrink']}")
    else:
        print("No cocktail suggestions found.")

if __name__ == "__main__":
    get_cocktail_suggestions()
    cocktail_name = input("\nEnter the name of the cocktail you want to know the recipe for: ")
    get_cocktail_recipe(cocktail_name)
