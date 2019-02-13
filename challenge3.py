
# https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json

#goal: calculate average grade

import json

import requests

request_url = "https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json"
response = requests.get(request_url)

parsed_response = json.loads(response.text)

breakpoint()