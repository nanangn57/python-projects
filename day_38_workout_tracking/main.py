import requests
from datetime import datetime
import json

with open("..\config.json", "r") as f:
    config = json.load(f)['workout']

APP_NUTRITION_ID = config['nutrition_id']
APP_NUTRITION_KEY = config['nutrition_key']

GENDER = "female"
WEIGHT_KG = config['weight']
HEIGHT_CM = config['height']
AGE = config['age']

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": input("What did you do? "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
}

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_NUTRITION_ID,
    'x-app-key': APP_NUTRITION_KEY
}

response = requests.post(url=url, json=params, headers=headers)
response = response.json()

SHEETY_USER = config['sheety_user']
SHEETY_url = f'https://api.sheety.co/{SHEETY_USER}/myWorkouts/workouts'

for i in range(len(response['exercises'])):
    body = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.today().strftime("%H:%M:%S"),
            "exercise": response['exercises'][i]['name'],
            "duration": response['exercises'][i]['duration_min'],
            "calories": response['exercises'][i]['nf_calories']
        }
    }

    headers = {
        "Authorization": config['sheety_authentication']
    }

    post_response = requests.post(url=SHEETY_url, json=body, headers=headers)
