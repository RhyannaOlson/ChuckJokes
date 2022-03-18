import requests
import json
from pprint import pprint

url = "https://api.icndb.com/jokes/random"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

responseJson = response.json()

print("Your randomly generated Chuck Norris joke is: " + str(responseJson['value']['joke']))
print("You're Welcome...")

