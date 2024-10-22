import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


data = pd.read_excel('calorie_data.xlsx')

print("Food Calorie Dataset:\n")
print(data)


food_dict = dict(zip(data['Food_Item'], data['Calories_per_100g']))


X = np.array([100] * len(data)).reshape(-1, 1)  
y = data['Calories_per_100g'].values


model = LinearRegression()
model.fit(X, y)


def predict_calories_ml():
    total_calories = 0
    quantities = []
    
    while True:
        try:
        
            food_item = input("\nEnter the food item you consumed (or type 'exit' to finish): ").capitalize()
            
            if food_item.lower() == 'exit':
                break
            
            if food_item in food_dict:
                quantity = float(input(f"Enter the quantity of {food_item} in grams: "))
                quantities.append([quantity])
                calories_predicted = model.predict(np.array([[quantity]]))
                total_calories += calories_predicted[0]
                print(f"{food_item} ({quantity}g) adds {calories_predicted[0]:.2f} calories to your total (predicted using ML).")
            else:
                print("Sorry, the food item is not in the database. Please try another one.")
        except ValueError:
            print("Invalid input. Please enter a number for the quantity.")
    
    print(f"\nYour total calorie intake for the day (predicted using ML) is: {total_calories:.2f} calories.")


predict_calories_ml()
