# Compare FF for specific environments
import os
import requests

# Get FF for specific env
PROJECT_KEY = os.getenv("PROJECT_KEY")
ENV1 = os.getenv("ENV1")
ENV2 = os.getenv("ENV2")
API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

headers = {"Authorization": API_KEY}

response = requests.get(URL + PROJECT_KEY, headers=headers)
data = response.json()

# Iterate through data to find the flag
failedItems = []
for item in data["items"]:
    isMatch = item["environments"][ENV1]["on"] == item["environments"][ENV2]["on"]
    if isMatch == False:
         print("Flag failed to match: ", item["name"], " (Staging: ", item["environments"]["test"]["on"], "| Production: ", item["environments"]["production"]["on"],")")
         failedItems.append(item["name"])
# Check if anything failed
if len(failedItems) != 0:
    exit(1)
else:
    print(ENV1 + " and " + ENV2 + " flags match!")