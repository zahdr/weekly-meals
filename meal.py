import os
import random
   
if __name__ == "__main__":
    dataFile = "meal-list.txt"
    meals = []
    with open(dataFile, "r") as myFile:
        for line in myFile:
            meals.append(line.rstrip())

    print("Wie viele Gerichte möchtest du haben?")
    amount = int(input())

    pickedMeals = random.sample(range(0, len(meals)), amount)

    while True:
        print("\nDeine Gerichte:")
        for i in range(len(pickedMeals)):
            print(f"{i+1}. {meals[pickedMeals[i]]}")

        print("\n\nWelches Gericht möchtest du durch ein neues ersetzen?")
        replaceMeal = int(input())

        uniqueMeal = False
        while uniqueMeal == False:
            newMeal = random.randint(0, len(meals))
            if newMeal not in pickedMeals:
                uniqueMeal = True
        
        pickedMeals[replaceMeal-1] = newMeal
