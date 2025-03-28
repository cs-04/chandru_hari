import requests
from dotenv import load_dotenv
import os

# Load API credentials
load_dotenv()
API_URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"
API_ID = os.getenv("e1b9857d")
API_KEY = os.getenv("c1d675e4edeada53afd579be4f4e1c22")

def get_nutrition_info(food_item):
    """Fetches calorie, protein, and fat information using Nutritionix API."""
    
    headers = {
        "x-app-id": "e1b9857d",
        "x-app-key": "c1d675e4edeada53afd579be4f4e1c22",
        "Content-Type": "application/json"
    }

    data = {"query": food_item}

    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        foods = result.get("foods", [])
        
        if foods:
            food = foods[0]
            food_name = food.get("food_name", "Unknown")
            calories = food.get("nf_calories", "N/A")
            protein = food.get("nf_protein", "N/A")
            fat = food.get("nf_total_fat", "N/A")

            return (
                f"\n🍽️ {food_name.capitalize()} Nutrition Info:\n"
                f"🔸 Calories: {calories} kcal\n"
                f"🔸 Protein: {protein} g\n"
                f"🔸 Fat: {fat} g\n"
            )
        else:
            print("API response:", result)
            return "No nutrition data found for the given food item."
    else:
        return f"Error: Unable to fetch data ({response.status_code}) - {response.text}"

# Input from user
food_item = input("Enter the food name: ")
print(get_nutrition_info(food_item))
