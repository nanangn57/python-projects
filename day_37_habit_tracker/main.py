import requests
from datetime import datetime
import json


with open("..\config.json", "r") as f:
    config = json.load(f)['pixela']

USERNAME = config['username']
TOKEN = config['token']

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = "https://pixe.la/v1/users"

# #Set up user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Pages Graph",
    "unit": "Page",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# # Create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
#
# pixel_config = {
#     "date": f'{datetime.today().strftime("%Y%m%d")}',
#     "quantity": input("How many pages you read today?")
# }

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# pixel_update_endpoint = f"{pixel_endpoint}/20240811"
#
# pixel_config = {
#     "quantity": "5"
# }
#
# response = requests.put(url=pixel_update_endpoint, json=pixel_config, headers=headers)
# print(response.text)
